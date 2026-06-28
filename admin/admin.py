from flask import Blueprint,render_template,redirect,session,request,flash,send_file
import util
from admin.forms import RenameUserForm,DeleteUserForm,AddUserForm,UserPasswordResetForm
from admin.query import updateName, getUserList, getUser,deleteUser,addUser,updatePassword
import mysql.connector
import subprocess
import io
import os



admin_bp = Blueprint('admin_bp', __name__,
                     template_folder='templates',
                     static_url_path='admin')

@admin_bp.route('/')
def show_admin():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Blueprint Admin Page",
        "pageTitle": "",
        "pageDescription": ""
    }
    return render_template('admin/admin.html',tvals=tvals)


@admin_bp.route('/renameUser/<int:uid>', methods=['GET','POST'])
def rename_user(uid):
    if not session.get("name"):
        return redirect("/DemoApp/login")
    if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Rename User",
        "pageTitle": "Password Update",
        "pageDescription": "Please enter user's new name",   
    }
    userInfo = getUser(uid)
    print("userInfo",flush=True)
    print(userInfo["user"],flush=True)
    form = RenameUserForm()
    if form.validate_on_submit():
        name = request.form.get("newName")
        
        updateName(uid,name)
        flash("Name updated","success")
        return redirect("/DemoApp")
    return render_template('admin/renameUser.html',oldName=userInfo["user"], tvals=tvals,form=form)


@admin_bp.route('/deleteUser/<int:uid>', methods=['GET','POST'])
def delete_user(uid):
    if not session.get("name"):
        return redirect("/DemoApp/login")
    if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Delete User",
        "pageTitle": "Delete User",
        "pageDescription": "",   
    }
    userInfo = getUser(uid)
    duser = userInfo['user']
    print("userInfo",flush=True)
    print(userInfo["user"],flush=True)
    form = DeleteUserForm()
    if form.validate_on_submit():
        if form.yes.data:
            deleteUser(uid)
            flash(f"User {duser} deleted.","success")
        if form.no.data:
            flash(f"User {duser} not deleted.","success")
        return redirect("/DemoApp")
    return render_template('admin/deleteUser.html',deleteName=duser, tvals=tvals,form=form)

@admin_bp.route('/addUser', methods=['GET','POST'])
def add_user():
   if not session.get("name"):
        return redirect("/DemoApp/login")
   if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")
   tvals = {
       "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Add User",
        "pageTitle": "Adding a New User",
        "pageDescription": ""
   } 
   form = AddUserForm()
   if form.validate_on_submit():
       username = form.username.data
       pwd = form.password.data
       password = util.password_hash(pwd)
       addUser(username,password)
       return redirect("/DemoApp")
   return render_template('admin/addUser.html',tvals=tvals, form=form)

@admin_bp.route('/userPasswordReset/<int:uid>', methods=['GET','POST'])
def user_password_reset(uid):
   if not session.get("name"):
        return redirect("/DemoApp/login")
   if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp/")
   tvals = {
       "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"User Password Reset",
        "pageTitle": "Reset Password",
        "pageDescription": ""
   } 
   form = UserPasswordResetForm()
   userInfo = getUser(uid)
   puser = userInfo['user']
   if form.validate_on_submit():
       pwd = form.newPassword.data
       password = util.password_hash(pwd)
       updatePassword(uid,password)
       return redirect("/DemoApp")
   return render_template('admin/userPasswordReset.html',puser=puser,tvals=tvals, form=form)

@admin_bp.route('/userList')
def list_users():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")

    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"User List",
        "pageTitle": "List of Current Users",
        "pageDescription": "This page displays the current users"
    }

    nres = getUserList()
    return render_template("admin/userList.html", tvals=tvals, rows=nres)
    
@admin_bp.route('/db_details', methods=['GET','POST'])
def database_details():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")
    config = util.db_config[dbname]
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Details",
        "pageTitle": "Database Details",
        "pageDescription": "This page displays DB host details"
    }
    return render_template('admin/dbDetails.html',config=config,tvals=tvals)


@admin_bp.route('/export_db', methods=['GET','POST'])
def export_database():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    if "admin" != session.get("name"):
        flash("Permission denied")
        return redirect("/DemoApp")
    try:
        # Construct the mysqldump command
        # Using --single-transaction for InnoDB tables to avoid locking
        # Using --add-drop-database to include DROP DATABASE IF EXISTS statement
        # Using -r to specify the output file, but we'll capture it via stdout
        #mysqldump=r"D:\bin\mysql-8.0.42-winx64\bin\mysqldump.exe"

        config = util.db_config[dbname]
        DB_HOST=config["host"]
        DB_USER=config["user"]
        DB_PASSWORD=config["passwd"]
        DB_NAME=config["database"]
        command = [
            'mysqldump',
            f'--host={DB_HOST}',
            f'--user={DB_USER}',
            f'--password={DB_PASSWORD}',
            '--single-transaction',
            '--add-drop-database',
            DB_NAME
        ]

        # Execute mysqldump command and capture stdout
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            flash(f"Error exporting database: {stderr.decode()}", "error")
            return redirect('/DemoApp')

        # Create an in-memory file-like object from the captured stdout
        # The output of mysqldump is typically bytes
        dump_buffer = io.BytesIO(stdout)
        dump_buffer.seek(0) # Rewind the buffer to the beginning

        # Set the filename for the download
        download_filename = f"{DB_NAME}_backup.sql"

        # Send the file to the client
        return send_file(
            dump_buffer,
            mimetype='application/sql',
            as_attachment=True,
            download_name=download_filename # Use download_name for newer Flask versions
            # For older Flask versions, use attachment_filename=download_filename
        )

    except FileNotFoundError:
        flash("Error: 'mysqldump' command not found. Please ensure MySQL client utilities are installed and in your system's PATH.", "error")
        return redirect('/DemoApp')
    except Exception as e:
        flash(f"An unexpected error occurred: {e}", "error")
        return redirect('/DemoApp')

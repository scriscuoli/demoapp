from flask import Blueprint,render_template,redirect,session,request,flash
import util
from user.forms import UpdatePasswordForm
from user.query import updatePassword,getUser
import mysql.connector


user_bp = Blueprint('user_bp', __name__,
                     template_folder='templates',
                     static_url_path='user')

@user_bp.route('/updatePassword/<int:uid>', methods=['GET','POST'])
def edit_user(uid):
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Password Update",
        "pageTitle": "Password Update",
        "pageDescription": "Please type yourpassword twice to update",   
    }
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        p = request.form.get("newPassword")
        newPassword = util.password_hash(p)
        updatePassword(uid,newPassword)
        flash("Password updated","success")
        return redirect("/DemoApp")
    return render_template('user/updatePassword.html',tvals=tvals,form=form)


@user_bp.route('/')
def show_user():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"Blueprint user Page",
        "pageTitle": "",
        "pageDescription": ""
    }
    return render_template('user/user.html',tvals=tvals)

    
@user_bp.route('/userProfile/<int:uid>', methods=['GET','POST'])
def user_profile(uid):
    if not session.get("name"):
        return redirect("/DemoApp/login")

    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"User Profile",
        "pageTitle": "Profile of Current User",
        "pageDescription": ""
    }
    
    nres = getUser(uid)
    return render_template("user/userProfile.html", tvals=tvals, row=nres)
from flask import Blueprint,render_template,redirect,session,request,current_app
import util
import os
from pathlib import Path


RESUMES_FOLDER = os.path.join("static", "images", "resumes")
OPENINGS_FOLDER = os.path.join("static", "images", "openings")


upload_bp = Blueprint('upload_bp', __name__,
                     template_folder='templates',
                     static_url_path='upload')

@upload_bp.route('/resumes')
def show_upload_resumes():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Upload Resumes",
        "pageTitle": "",
        "pageDescription": ""
    }

    resumes = [f.name for f in Path(RESUMES_FOLDER).iterdir() if f.is_file()]

    return render_template('upload/upload_resumes.html',resumes=resumes,tvals=tvals)

@upload_bp.route('/openings')
def show_upload_openings():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Upload Openings",
        "pageTitle": "",
        "pageDescription": ""
    }
    openings = [f.name for f in Path(OPENINGS_FOLDER).iterdir() if f.is_file()]

    return render_template('upload/upload_openings.html',openings=openings,tvals=tvals)

@upload_bp.route('/handleResumes', methods=['POST'])
def show_upload_handle_resumes():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Upload",
        "pageTitle": "",
        "pageDescription": ""
    }
    if request.method == 'POST':
        f = request.files.get('file')
        dest = os.path.join(RESUMES_FOLDER,f.filename)
        f.save(dest)
    return render_template('upload/upload_resumes.html',tvals=tvals)

@upload_bp.route('/handleOpenings', methods=['POST'])
def show_upload_handle_openings():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Upload",
        "pageTitle": "",
        "pageDescription": ""
    }
    if request.method == 'POST':
        f = request.files.get('file')
        dest = os.path.join(OPENINGS_FOLDER,f.filename)
        f.save(dest)
    return render_template('upload/upload_openings.html',tvals=tvals)
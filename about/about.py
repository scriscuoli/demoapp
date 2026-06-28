from flask import Blueprint,render_template,redirect,session
import util

about_bp = Blueprint('about_bp', __name__,
                     template_folder='templates',
                     static_url_path='about')

@about_bp.route('/')
def show_about():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : "",
        "name": session.get("name"),
        "title":"About",
        "pageTitle": "",
        "pageDescription": ""
    }
    return render_template('about/about.html',tvals=tvals)
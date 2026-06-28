from flask import Blueprint,render_template,redirect,session
import util

home_bp = Blueprint('home_bp', __name__,
                     template_folder='templates')

@home_bp.route('/')
def show_home():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":util.getSiteName() + " - Home Page",
        "pageTitle": "",
        "pageDescription": ""
    }
    return render_template('home/home.html',tvals=tvals)

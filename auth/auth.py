from flask import Blueprint,render_template,redirect,session,request
from auth.forms import LoginForm

import util


def checkUserPass(user,pwd):
    return 1

auth_bp = Blueprint('auth_bp', __name__,
                     template_folder='templates')


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    tvals = {
        "site": util.getSiteName(),
        "name": session.get("name"),
        "title":"Login",
        "pageTitle": "",
        "pageDescription": "",
        
    }
    form = LoginForm('auth/login.html')
    if request.method == "POST":
        # Record the user name in session
        n = request.form.get("name")
        p = request.form.get("password")
        id = checkUserPass(n,p)
        if id != 0:
            session["name"] = request.form.get("name")
            session["id"] = id
            return redirect("/DemoApp")
    return render_template("auth/login.html",tvals=tvals,form=form)

@auth_bp.route("/logout")
def logout():
    # Clear the username from session
    session["name"] = None
    session["id"] = None
    return redirect("/DemoApp")

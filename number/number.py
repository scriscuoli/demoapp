from flask import Blueprint,render_template,redirect,session,request
import util
import os
from pathlib import Path
from number.forms import NumberForm
from number.p6174 import process_num


number_bp = Blueprint('number_bp', __name__,
                     template_folder='templates',
                     static_url_path='number')

@number_bp.route('/', methods=["GET", "POST"])
def show_number():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Magic 6147",
        "pageTitle": "",
        "pageDescription": ""
    }
    
    numberPicked=""
    results = []
    form = NumberForm(numberPicked)
    if request.method == "POST":
        numberPicked = request.form.get("numberPicked")
        results = process_num(numberPicked)
    return render_template('number/number.html',form=form,tvals=tvals,numberPicked=numberPicked,results=results)


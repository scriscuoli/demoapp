from flask import Blueprint,render_template,redirect,session,request
import util
import os
from pathlib import Path
from dnd.forms import BackstoryForm
from dnd.builder import build_back_story,get_manifest



dnd_bp = Blueprint('dnd_bp', __name__,
                     template_folder='templates',
                     static_url_path='dnd')

@dnd_bp.route('/', methods=["GET", "POST"])
def show_dnd():
    if not session.get("name"):
        return redirect("/DemoApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"D&D",
        "pageTitle": "",
        "pageDescription": ""
    }
    form = BackstoryForm()
    backstory = {}
    manifest = get_manifest()
    if request.method == "POST":
        race = request.form.get("race")
        clazz = request.form.get("clazz")
        print(f"race={race}  class={clazz}")
        backstory = build_back_story(race,clazz=clazz)
        print(manifest)
        print(backstory)
    return render_template('dnd/dnd.html',form=form,tvals=tvals,manifest=manifest,backstory=backstory)


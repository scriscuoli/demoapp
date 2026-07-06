from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from flask_wtf.file import DataRequired
from werkzeug.utils import secure_filename
import os

class BackstoryForm(FlaskForm):
    race = SelectField('Race', 
        choices=[
            ("Dragonborn", "Dragonborn"),
            ("Dwarf", "Dwarf"),
            ("Elf", "Elf"),
            ("Gnome", "Gnome"),
            ("Halfling", "Halfling"),
            ("Half-Elf", "Half-Elf"),
            ("Half-Orc", "Half-Orc"),
            ("Human", "Human"),
            ("Tiefling", "Tiefling")
        ],
        validators=[DataRequired()])
    clazz = SelectField('Class', 
        choices=[
            ("Artificer", "Artificer"),
            ("Barbarian", "Barbarian"),
            ("Bard", "Bard"),
            ("Cleric", "Cleric"),
            ("Druid", "Druid"),
            ("Fighter", "Fighter"),
            ("Monk", "Monk"),
            ("Paladin", "Paladin"),
            ("Ranger", "Ranger"),
            ("Rogue", "Rogue"),
            ("Sorcerer", "Sorcerer"),
            ("Warlock", "Warlock"),
            ("Wizard", "Wizard")
        ],
        validators=[DataRequired()])
    submit = SubmitField('Submit')

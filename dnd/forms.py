from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from flask_wtf.file import DataRequired
from wtforms.validators import InputRequired, NumberRange
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
    cha = IntegerField('CHA Modifier', validators=[
        InputRequired(message="This field is required."),
        NumberRange(min=-5, max=30, message="Charisma modifier should be between -5 and 30.")
    ])
    submit = SubmitField('Submit')

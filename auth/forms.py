from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from flask_wtf.file import FileAllowed,FileRequired
from werkzeug.utils import secure_filename
import os



class LoginForm(FlaskForm):
    name = StringField('Name')
    password = PasswordField('Password')
    submit = SubmitField('Submit')

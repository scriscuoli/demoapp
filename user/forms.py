from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileAllowed,FileRequired
from werkzeug.utils import secure_filename
import os

class UpdatePasswordForm(FlaskForm):
    newPassword = PasswordField('NewPassword', validators=[Length(min=6)])
    newPasswordAgain = PasswordField('NewPasswordAgain', validators=[Length(min=6)])
    submit = SubmitField('Submit',render_kw={"disabled": "disabled"})
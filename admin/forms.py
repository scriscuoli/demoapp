from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileAllowed,FileRequired
from werkzeug.utils import secure_filename
import os

class UserEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[Length(min=6)]) # Password might be updated, so not always DataRequired
    submit = SubmitField('Update User')

class RenameUserForm(FlaskForm):
    newName = StringField('New Username', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Update User')

class DeleteUserForm(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')

class UserPasswordResetForm(FlaskForm):
    newPassword = PasswordField('NewPassword', validators=[Length(min=6)])
    newPasswordAgain = PasswordField('NewPasswordAgain', validators=[Length(min=6)])
    submit = SubmitField('Update Password',render_kw={"disabled": "disabled"})

class AddUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[Length(min=6)]) # Password might be updated, so not always DataRequired
    passwordAgain = PasswordField('Password Again', validators=[Length(min=6)]) # Password might be updated, so not always DataRequired
    submit = SubmitField('Add User',render_kw={"disabled": "disabled"})



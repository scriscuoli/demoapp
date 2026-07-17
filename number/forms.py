from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import DataRequired

class NumberForm(FlaskForm):

    submit = SubmitField('Submit')
    numberPicked = StringField('Pick', validators=[DataRequired()])

    def __init__(self, np, *args, **kwargs):
        super(NumberForm, self).__init__(*args, **kwargs)
        self.numberPicked.data = np
        
    
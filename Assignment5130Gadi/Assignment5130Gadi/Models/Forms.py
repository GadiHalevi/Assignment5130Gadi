from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField, IntegerField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

#Imports to make the forms possible.

class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name = "Expand"
    value = "Expand"

#converts the first 'submit' option to be 'Expand'.

class CollapseForm(FlaskForm):
	submit2 = SubmitField('Collapse')
	name="Collapse"
	value="Collapse"

#Converts the second 'submit' option to be 'Collapse'.

class GamesPoints(FlaskForm):
    points = IntegerField('Enter number of points:' , validators = [DataRequired] )
    submit = SubmitField('submit')

#Registers the user's input as 'Points' and creates a submit option.
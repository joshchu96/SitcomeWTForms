from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, RadioField, IntegerField

class AddChar(FlaskForm):
    """Form for adding new characters."""

    name = StringField("Name")
    age = FloatField("Age")
    state = StringField("State")

class AddJob(FlaskForm):
    job = StringField("What is the job? ")
    salary = IntegerField("What is the salary for the job?")
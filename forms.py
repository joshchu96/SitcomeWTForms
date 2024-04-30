from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,IntegerField,SelectField
from wtforms.validators import InputRequired, Optional

class AddChar(FlaskForm):
    """Form for adding new characters."""

    name = StringField("Name", 
                       validators = [InputRequired(message = "Name can not be blank")])
    age = FloatField("Age", validators = [InputRequired(message = "Error: Age input is required")])
    state = StringField("State", 
                        validators = [Optional()])
    

class AddJob(FlaskForm):
    job = StringField("What is the job? ")
    salary = IntegerField("What is the salary for the job?")


#creating dynamic fields in forms. 
#creating lists of choices in a field.
class practiceChoice(FlaskForm):
    jobs= SelectField("List of jobs") #SelectField("LABEL", choices = "[(tuple1, tuple2), ... ]") expect: list of tuples. tuple1=data, tuple2= UI seen.


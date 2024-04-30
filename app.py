from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Character, Job, Character_Job_Association
from forms import AddChar, AddJob, practiceChoice



app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debugger = DebugToolbarExtension(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Hill'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
app.app_context().push() #push everything from my models to the db?


@app.route("/char-lists")
def show_all_char():
    chars = Character.query.all() #[all the characters in a list]
    jobs = Job.query.all()
    return render_template("char-list.html", chars = chars, jobs = jobs)

@app.route("/char/add-form", methods =["GET","POST"])
def form_add_char():
    '''Creates a form to add a new character'''
    form = AddChar()
    
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

       #handle the possible default empty string error
        if (form.state.data != ""):
            state = form.state.data
            newChar = Character(name = name, age = age, state = state)
        
        newChar = Character(name = name , age = age)
        db.session.add(newChar)
        db.session.commit()
    
        return redirect("/char-lists")
    
    else:
        return render_template("form_newChar.html", form = form)

@app.route("/job/add-form", methods = ["GET","POST"])
def form_add_job():
    '''Shows & handles data for adding a job.'''

    form = AddJob()
    
    if form.validate_on_submit():
        job = form.job.data
        salary = form.salary.data
        newJob = Job(name = job, salary = salary)

        db.session.add(newJob)
        db.session.commit()
        return redirect("/char-lists") 
    
    else:
        return render_template("form_newJob.html", form = form)

@app.route("/char_jobs")
def show_char_job():
    '''Shows a table of characters and their job(s) at the moment''' 
    #grab every char in the query
    #char.jobs 

    chars = Character.query.all() #grab the list of all the characters made
    
    return render_template("char-jobs.html", chars =chars )
        

#practice route for selectfields
@app.route("/user/job-choice")
def job_choice():

    form = practiceChoice()

    jobs = db.session.query(Job.id,Job.name) #takes the list of jobs object and destructure each idv obj to get the id and name of job. 
    form.jobs.choices = [(job.name, job.name) for job in jobs] #TODO: why need to create another tuple list formatted for this to just show 1 var. 

    return render_template("choice.html", form = form)

@app.route("/user/<int:char_id>/edit", methods = ["GET","POST"])
def editChar(char_id):
    '''Edit the Char Profile Form'''

    char =  Character.query.get_or_404(char_id)
    form = AddChar(obj = char)

    if form.validate_on_submit():
        char.name = form.name.data
        char.age = form.age.data
        db.session.commit()
        return redirect("/char-lists")

    else:
        return render_template("edit_char_form.html", form = form )







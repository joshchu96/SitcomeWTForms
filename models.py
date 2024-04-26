from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Character_Job_Association(db.Model):
        __tablename__ = "character_job"

        id = db.Column(db.Integer, primary_key = True)
        character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
        job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
        


class Character(db.Model):
    __tablename__ = "characters"

    def __repr__(self):
        return f"< ID: {self.id} Name: {self.name} Age: {self.age} State: {self.state} Jobs: {self.jobs} >"

    id = db.Column(db.Integer, primary_key= True, autoincrement = True)
    name = db.Column(db.Text, unique = True, nullable = False)
    age = db.Column(db.Integer, nullable = True)
    state = db.Column(db.Text, nullable = False, default = "TX")
    jobs = db.relationship("Job", secondary = "character_job", backref = "characters")



class Job (db.Model):
    __tablename__ = "jobs"

    def __repr__(self):
        return f" < Job: {self.name} Salary: {self.salary} > "

    id = db.Column(db.Integer, primary_key= True, autoincrement = True)
    name = db.Column(db.Text, unique = True, nullable = False)
    salary = db.Column(db.Integer, nullable = True)

  
















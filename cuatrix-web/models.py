from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(80),unique = True)
    name = db.Column(db.String())
    position = db.Column(db.String(80))
    email = db.Column(db.String(80))
    starting_date = db.Column(db.String(80))
    ending_date = db.Column(db.String(80))

    def __init__(self, employee_id,name,position, email, starting_date, ending_date):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.email = email
        self.starting_date = starting_date
        self.ending_date = ending_date

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"

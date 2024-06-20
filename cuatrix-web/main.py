from flask import Flask, abort,render_template,request,redirect
from models import db,EmployeeModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

    
@app.before_request
def create_table():
    db.create_all() 

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        position = request.form['position']
        email = request.form['email']
        starting_date = request.form['starting_date']
        ending_date = request.form['ending_date']
        employee = EmployeeModel(employee_id=employee_id, name=name, email=email, position=position, starting_date=starting_date, ending_date=ending_date)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')
    
@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/data/<string:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"

@app.route('/data/<string:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()

            name = request.form['name']
            position = request.form['position']
            email = request.form['email']
            starting_date = request.form['starting_date']
            ending_date = request.form['ending_date']
            employee = EmployeeModel(employee_id=id, name=name, position=position, email=email, starting_date=starting_date, ending_date=ending_date)
        
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"

    return render_template('update.html', employee = employee)

@app.route('/data/<string:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        abort(404)

    return render_template('delete.html')

@app.route('/time_tracking/data')
def RetrieveTimesheet():
    employees = EmployeeModel.query.all()
    return render_template('time_tracking/datalist.html',employees = employees)

@app.route('/time_tracking/data/<string:id>')
def RetrieveSingleTimesheet(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('time_tracking/data.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"

if __name__ == '__main__':
    app.debug = True
    app.run()
app.run(host='localhost', port=5000)
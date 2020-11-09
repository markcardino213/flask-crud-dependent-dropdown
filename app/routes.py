from flask import render_template, redirect, request, url_for, flash
from app import app
import app.database as database

@app.route('/')
def index():
	data = database.Database.all()
	return render_template('index.html', students = data)

@app.route('/course_page/')
def course_page():
	data4 = database.Database.course_page()
	return render_template('page.html',page = data4)

@app.route('/course_list/')
def course_list():
	data4 = database.Database.course_page()
	return render_template('course.html',page = data4)	

@app.route('/add/', methods = ['GET','POST'])
def add():
	if request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		idno = request.form['idno']
		yrlvl = request.form['yrlvl']
		gender = request.form['gender']
		college = request.form['college']
		dept = request.form['dept']
		course = request.form['course']
		data = database.Database(first_name = first_name, last_name = last_name, idno = idno, yrlvl = yrlvl, gender = gender, college = college, dept = dept, course = course)
		data.add()
		flash("new information added!")
		return redirect(url_for('index'))
	else:
		data = database.Database.all()
		data1 = database.Database.college_dropdown()
		data2 = database.Database.dept_dropdown()
		data3 = database.Database.course_dropdown()
		return render_template('add.html',students = data, college = data1, department = data2, course = data3)
	


@app.route('/update/<int:id_data>/')
def update(id_data):
	data = database.Database.get_data(id_data)
	data1 = database.Database.college_dropdown()
	data2 = database.Database.dept_dropdown()
	data3 = database.Database.course_dropdown()
	return render_template('update.html', students = data,  college = data1, department = data2, course = data3)


@app.route('/update_info/<int:id_data>/', methods=['POST'])
def update_info(id_data):
    if request.method == 'POST':
    	first_name = request.form['first_name']
    	last_name = request.form['last_name']
    	idno = request.form['idno']
    	yrlvl = request.form['yrlvl']
    	gender = request.form['gender']
    	college = request.form['college']
    	dept = request.form['dept']
    	course = request.form['course']
    	data = database.Database(first_name = first_name, last_name = last_name, idno = idno, yrlvl = yrlvl, gender = gender, college = college, dept = dept, course = course, id_data = id_data)
    	data.update_info(id_data)
    	flash('Record Updated Successfully')
    	return redirect(url_for('index'))


@app.route('/delete_info/<int:id_data>/')
def delete_info(id_data):
	data = database.Database(id_data = id_data)
	data.delete_info(id_data)
	flash("Record has been deleted successfully")
	return redirect(url_for('index'))


 
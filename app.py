from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os

# Adapted from the OSU CS340 Flask Starter App https://github.com/osu-cs340-ecampus/flask-starter-app

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_koshyn'
app.config['MYSQL_PASSWORD'] = '2356' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_koshyn'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes
@app.route('/')
def root():
    return render_template("index.j2")

@app.route('/index.html')
def index():
    return render_template("index.j2")

# Departments 
@app.route('/departments', methods = ["POST", "GET"])
def departments():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM departments;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("departments.j2", data=data)
    # Department Insert
    if request.method =="POST":
        if request.form.get("Add_Department"):
            department_name=request.form["department_name"]
            location=request.form["location"]
            query = "INSERT INTO departments (department_name, location) VALUES (%s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (department_name, location))
            mysql.connection.commit()

        return redirect("/departments")

# Department Delete
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_department/<int:department_id>")
def delete_department(department_id):
    # mySQL query to delete with our passed id
    query = "DELETE FROM departments WHERE department_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (department_id,))
    mysql.connection.commit()

    # redirect back to departments page
    return redirect("/departments")

# Department Edit
@app.route("/edit_department/<int:department_id>", methods=["POST", "GET"])
def edit_department(department_id):
    if request.method == "GET":
        query = "SELECT * FROM departments WHERE department_id = %s" % (department_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_department.j2", data=data)

    if request.method == "POST":
        if request.form.get("Edit_Department"):
            department_name=request.form["department_name"]
            location=request.form["location"]

        query = "UPDATE departments SET departments.department_name = %s, departments.location = %s WHERE departments.department_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (department_name, location, department_id))
        mysql.connection.commit()

        return redirect("/departments")

# Employees 
@app.route('/employees', methods = ["POST", "GET"])
def employees():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM employees;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("employees.j2", data=data)
    # Employee Insert
    if request.method =="POST":
        if request.form.get("Add_Employee"):
            first_name =request.form["first_name"]
            last_name =request.form["last_name"]
            query = "INSERT INTO employees (first_name, last_name) VALUES (%s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name))
            mysql.connection.commit()

        return redirect("/employees")

# Employee Delete
@app.route("/delete_employee/<int:employee_id>")
def delete_employee(employee_id):
    # mySQL query to delete with our passed id
    query = "DELETE FROM employees WHERE employee_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (employee_id,))
    mysql.connection.commit()

    # redirect back to departments page
    return redirect("/employees")

# Employee Edit
@app.route("/edit_employee/<int:employee_id>", methods=["POST", "GET"])
def edit_employee(employee_id):
    if request.method == "GET":
        query = "SELECT * FROM employees WHERE employee_id = %s" % (employee_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_employee.j2", data=data)

    if request.method == "POST":
        if request.form.get("Edit_Employee"):
            first_name=request.form["first_name"]
            last_name=request.form["last_name"]

        query = "UPDATE employees SET employees.first_name = %s, employees.last_name = %s WHERE employees.employee_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (first_name, last_name, employee_id))
        mysql.connection.commit()

        return redirect("/employees")

# Items 
@app.route('/items', methods = ["POST", "GET"])
def items():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM items;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("items.j2", data=data)
    # Items Insert
    if request.method =="POST":
        if request.form.get("Add_Item"):
            name=request.form["name"]
            price=request.form["price"]
            clearance=request.form["clearance"]
            brand=request.form["brand"]
            departments_department_id=request.form["departments_department_id"]

            query = "INSERT INTO items (name, price, clearance, brand, departments_department_id) VALUES (%s,%s,%s,%s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, price, clearance, brand, departments_department_id))
            mysql.connection.commit()

        return redirect("/items")
    
# Item Delete
@app.route("/delete_item/<int:item_id>")
def delete_item(item_id):
    # mySQL query to delete with our passed id
    query = "DELETE FROM items WHERE item_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (item_id,))
    mysql.connection.commit()

    # redirect back to departments page
    return redirect("/items")

# Item Edit
@app.route("/edit_item/<int:item_id>", methods=["POST", "GET"])
def edit_item(item_id):
    if request.method == "GET":
        query = "SELECT * FROM items WHERE item_id = %s" % (item_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_item.j2", data=data)

    if request.method == "POST":
        if request.form.get("Edit_Item"):
            name=request.form["name"]
            price=request.form["price"]
            clearance=request.form["clearance"]
            brand=request.form["brand"]
            departments_department_id=request.form["departments_department_id"]

        query = "UPDATE items SET items.name = %s, items.price = %s, items.clearance = %s, items.brand = %s, items.departments_department_id = %s  WHERE items.item_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (name, price, clearance, brand, departments_department_id, item_id))
        mysql.connection.commit()

        return redirect("/items")

# Sales 
@app.route('/sales', methods = ["POST", "GET"])
def sales():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM sales;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        # FIX
        return render_template("departments.j2", data=data)
    # TODO Sale Insert #
    if request.method =="POST":
        if request.form.get("Add_Sales"):
            sale_date=request.form["name"]
            query = "INSERT INTO sales (sale_date) VALUES (%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (sale_date))
            mysql.connection.commit()

        return redirect("/sales")

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=19956, debug=True)


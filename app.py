# All work below was performed by Christelle Nieves

import os

from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
import setup
import Encryption

app = Flask(__name__)
app.secret_key = os.urandom(12)


# If a user is not logged in, redirect them to the login page, otherwise redirect them to the home page.
@app.route('/')
@app.route('/home')
def home():
    if not session.get("logged_in"):
        return render_template('login.html')
    else:
        # Redirect to the home page and pass in the name and security level of the user
        return render_template('home.html', name=session['fname'], level=session['level'])


# Completes the log in process for a user. Checks for correct username/password combination in the Employee table.
@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        try:
            # Store the username and password
            username = request.form['username']
            password = bytes(request.form['password'], encoding='utf-8')

            # Encrypt the password
            encrypted_pwd = str(Encryption.cipher.encrypt(password).decode('utf-8'))

            # Connect to the database
            with sqlite3.connect('data.db') as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()

                # Run a query to find the username and password in the Employee table
                query = '''SELECT * FROM Employee WHERE UserName = ? AND LoginPassword = ?'''
                cur.execute(query, (username, encrypted_pwd))

                row = cur.fetchone()

                # If username/password were found in the table, login as the user and redirect to the home page
                if row is not None:
                    session["name"] = username
                    session["logged_in"] = True

                    # Get the security level of the user
                    query = '''SELECT SecurityLevel FROM Employee WHERE UserName = ? AND LoginPassword = ?'''
                    cur.execute(query, (username, encrypted_pwd))

                    # Set the security level as a session variable "level"
                    level = cur.fetchone()[0]
                    session["level"] = level

                    # Get the first name of the user
                    query = '''SELECT FirstName FROM Employee WHERE UserName = ? AND LoginPassword = ?'''
                    cur.execute(query, (username, encrypted_pwd))

                    # Set the first name as a session variable
                    first_name = cur.fetchone()[0]
                    session['fname'] = first_name

                    return redirect(url_for("home"))
                else:
                    # If username/password were not found, display incorrect username/password message
                    msg = "Invalid username and/or password"
                    session["logged_in"] = False
                    flash("Incorrect username and/or password")

        except:
            # If there was a problem inserting the information display the error to the screen
            con.rollback()
            flash("Error in SQL Operation")

        finally:
            # Close the connection to the database
            con.close()

        # Return the home function that will determine if the user is logged in or not
        return home()


# Completes the log out process for a user and returns them to the login page.
@app.route('/log_out')
def log_out():
    # Reset all the session fields
    session['name'] = ""
    session['logged_in'] = False
    session['level'] = ""
    flash("Successfully logged out")
    return home()


# Renders the Add New Employee screen to the user
@app.route('/addnew')
def add_new():
    # If the user is not logged in, redirect them to the login screen
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # If the user is not security level 1 redirect them to the home screen
        if not session.get('level') == 1:
            return home()
        else:
            return render_template('addnew.html')


@app.route('/remove')
def remove():
    if not session.get('logged_in') or session.get('level') != 1:
        return home()
    else:
        if not session.get('level') == 1:
            return home()
        else:
            return render_template('remove.html')


@app.route('/remove_employee', methods=['POST', 'GET'])
def remove_employee():
    if request.method == 'POST':
        con = sqlite3.connect('data.db')

        try:
            firstname = request.form['fname']
            lastname = request.form['lname']
            eid = request.form['eid']

            con.row_factory = sqlite3.Row
            cur = con.cursor()

            query = '''DELETE FROM Employee WHERE FirstName = ? AND LastName = ? AND EmployeeId = ?'''
            cur.execute(query, (firstname, lastname, eid))
            con.commit()

            flash("Employee removed")

        except:
            con.rollback()
            flash("Employee not found in database")

        finally:
            con.close()

            return render_template('results.html')


# Gets field values for the entry of a new employee and completes the sql query to insert it into the Employee table.
@app.route('/enter_new', methods=['POST', 'GET'])
def enter_new():
    if request.method == 'POST':
        con = sqlite3.connect('data.db')

        try:
            # Get all the info from the form and store them in variables
            username = request.form['username']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            level = request.form['level']
            password = request.form['pass']

            valid = True

            # Check for valid inputs
            if not username:
                flash("Username field cannot be empty.")
                valid = False

            if not firstname:
                flash("First name field cannot be empty.")
                valid = False

            if not lastname:
                flash("Last name field cannot be empty.")
                valid = False

            if username.isspace():
                flash("Username field cannot contain only spaces.")
                valid = False

            if firstname.isspace():
                flash("First name field cannot contain only spaces.")
                valid = False

            if lastname.isspace():
                flash("Last name field cannot contain only spaces.")
                valid = False

            if int(level) < 1 or int(level) > 10:
                flash("Security level must be a number between 1 and 10 inclusive.")
                valid = False

            # Encrypt the password
            encrypted_pwd = str(Encryption.cipher.encrypt(bytes(password, encoding='utf-8')).decode('utf-8'))

            # Connect to the database
            cur = con.cursor()

            # If the inputs are all valid, insert them into the Employee table in the database
            if valid:
                cur.execute("INSERT INTO Employee(UserName, FirstName, LastName, SecurityLevel, LoginPassword) "
                            "VALUES (?,?,?,?,?)",
                            (username, firstname, lastname, level, encrypted_pwd))

                con.commit()

                flash("Record added")
        except:
            # If there was an error display it to the screen
            con.rollback()
            flash("Error in insert operation")
        finally:
            # Close the connection to the database and return results.html
            con.close()
            return render_template('results.html')


# Retrieves all entries in the Employee table and returns them to list.html to be displayed on screen.
@app.route('/list')
def list_employees():
    # If the user is not logged in redirect them to the login screen
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # If the user is not security level 1 or 2 redirect them to the home screen
        if not session.get('level') == 1 and not session.get('level') == 2:
            return home()
        else:
            # If the user is logged in and has the correct security level get all Employees and pass them into list.html
            con = sqlite3.connect("data.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM Employee")

            rows = cur.fetchall()
            return render_template("list.html", rows=rows)


# Displays list.html which shows the results of an "Add new employee" operation.
@app.route('/results')
def results():
    # If the user is not logged in redirect them to the login screen
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # If the user is logged in take them to the results screen
        return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)

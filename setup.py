# This script contains the setup for the database. It sets up a table "Employee" and performs some insertions on it.
# All work below was performed by Christelle Nieves

import sqlite3
import Encryption


# This method takes in employee data, encrypts the password, and then inserts the data into the Employee table
def encrypt_and_insert_employee(cursor, conn, emp_username, emp_fname, emp_lname, emp_level, emp_password):

    # Convert the strings into bytes
    pwd = bytes(emp_password, encoding='utf-8')

    # Perform encryption of the password
    encrypted_pwd = str(Encryption.cipher.encrypt(pwd).decode('utf-8'))

    # Insert Agent data into the Agent table
    cursor.execute('''INSERT INTO Employee (Username, FirstName, LastName, SecurityLevel, LoginPassword)
        VALUES (?,?,?,?,?)''', (emp_username, emp_fname, emp_lname, emp_level, encrypted_pwd))

    # Commit the changes to the database
    conn.commit()


# Connect to the database
con = sqlite3.connect('data.db')

# Get a cursor to the database
cur = con.cursor()

# Drop tables if they exist
cur.execute('DROP TABLE IF EXISTS Employee')

con.commit()

# Create the Employee table
cur.execute('''CREATE TABLE Employee (
    EmployeeId INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    SecurityLevel INTEGER NOT NULL,
    LoginPassword TEXT NOT NULL
    )
    ''')

con.commit()

# Insert some data into the Employee table
encrypt_and_insert_employee(cur, con, 'cjn123', 'Christelle', 'Nieves', 1, 'password')
encrypt_and_insert_employee(cur, con, 'rickyjr92', 'Ricky', 'Inczedy', 2, 'pwd123')
encrypt_and_insert_employee(cur, con, 'JohnDoe', 'John', 'Doe', 1, 'pass456')
encrypt_and_insert_employee(cur, con, 'JaneDoe', 'Jane', 'Doe', 3, 'test7')
encrypt_and_insert_employee(cur, con, 'Test', 'Test User', 'Tester', 1, 'password')

con.commit()

# Close the database connection
con.close()

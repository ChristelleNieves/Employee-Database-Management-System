# This script contains the setup for the database. It sets up a table "Employee" and performs some insertions on it.
# All work below was performed by Christelle Nieves

import sqlite3

# Connect to the database
con = sqlite3.connect('data.db')

# Get a cursor to the database
cur = con.cursor()

# Drop tables if they exist
cur.execute('DROP TABLE IF EXISTS Employee')

con.commit()

# Create the Agent table
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
cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('Cjn', 'Christelle', 'Nieves', 1, 'password')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('RickyI', 'Ricky', 'Inczedy', 1, 'hello123')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('JohnDoe', 'John', 'Doe', 2, 'pass1')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('JaneDoe', 'Jane', 'Doe', 2, 'pass2')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('NickWild', 'Nicholas', 'Wild', 2, '12345')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('PeterQuill', 'Peter', 'Quill', 2, 'mypassword1')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('ReginaGeorge', 'Regina', 'George', 3, 'pass123')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('ThomasW', 'Thomas', 'Winston', 2, 'p7658')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('SimonC', 'Simon', 'Clark', 3, 'password908')''')

con.commit()

cur.execute('''INSERT INTO Employee (UserName, FirstName, LastName, SecurityLevel, LoginPassword)
    VALUES('Test', 'Test User', 'Test', 1, 'password')''')

con.commit()

# Close the database connection
con.close()

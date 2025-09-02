# connecting to sql lite 3
import sqlite3

# create a connection to the database
conn = sqlite3.connect('school.db')

# create a cursor object to execute SQL commands

cur = conn.cursor()

# create a table for students
cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
);
''')

conn.commit() # saves the changes
# Always use IF NOT EXISTS to avoid table duplication when rerunning the script
# insert a student record
cur.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", ('Prince', 20, 'A'))
# we use placeholders for values to prevent SQL injection attacks (hacking)
conn.commit()

# fetch all records from the table
cur.execute("SELECT * FROM students")
students = cur.fetchall()

# print the records
for student in students:
    print(student)
# 02insertingmultipledata.py in sqlite3
import sqlite3

# create a connection to the database
conn = sqlite3.connect('school.db')

# create a cursor object to execute SQL commands
cur = conn.cursor()

cur.execute('''
    drop TABLE IF EXISTS students1;

''')
conn.commit() # saves the changes


# create a table for students
cur.execute('''
CREATE TABLE IF NOT EXISTS students1 (
    id INTEGER primary KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
);
''')

conn.commit() # saves the changes

# insert multiple student records using a list of tuples
students = [('Prince', 20, 'A'), ('John', 18, 'B'), ('Alice', 22, 'C')]
cur.executemany("INSERT INTO students1 (name, age, grade) VALUES (?,?,?)", students)

conn.commit() # saves the changes

cur.execute('''UPDATE students1 
            SET age=? 
            WHERE name=? ''',
            (21,"Prince"))
conn.commit() # saves the changes

cur.execute("DELETE FROM students1 WHERE name=?",("Alice",))
conn.commit() # saves the changes

# fetch all records from the table
cur.execute("SELECT * FROM students1")
students = cur.fetchall()

# print the records
for student in students:
    print(student)

conn.close() # close the connection to the database

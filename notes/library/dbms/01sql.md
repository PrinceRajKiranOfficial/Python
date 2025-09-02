<!-- database_connectivity_sqlite3.md -->

# DATABASE CONNECTIVITY IN PYTHON WITH SQLITE3

## Why Use SQLite?
- **Lightweight** → File-based database (no separate server required)  
- **Built-in** → Available in Python through the `sqlite3` module  
- **Portable** → Database stored in a single file  
- **Best For** → Small to medium-scale applications  

## Key Features
- Simple integration with Python  
- SQL support for queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)  
- Good for prototyping, desktop apps, and small web projects  

## Basic Workflow
1. **Import sqlite3 module**  
2. **Connect to a database** (creates one if it doesn’t exist)  
3. **Create a cursor** object to execute SQL queries  
4. **Execute queries** (`CREATE TABLE`, `INSERT`, `SELECT`, etc.)  
5. **Commit changes** (for `INSERT`, `UPDATE`, `DELETE`)  
6. **Close connection**  

## Example Code
```python
import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect("students.db")

# Create a cursor
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER
)
""")

# Insert data
cur.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Alice", 85))
cur.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Bob", 90))

# Commit changes
conn.commit()

# Fetch data
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()

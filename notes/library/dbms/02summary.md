<!-- sqlite3_crud_summary.md -->

# SUMMARY TABLE: CRUD WITH SQLITE3

| **Operation** | **Python Function**         | **SQL Command**   | **Example** |
|---------------|-----------------------------|-------------------|-------------|
| **Create**    | `cursor.execute(...)`<br>`executemany(...)` | `INSERT INTO` | `cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Alice", 85))` |
| **Read**      | `cursor.execute("SELECT ...")`<br>`fetchall()` / `fetchone()` | `SELECT` | `cursor.execute("SELECT * FROM students")`<br>`rows = cursor.fetchall()` |
| **Update**    | `cursor.execute("UPDATE ...")` | `UPDATE ... SET` | `cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Alice'")` |
| **Delete**    | `cursor.execute("DELETE FROM ...")` | `DELETE FROM` | `cursor.execute("DELETE FROM students WHERE name = 'Bob'")` |

---

## Notes
- Always call **`conn.commit()`** after `INSERT`, `UPDATE`, or `DELETE` to save changes.  
- Use **parameterized queries (`?`)** to avoid SQL injection.  
- Close connection with **`conn.close()`** after operations.  

<!-- sqlite3_crud_summary.md -->

# SUMMARY TABLE: CRUD WITH SQLITE3

| **Operation** | **Python Function**         | **SQL Command**   | **Example** |
|---------------|-----------------------------|-------------------|-------------|
| **Create**    | `cursor.execute(...)`<br>`executemany(...)` | `INSERT INTO` | `cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Alice", 85))` |
| **Read**      | `cursor.execute("SELECT ...")`<br>`fetchall()` / `fetchone()` | `SELECT` | `cursor.execute("SELECT * FROM students")`<br>`rows = cursor.fetchall()` |
| **Update**    | `cursor.execute("UPDATE ...")` | `UPDATE ... SET` | `cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Alice'")` |
| **Delete**    | `cursor.execute("DELETE FROM ...")` | `DELETE FROM` | `cursor.execute("DELETE FROM students WHERE name = 'Bob'")` |

---

## Notes
- Always call **`conn.commit()`** after `INSERT`, `UPDATE`, or `DELETE` to save changes.  
- Use **parameterized queries (`?`)** to avoid SQL injection.  
- Close connection with **`conn.close()`** after operations.  


import sqlite3

connection = sqlite3.connect('students.db')
# Creates a cursor
c = connection.cursor()

# c.execute("""CREATE TABLE students (
#         first_name text,
#         last_name text,
#         age int
#         )""")


# deleting records
# c.execute("DELETE from students WHERE rowid = 10")
# connection.commit()

c.execute("SELECT rowid, * FROM students LIMIT 5")

# c.execute("""UPDATE students SET first_name = 'fallon' WHERE rowid = 2""")
# connection.commit()
# c.execute("INSERT INTO students VALUES('Mary','Smith','22')")
# c.execute("SELECT rowid, * FROM students")
# c.execute("SELECT * FROM students WHERE last_name LIKE 'ha%'")
items = c.fetchall()
for item in items:
    print(item)

# for item in items:
#     print(item[0] + " " + item[1])
# student_list = [('jacob','hold','17'),('fallon','hased','17'),('jab','said','17')]
print("Successful insert")

# c.executemany("INSERT INTO students VALUES (?,?,?)", student_list)
connection.commit()
connection.close()
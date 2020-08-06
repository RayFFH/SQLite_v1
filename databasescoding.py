import sqlite3

# connection = sqlite3.connect('students.db')
# c = connection.cursor()

# c.execute("""CREATE TABLE students (
#         first_name text,
#         last_name text,
#         age text

# )""")
# connection.commit()
# connection.close()

def show_record():
    connection = sqlite3.connect('students.db')

    c = connection.cursor()

    c.execute("SELECT rowid, * FROM students LIMIT 5")
    records = c.fetchall()
    for record in records:
        print(record)

    connection.commit()
    connection.close()


def add(first, last, age):
    connection = sqlite3.connect('students.db')
    c = connection.cursor()
    c.execute("INSERT INTO students VALUES (?,?,?)", (first, last, age))
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect('students.db')
    c = connection.cursor()
    c.execute("DELETE from students WHERE rowid = (?)", id)
    connection.commit()
    connection.close()

def name_finder(first):
    connection = sqlite3.connect('students.db')
    c = connection.cursor()
    c.execute("SELECT * from students WHERE first = (?)", (first,))
    records = c.fetchall()
    for record in records:
        print(record)

    connection.commit()
    connection.close()

def drop():
    connection = sqlite3.connect('students.db')
    c = connection.cursor()
    c.execute("DROP TABLE students")
    print("Table dropped.")
    connection.commit()
    connection.close()
# Develop a database application to Create a table named „student‟ to store the student information like usn,name,semester,department and number of clubs. Further insert the number of rows to the same table.

import sqlite3 as sql

tab = sql.connect('database.db')
cur = tab.cursor()
cur.execute(
    'CREATE TABLE student(usn TEXT PRIMARY KEY NOT NULL,name TEXT,sem INTEGER,dept TEXT,noc INTEGER)'
)

usn = '1MS20EC100'
name = 'Flappy Bird'
sem = 5
dept = 'ECE'
noc = 2
cur.execute('INSERT INTO student VALUES(?,?,?,?,?)',
            (usn, name, sem, dept, noc))
usn = '1MS20IS048'
name = 'Snoop Dogg'
sem = 5
dept = 'ISE'
noc = 0
cur.execute('INSERT INTO student VALUES(?,?,?,?,?)',
            (usn, name, sem, dept, noc))
usn = '1MS19ME084'
name = 'Joe Ligma'
sem = 7
dept = 'ME'
noc = 1
cur.execute('INSERT INTO student VALUES(?,?,?,?,?)',
            (usn, name, sem, dept, noc))
usn = '1MS21EC034'
name = 'Fried Momos'
sem = 3
dept = 'ECE'
noc = 2
cur.execute('INSERT INTO student VALUES(?,?,?,?,?)',
            (usn, name, sem, dept, noc))

cur.execute('SELECT * FROM student')
print(cur.fetchall())

cur.execute('DROP TABLE student')

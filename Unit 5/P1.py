# In this exercise, you will create a table to store the population and land area of the Canadian provinces and territories according to the 2001 census.
# Write Python code that does the following:
# a. Creates a new database called census.db
# b. Makes a database table called Density that will hold the name of the
# province or territory (TEXT), the population (INTEGER), and the land area
# (REAL)
# c. Inserts the data from Table 32, 2001 Canadian Census Data, on page
# 361
# d. Retrieves the con tents of the table
# e. Retrieves the populations
# f. Retrieves the provinces that have populations of less than one million
# g. Retrieves the provinces that have populations of less than one million or greater than five million
# h. Retrieves the provinces that do not have populations of less than one million or greater than five million
# i. Retrieves the populations of provinces that have a land area greater than 200,000 square kilometers
# j. Retrieves the provinces along with their population densities (population divided by land area)

import sqlite3 as sql


def printRows(Data):
    for row in Data:
        print(row)
    print("\n")


data = [
    ("Newfoundland and Labrador", 512930, 370501.69),
    ("Prince Edward Island", 125294, 5684.39),
    ("Nova Scotia", 908007, 52917.43),
    ("New Brunswick", 729498, 71355.67),
    ("Quebec", 7237479, 1257743.08),
    ("Ontario", 11410046, 907655.59),
    ("Manitoba", 1119583, 551937.87),
    ("Saskatchewan", 978933, 586561.35),
    ("Alberta", 2974807, 639987.12),
    ("British Columbia", 3907738, 926492.48),
    ("Yukon Territory", 28674, 474706.97),
    ("Northwest Territories", 37360, 1141108.37),
    ("Nanavut", 26745, 1925460.18),
]

# Create Database and Table
database = sql.connect("Unit 5/census.db")
cur = database.cursor()
cur.execute("CREATE TABLE Density(Region TEXT, Population INTEGER, Area REAL)")

# Insert Values into Table
for i in data:
    cur.execute("INSERT INTO Density VALUES (?, ?, ?)", (i))
database.commit()

# Retrieve Data
cur.execute("SELECT * FROM Density")
print("Data")
printRows(cur.fetchall())

# Retrieve Population
cur.execute("SELECT Population FROM Density")
print("Population")
printRows(cur.fetchall())

# Retrieve Region where Population less than 1,000,000
cur.execute("SELECT Region FROM Density WHERE Population < 1000000")
print("Population < 1000000")
printRows(cur.fetchall())

# Retrieve Region where Population less than 1,000,000 or greater than 5,000,000
cur.execute(
    "SELECT Region FROM Density WHERE Population < 1000000 OR Population > 5000000"
)
print("Population < 1000000 OR Population > 5000000")
printRows(cur.fetchall())

# Retrieve Population where Area less than 200,000
cur.execute("SELECT Population FROM Density WHERE Area > 200000")
print("Area > 200,000")
printRows(cur.fetchall())

# Retrieve Region and Population Density
cur.execute("SELECT Region, Population / Area FROM Density")
print("Country and Population Density")
printRows(cur.fetchall())

# For this exercise, add a new table called Capitals to the database. Capitals has three columns - province/territory (TEXT), capital (TEXT), and population (INTEGER)- and it holds the data shown here:
# Province/Territory Capital Population
# Newfoundland and Labrador St. John's 172918
# Prince Edward Is land Charlottetown 58358
# Nova Scotia Halifax 359183
# New Brunswick Fredericton 8 1346
# Quebec Quebec City 682757
# Ontario Toronto 4682897
# Manitoba Winnipeg 671274
# Saskatchewan Regina 192800
# Alberta Edmonton 937845
# British Columbia Victoria 31 1902
# Yukon Territory Whitehorse 2 1405
# Northwest Territories Yellowknife 16541
# Nunavut Iqaluit 5236
#
# Write SQL queries that do the following:
# a. Retrieve the contents of the table
# b. Retrieve the populations of the provinces and capitals (in a list of tuples of the form [province population, capital population])
# c. Retrieve the land area of the provinces whose capitals have populations greater than 100,000
# d. Retrieve the provinces with land densities less than two people per square kilometer and capital city populations more than 500,000
# e. Retrieve the total land area of Canada
# f. Retrieve the average capital city population
# g. Retrieve the lowest capital city population
# h. Retrieve the highest province/territory population
# i. Retrieve the provinces that have land densities within 0.5 persons per square kilometer of on another- have each pair of provinces reported only once

import sqlite3 as sql


def printRows(Data):
    for row in Data:
        print(row)
    print("\n")


data = [
    ("Newfoundland and Labrador", "St. John's", 172918),
    ("Prince Edward Island", "Charlottetown", 58358),
    ("Nova Scotia", "Halifax", 359183),
    ("New Brunswick", "Fredericton", 81346),
    ("Quebec", "Quebec City", 682757),
    ("Ontario", "Toronto", 4682897),
    ("Manitoba", "Winnipeg", 671274),
    ("Saskatchewan", "Regina", 192800),
    ("Alberta", "Edmonton", 937845),
    ("British Columbia", "Victoria", 311902),
    ("Yukon Territory", "Whitehorse", 21405),
    ("Northwest Territories", "Yellowknife", 16541),
    ("Nunavut", "Iqaluit", 5236),
]

# Create Database and Table
database = sql.connect("Unit 5/census.db")
cur = database.cursor()
cur.execute("CREATE TABLE Capitals(Province TEXT, Capital TEXT, Population INTEGER)")

# Insert Values
for i in data:
    cur.execute("INSERT INTO Capitals VALUES (?, ?, ?)", (i))
database.commit()

# Retrieve Data
cur.execute("SELECT * FROM Capitals")
print("Data")
printRows(cur.fetchall())

# Populations and Capitals
cur.execute(
    "SELECT Capitals.Population, Density.Population FROM Capitals INNER JOIN Density WHERE Capitals.Province = Density.Region"
)
print("Population of Capitals and Province")
printRows(tuple(cur.fetchall()))

# Land Area whose Capitals have population greater than 100,000
cur.execute(
    "SELECT Density.Area FROM Density INNER JOIN Capitals WHERE Capitals.Population > 100000 AND Capitals.Province = Density.Region"
)
print("Land Area whose Capital Population greater than 100,000")
printRows(cur.fetchall())

# Provinces whose population density less than 2 and capital population greater than 500,000
cur.execute(
    "SELECT Density.Region FROM Density INNER JOIN Capitals WHERE Density.Population / Density.Area < 2 AND Capitals.Population > 500000"
)
print("Provinces whose population density less than 2")
printRows(cur.fetchall())

# Total Land Area of Canada
cur.execute("SELECT SUM(Area) FROM Density")
print("Total Land Area of Canada")
printRows(cur.fetchall())

# Average Capital City Population
cur.execute("SELECT AVG(Population) FROM Capitals")
print("Average capital city population")
printRows(cur.fetchall())

# Lowest capital city Population
cur.execute("SELECT Capital, MIN(Population) FROM Capitals")
print("Lowest capital city population")
printRows(cur.fetchall())

# Highest Province Population
cur.execute("SELECT Province, MAX(Population) FROM Capitals")
print("Highest capital city population")
printRows(cur.fetchall())

# Pairs of Provinces with Population Density Difference is less than 0.5
cur.execute(
    "SELECT DISTINCT A.Region, B.Region FROM Density A INNER JOIN Density B WHERE A.Region != B.Region AND A.Region < B.Region AND ABS(A.Population / A.Area - B.Population / B.Area) < 0.5"
)
print("Population difference less than 0.5")
printRows(cur.fetchall())

import sqlite3

# Create database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("create table observations ('species_key' varchar, 'date' varchar, 'nr_of_individuals' int)")

# Add some data
cursor.execute("insert into observations values('1', '2014-09-19', 6)")
cursor.execute("insert into observations values('2', '2014-09-19', 1)")
cursor.execute("insert into observations values('1', '2014-09-20', 2)")

# Fetch rows
cursor.execute("select * from observations")
rows = cursor.fetchall()
for row in rows:
    print row
connection.close()
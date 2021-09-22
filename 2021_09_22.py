import sqlite3

# We need a connection to our database
# conn = sqlite3.connect(':memory:') If you want to do some stuff and then it will dissappear

conn = sqlite3.connect('customer.db')

# First we need to create cursor (Tells the database what you wanna do) we can build it once and use it

c = conn.cursor()

# Create a Table (Has all the data inside)
# Use Dock String for multiple line work.

# c.execute("""CREATE TABLE customers (
# 		first_name text,
# 		last_name text,
# 		email text
# 	)""")

#DATA TYPES:
#NULL    (Doesn't exist if exists called not-null)
#INTEGER
#REAL    (Decimal)
#TEXT
#BLOB    (Extored exactly how it is (example: Image))

# many_customers = [	('Wes', 'King', 'wes@king.com'), 
# 					('Tim', 'Black', 'tim@black.com'),
# 					('Adriana', 'Grande', 'grande@gmail.com'),
# 					('Simon', 'Cowel', 'simon7@yahoo.com'),
# 				]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


# Query The Database
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Gr%' ")
# print(c.fetchone()[0])
# c.fetchmany(3)

# Update Records

c.execute("""UPDATE customers SET first_name = 'John'
			Where last_name = "King"



	""")
conn.commit()

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	# print(item[0] + " " + item[1] + "		" + item[2])
	print(item)



# print("Command executed successfully...")if you would like.






# Commit our command
conn.commit()

# Close our connection
conn.close()





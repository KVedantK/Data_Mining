import mysql.connector

Db = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                passwd = '',
                database = 'testdatabase'
            )

cursor = Db.cursor()
cursor.execute("SELECT * FROM details")
rows = cursor.fetchall()
print(rows)
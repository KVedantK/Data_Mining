# Importing Mysql Connector Use pip install mysql-connector if no module found
import mysql.connector   


# returns a connector object 
# pass host, user, password, database name
def ConnectDB(self,h=None,u=None,p=None,d=None):
    if d != None:
        Db = mysql.connector.connect(
            host = h,
            user = u,
            passwd = p,
            database = d
            )
        return Db
    else:
        Db = mysql.connector.connect(
            host = h,
            user = u,
            passwd = p
        )
        return Db

# class containing some usual queries.
# pass Database object(u can use the previous function to create one), Table name to retreieve all rows from.
def RetreieveRows(self, Db, TableName):
    cursor = Db.cursor()
    cursor.execute("SELECT * FROM {}".foramt(TableName))
    Row = cursor.fetchall()
        


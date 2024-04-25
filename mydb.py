import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    auth_plugin='mysql_native_password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE prod_db")

print('All done')

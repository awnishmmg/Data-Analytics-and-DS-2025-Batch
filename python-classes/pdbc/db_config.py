# ctrl+shift+p 
# select Interpreter : select your myenv python.exe 
# package -> subpackage 
# mysql : package -> connector 
import mysql.connector

DB_CREDS = {
    'host' : '127.0.0.1',
    'port' : '3306',
    'user' : 'root',
    'password':"",
    'database' : 'siper_db'
}

def getConnection(debug=False):
    try:
        conn = mysql.connector.connect(**DB_CREDS)
        if conn.is_connected():
            if debug == True:
                print('Database connection Successfull')
            return conn
        else:
            print('Error in Connection')
            return None
    except Exception as e:
        print(f' Error :{e}')
        return None
    
import mysql.connector
import sys 

DB_CRED ={
    'host' : '127.0.0.1',
    'port' : '3307',
    'user' : 'root',
    'password' : '',
    'database' : 'siper_db'
}

def getConnection():
    conn = mysql.connector.connect(**DB_CRED)
    if conn.is_connected():
        print('Database Connected Successfully')
        return conn
    else:
        print('Connection Error')
    return None


def main():
    result = getConnection()
    print('Result:',result)


if __name__ == '__main__':
    sys.exit(main())
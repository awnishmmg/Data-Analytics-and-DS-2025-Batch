from pdbc.db_config import getConnection
import sys 

def DeletetUser(id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = f"delete from users where id='{id}'"
        cursor.execute(query)
    except Exception as e:
        print(f' Error in Query : {e}')
    finally:
        conn.commit()
        conn.close()
        return cursor._rowcount

def main():
    id =  input('Enter the ID:')
    effectedRows = DeletetUser(id)
    if effectedRows:
        print('User Deleted with ID=',id)
    else:
        print('User Not Deleted')

if __name__ == '__main__':
    sys.exit(main())
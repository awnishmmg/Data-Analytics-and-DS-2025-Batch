
from db3 import getConnection
import sys 

def insertProduct(name,desc,price,brand,qty):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = f"insert into products(`name`,`desc`,`price`,`brand`,`qty`) values('{name}','{desc}','{price}','{brand}','{qty}')";
        cursor.execute(query)
    except Exception as e:
        print(f'Query Error {e}')
    finally:
        conn.commit()
        conn.close()
    return cursor.lastrowid

def main():
    insertProduct('Maggie','This is Maggie','12','Nestle','50')


if __name__ == '__main__':
    sys.exit(main())
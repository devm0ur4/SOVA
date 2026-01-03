from src.db.connection import get_connection

def readAll():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM UNIDADES')
        return cursor.fetchall()


def read(id):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM UNIDADES WHERE COD = ?',(id,))
        return cursor.fetchone()


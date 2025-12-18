from db.connection import get_connection
from dataclasses import dataclass

@dataclass
class Fatura:
    nf : str
    valor_boleto : float
    valor_total: float
    emissao: str
    vencimento: str
    unidade_cod: str
    
def insert(f : Fatura):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute(
            """"
            'INSERT INTO FATURAS(NF, VALOR_BOLETO, VALOR_TOTAL, EMISSAO, VENCIMENTO, UNIDADE_COD'
            'VALUES (?,?,?,?,?,?)' 
            ')
            """,
            (
                f.nf, 
                f.valor_boleto,
                f.valor_total,
                f.emissao,
                f.vencimento,
                f.unidade_cod,
            )
        )

def delete(ID):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM FATURAS WHERE NF = ?', (ID,))
        

def readAll():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM FATURAS')
        return cursor.fetchall()


def read(ID):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM FATURAS WHERE NF = ?',(ID,))
        return cursor.fetchone()


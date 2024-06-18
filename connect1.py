import sqlite3 as sql


try:

    with sql.connect('PYTHON/Python Project/filmflix.db') as db_con:
        #we create a cursor object and bind it with the bd_con 
        db_cursor = db_con.cursor()
except sql.OperationalError as oe: 
    #handle exception /error raised78
    print(f"connection failed because: {oe}")
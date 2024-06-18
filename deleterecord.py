from connect1 import *
 
def delete_record():
 
    try:
        # SongID is use to delete a record as it is a primary key (unique)field
        id_field = input("Enter the FilmID of the record to be deleted:")
        db_cursor.execute("SELECT * FROM tblfilms WHERE FilmID = ?", (id_field,))
        a_record = db_cursor.fetchone()

        if a_record == None:
            print(f"The record with id {id_field} does not exists")
        else:
            db_cursor.execute("DELETE FROM tblfilms WHERE FilmID=?",(id_field,))
            db_con.commit()
            print(f"Record {id_field} deleted from film table")
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Displayed all records")
if __name__ == "__main__":
    delete_record()
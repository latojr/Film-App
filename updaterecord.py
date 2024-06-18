from connect1 import *
 
def update_record():
 
    try:
        # SongID is use to update a record as it is a primary key (unique)field
        id_field = input("Enter the FilmID of the record to be updated:")
 
        # db_cursor.execute(f"SELECT * FROM songs WHERE SongID = {id_field}")
        # or
        db_cursor.execute("SELECT * FROM tblfilms WHERE FilmID = ?", (id_field,)) # select a single record based on the SongID
 
        a_record = db_cursor.fetchone() # fetches a single record
 
        if a_record == None: # Is a singleton object use to check if a value is present/exists
            print(f"The record with {id_field} does not exists! ")
        else:
            field_name = input("Enter the field name of the record you want to update: ").title()
 
            field_value = input(f"Enter the value for the field {field_name}: ")
          
            field_value = "'"+field_value+"'" # wrap single quotes to match the value as it is in the table
 
            db_cursor.execute(f"UPDATE tblfilms SET {field_name} = {field_value} WHERE FilmID = {id_field} ")
            db_con.commit()
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Operation completed")
 
if __name__ == "__main__":
    update_record()
 
    
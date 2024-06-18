from connect1 import *
def read_record():
 
    try:
        # Select all records
        db_cursor.execute("SELECT * from tblfilms")
 
        # Fetchall() method to fetch/get the selected records from the table
        all_records = db_cursor.fetchall()
 
        # iterate and print all records
        for aRecord in all_records:
            print(aRecord)
        else:
            print("no record found in the film table")
            
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Displayed all records")
if __name__ == "__main__":
    read_record()
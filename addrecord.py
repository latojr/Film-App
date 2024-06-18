from connect1 import *

def add_record():
   try:
        film_title = input("enter film title: ")
        film_releasedyear = input("enter film released year: ")
        film_rating = input("enter film rating: ")
        film_duration = input("enter film duration: ")
        film_genre = input("enter film genre: ")

        #execute sql add statement
        db_cursor.execute("INSERT INTO tblfilms  VALUES(NULL, ?,?,?,?,?)",(film_title,film_releasedyear,film_rating,film_duration,film_genre))
        db_con.commit() #permently inserting a record in the db of film table 
        print(f"{film_title} inserted in the films table. ")
   except sql.ProgrammingError as pe: #use to handle invalid sql statement
       print(f"failed operation {pe}")
   except sql.OperationalError as oe:
       print(f"connection failed because: {oe}")
   except sql.Error as e:
       print(f"error resulted in:{e}")
   finally:
       print("operation completed")
if __name__ == "__main__":
    add_record()
    
                   


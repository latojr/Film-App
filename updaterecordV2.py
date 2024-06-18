from connect1 import *
 
def update_record():
 
    try:
        # SongID is use to update a record as it is a primary key (unique)field
        id_field = input("Enter the FilmID of the record to be updated: ")
 
        # db_cursor.execute(f"SELECT * FROM songs WHERE SongID = {id_field}")
        # or
        db_cursor.execute("SELECT * FROM tblfilms WHERE FilmID = ?", (id_field,)) # select a single record based on the SongID
 
        a_record = db_cursor.fetchone() # fetches a single record
 
        if a_record == None: # Is a singleton object use to check if a value is present/exists
            print(f"The record with id {id_field} does not exists! ")
        else:
            film_title = input("Enter film title: ")
            film_releasedyear = input("Enter film released year: ")
            film_rating = input("Enter the film rating: ")
            film_duration = input("Enter the film duration time: ")
            film_genre = input("Enter the film genre: ")
            
            film_title = "'"+film_title+"'" # wrap single quotes to match the value as it is in the table
            film_releasedyear = "'"+film_releasedyear+"'"
            film_rating = "'"+film_rating+"'"
            film_duration = "'"+film_duration+"'"
            film_genre = "'"+film_genre+"'"
 
            db_cursor.execute(f"UPDATE tblfilms SET title=?, yearReleased=?,rating=?,duration=?,genre=? WHERE FilmID=?", (film_title,film_releasedyear,film_rating,film_duration,film_genre,id_field))
            db_con.commit()
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Operation completed")
 
if __name__ == "__main__":
    update_record()
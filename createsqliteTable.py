from connect1 import *


db_cursor.execute(
     """ 
CREATE TABLE "tblfilms"(
     "FilmID" INTEGER not null unique,
     "Title" text,
     "YearReleased" integer,
     "Rating" text,
     "Duration" integer,
     "Genre" text,
     PRIMARY KEY ("FilmID" autoincrement)
) 
""" 
)
#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

conn = sqlite3.connect('C:/Users/mouse/tornados.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
tornado_id = form.getvalue("TornadoID")
state_id = form.getvalue("StateID")
rating_id = form.getvalue("RatingID")
event_type_id = form.getvalue("EventTypeID")
start_time = form.getvalue("StartTime")
path_length = form.getvalue("PathLengthMi")

# Insert into Tornado table
cursor.execute(
    "INSERT INTO Tornado (TornadoID, StateID, RatingID, EventTypeID, StartTime, PathLengthMi) VALUES (?, ?, ?, ?, ?, ?)",
    (tornado_id, state_id, rating_id, event_type_id, start_time, path_length)
)

conn.commit()
conn.close()

print("<html><body><h1>Tornado Inserted Successfully!</h1></body></html>")

#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')  # update this path to your actual database if needed
cursor = conn.cursor()

# Get form input
form = cgi.FieldStorage()
event_type_id = form.getvalue("EventTypeID")
name = form.getvalue("Name")
description = form.getvalue("Description")
land_or_water = form.getvalue("LandOrWater")
frequency_rank = form.getvalue("FrequencyRank")
example_region = form.getvalue("ExampleRegion")

# Insert into EventType table
cursor.execute("""
    INSERT INTO EventType (EventTypeID, Name, Description, LandOrWater, FrequencyRank, ExampleRegion)
    VALUES (?, ?, ?, ?, ?, ?)
""", (event_type_id, name, description, land_or_water, frequency_rank, example_region))

# Save and close
conn.commit()
conn.close()

# Response
print("<html><body><h1>Event Info Inserted Successfully!</h1></body></html>")

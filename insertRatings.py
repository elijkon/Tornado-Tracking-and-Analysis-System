#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')  # update this path to your actual database if needed
cursor = conn.cursor()

# Get form input
form = cgi.FieldStorage()
rating_id = form.getvalue("RatingID")
code = form.getvalue("Code")
description = form.getvalue("Description")
min_wind = form.getvalue("MinWindSpeed")
max_wind = form.getvalue("MaxWindSpeed")
damage_level = form.getvalue("DamageLevel")

# Insert into Rating table
cursor.execute("""
    INSERT INTO Rating (RatingID, Code, Description, MinWindSpeed, MaxWindSpeed, DamageLevel)
    VALUES (?, ?, ?, ?, ?, ?)
""", (rating_id, code, description, min_wind, max_wind, damage_level))

# Finalize
conn.commit()
conn.close()

# Response
print("<html><body><h1>RatingID Record Inserted Successfully!</h1></body></html>")

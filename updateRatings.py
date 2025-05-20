#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')
cursor = conn.cursor()

# Get form values
form = cgi.FieldStorage()
rating_id = form.getvalue("RatingID")
code = form.getvalue("Code")
description = form.getvalue("Description")
min_wind = form.getvalue("MinWindSpeed")
max_wind = form.getvalue("MaxWindSpeed")
damage_level = form.getvalue("DamageLevel")

# Update the record
cursor.execute("""
    UPDATE Rating
    SET Code = ?, Description = ?, MinWindSpeed = ?, MaxWindSpeed = ?, DamageLevel = ?
    WHERE RatingID = ?
""", (code, description, min_wind, max_wind, damage_level, rating_id))

# Commit and close
conn.commit()
conn.close()

# Confirmation
print(f"<html><body><h1>✅ Rating ID {rating_id} updated successfully!</h1></body></html>")

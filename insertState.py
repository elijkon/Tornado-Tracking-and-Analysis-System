#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')  # update this path to your actual database if needed
cursor = conn.cursor()

# Get form input
form = cgi.FieldStorage()
state_id = form.getvalue("StateID")
name = form.getvalue("Name")
abbreviation = form.getvalue("Abbreviation")
region = form.getvalue("Region")
population = form.getvalue("Population")
area_sq_mi = form.getvalue("AreaSqMi")

# Insert the data
cursor.execute(
    "INSERT INTO State (StateID, Name, Abbreviation, Region, Population, AreaSqMi) VALUES (?, ?, ?, ?, ?, ?)",
    (state_id, name, abbreviation, region, population, area_sq_mi)
)

# Save and close
conn.commit()
conn.close() 

# Response
print("<html><body><h1>State Info Record Inserted Successfully!</h1></body></html>")

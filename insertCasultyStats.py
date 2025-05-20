#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')  # update this path to your actual database if needed
cursor = conn.cursor()

# Get form input
form = cgi.FieldStorage()
stat_id = form.getvalue("StatID")
tornado_id = form.getvalue("TornadoID")
injuries = form.getvalue("Injuries")
fatalities = form.getvalue("Fatalities")
property_damage = form.getvalue("PropertyDamage")
crop_damage = form.getvalue("CropDamage")

# Insert into CasualtyStats table
cursor.execute(
    "INSERT INTO CasualtyStats (StatID, TornadoID, Injuries, Fatalities, PropertyDamage, CropDamage) VALUES (?, ?, ?, ?, ?, ?)",
    (stat_id, tornado_id, injuries, fatalities, property_damage, crop_damage)
)

# Save and close
conn.commit()
conn.close()

# Response
print("<html><body><h1>CasualtyStats Record Inserted Successfully!</h1></body></html>")

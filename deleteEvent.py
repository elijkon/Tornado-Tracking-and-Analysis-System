#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Connect to the database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')  # adjust path as needed
cursor = conn.cursor()

# Get form data
form = cgi.FieldStorage()
id = form.getvalue("EventTypeID")

# Delete the user
cursor.execute("DELETE FROM EventType WHERE EventTypeID = ?", (id,))

# Commit and close
conn.commit()
conn.close()

print(f"<html><body><h1>✅ User '{id}' deleted (if found).</h1></body></html>")

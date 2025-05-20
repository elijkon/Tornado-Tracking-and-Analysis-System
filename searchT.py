#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
tornado_id = form.getvalue("TornadoID")

# Connect to the database
conn = sqlite3.connect("C:/Users/mouse/tornados.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Tornado WHERE TornadoID = ?", (tornado_id,))
row = cursor.fetchone()

# Display result
print("<html><body>")
if row:
    print("<h2>Tornado Found:</h2>")
    print("<p>" + str(row) + "</p>")
else:
    print(f"<p>No tornado found with ID {tornado_id}.</p>")
print("</body></html>")

conn.close()

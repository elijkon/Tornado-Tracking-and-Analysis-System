#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

# Get query parameters
form = cgi.FieldStorage()
rating_code = form.getvalue("rating_code")
state_name = form.getvalue("state_name")

# Connect to DB
conn = sqlite3.connect("C:/Users/mouse/tornados.db")
cursor = conn.cursor()

# Base query with optional filters
query = """
SELECT T.TornadoID, T.StartTime, R.Code AS Rating, S.Name AS State, T.PathLengthMi, C.Fatalities
FROM Tornado T
JOIN Rating R ON T.RatingID = R.RatingID
JOIN State S ON T.StateID = S.StateID
JOIN CasualtyStats C ON T.TornadoID = C.TornadoID
WHERE 1 = 1
"""
params = []

if rating_code:
    query += " AND R.Code = ?"
    params.append(rating_code)

if state_name:
    query += " AND S.Name LIKE ?"
    params.append(f"%{state_name}%")

# Execute query
cursor.execute(query, params)
results = cursor.fetchall()

print("<html><body>")
print("<h2>Search Results:</h2>")

if results:
    print("<table border='1'>")
    print("<tr><th>ID</th><th>Start Time</th><th>Rating</th><th>State</th><th>Path Length</th><th>Fatalities</th></tr>")

    for row in results:
        print("<tr>")
        for val in row:
            print(f"<td>{val}</td>")
        print("</tr>")

    print("</table>")
else:
    print("<p>No matching tornado records found.</p>")

print("</body></html>")

conn.close()

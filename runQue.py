#!C:/Users/mouse/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import sqlite3

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
choice = form.getvalue("query_option")

conn = sqlite3.connect("C:/Users/mouse/tornados.db")
cursor = conn.cursor()

# Choose SQL based on form input
if choice == "fatalities":
    query = """
    SELECT T.TornadoID, T.StartTime, C.Fatalities
    FROM Tornado T
    JOIN CasualtyStats C ON T.TornadoID = C.TornadoID
    WHERE C.Fatalities > 0
    """
elif choice == "most_damage":
    query = """
    SELECT T.TornadoID, C.PropertyDamage
    FROM Tornado T
    JOIN CasualtyStats C ON T.TornadoID = C.TornadoID
    ORDER BY C.PropertyDamage DESC
    LIMIT 1
    """
elif choice == "count_by_state":
    query = """
    SELECT S.Name, COUNT(*) AS TornadoCount
    FROM Tornado T
    JOIN State S ON T.StateID = S.StateID
    GROUP BY S.Name
    ORDER BY TornadoCount DESC
    """
elif choice == "avg_by_rating":
    query = """
    SELECT R.Code, ROUND(AVG(T.PathLengthMi), 2) AS AvgPathLength
    FROM Tornado T
    JOIN Rating R ON T.RatingID = R.RatingID
    GROUP BY R.Code
    ORDER BY AvgPathLength DESC
    """
elif choice == "in_midwest":
    query = """
    SELECT T.TornadoID, T.StartTime, S.Region
    FROM Tornado T
    JOIN State S ON T.StateID = S.StateID
    WHERE S.Region = 'Midwest'
    """
else:
    query = None

# Execute and display
print("<html><body><h2>Query Results:</h2>")

if query:
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print("<table border='1'>")

        # Print column headers
        print("<tr>")
        for column in cursor.description:
            print(f"<th>{column[0]}</th>")  # column[0] is the column name
        print("</tr>")

        # Print data rows
        for row in rows:
            print("<tr>")
            for val in row:
                print(f"<td>{val}</td>")
            print("</tr>")

        print("</table>")

    else:
        print("<p>No results found.</p>")
else:
    print("<p>Invalid query selection.</p>")

print("</body></html>")
conn.close()

import sqlite3

# Connect to your database
conn = sqlite3.connect('C:/Users/mouse/tornados.db')
cursor = conn.cursor()

print("Sample Tornado Queries:\n")

# 1. Tornadoes with fatalities
print("1. Tornadoes with fatalities:\n")
cursor.execute("""
    SELECT T.TornadoID, T.StartTime, C.Fatalities
    FROM Tornado T
    JOIN CasualtyStats C ON T.TornadoID = C.TornadoID
    WHERE C.Fatalities > 0
""")
for row in cursor.fetchall():
    print(row)

# 2. Most destructive tornado (by property damage)
print("\n2. Most destructive tornado:\n")
cursor.execute("""
    SELECT T.TornadoID, C.PropertyDamage
    FROM Tornado T
    JOIN CasualtyStats C ON T.TornadoID = C.TornadoID
    ORDER BY C.PropertyDamage DESC
    LIMIT 1
""")
print(cursor.fetchone())

# 3. Count of tornadoes per state
print("\n3. Tornado count per state:\n")
cursor.execute("""
    SELECT S.Name, COUNT(*) as TornadoCount
    FROM Tornado T
    JOIN State S ON T.StateID = S.StateID
    GROUP BY S.Name
    ORDER BY TornadoCount DESC
""")
for row in cursor.fetchall():
    print(row)

# 4. Average path length by rating
print("\n4. Average path length by rating:\n")
cursor.execute("""
    SELECT R.Code, ROUND(AVG(T.PathLengthMi), 2) as AvgPathLength
    FROM Tornado T
    JOIN Rating R ON T.RatingID = R.RatingID
    GROUP BY R.Code
    ORDER BY AvgPathLength DESC
""")
for row in cursor.fetchall():
    print(row)

# 5. Tornadoes in a specific region (e.g., Midwest)
print("\n5. Tornadoes in the Midwest region:\n")
cursor.execute("""
    SELECT T.TornadoID, T.StartTime, S.Region
    FROM Tornado T
    JOIN State S ON T.StateID = S.StateID
    WHERE S.Region = 'Midwest'
""")
for row in cursor.fetchall():
    print(row)

conn.close()

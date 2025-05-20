import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('/Users/mouse/tornados.db')
cursor = connection.cursor()

updates = [
    ('2025-04-01 14:00:00', 1),
    ('2025-04-02 02:00:00', 2),
    ('2025-04-02 14:00:00', 3),
    ('2025-04-03 02:00:00', 4),
    ('2025-04-03 14:00:00', 5),
    ('2025-04-04 02:00:00', 6),
    ('2025-04-04 14:00:00', 7),
    ('2025-04-05 02:00:00', 8)
]

# Run the update for each pair
cursor.executemany("UPDATE Tornado SET StartTime = ? WHERE TornadoID = ?", updates)

# Commit the changes and close the connection
connection.commit()
connection.close()

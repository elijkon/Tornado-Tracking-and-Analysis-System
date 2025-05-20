import sqlite3

# Connect to your SQLite database
connection = sqlite3.connect('/Users/mouse/tornados.db')  # Update path if needed
cursor = connection.cursor()

# SQL insert statement
sql = '''
INSERT INTO CasualtyStats (StatID, TornadoID, Injuries, Fatalities, PropertyDamage, CropDamage)
VALUES (?, ?, ?, ?, ?, ?)
'''

# Values you provided
val = [
    (2, 2, 1, 1, 0.5, 0.2),
    (3, 3, 2, 0, 1, 0.4),
    (4, 4, 3, 1, 1.5, 0.6),
    (5, 5, 4, 0, 2, 0.8),
    (6, 6, 0, 1, 2.5, 1.0),
    (7, 7, 1, 0, 3, 1.2),
    (8, 8, 2, 1, 3.5, 1.4),
    (9, 9, 3, 0, 4, 1.6),
    (10, 10, 4, 1, 4.5, 1.8),
    (11, 11, 0, 0, 5, 2.0),
    (12, 12, 1, 1, 5.5, 2.2),
    (13, 13, 2, 0, 6, 2.4),
    (14, 14, 3, 1, 6.5, 2.6),
    (15, 15, 4, 0, 7, 2.8),
    (16, 16, 0, 1, 7.5, 3.0),
    (17, 17, 1, 0, 8, 3.2),
    (18, 18, 2, 1, 8.5, 3.4),
    (19, 19, 3, 0, 9, 3.6),
    (20, 20, 4, 1, 9.5, 3.8)
]

# Execute insert
cursor.executemany(sql, val)

# Commit the changes and close the connection
connection.commit()
connection.close()
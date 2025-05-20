import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('/Users/mouse/tornados.db')
cursor = connection.cursor()

sql = '''
INSERT INTO Tornado (TornadoID, StateID, RatingID, EventTypeID, StartTime, PathLengthMi)
VALUES (?, ?, ?, ?, ?, ?)
'''

val = [
    (9, 9, 3, 4, '2025-04-05 14:00:00', 3.9),
    (10, 10, 4, 5, '2025-04-06 02:00:00', 4.2),
    (11, 11, 5, 1, '2025-04-06 14:00:00', 4.5),
    (12, 12, 6, 2, '2025-04-07 02:00:00', 4.8),
    (13, 13, 1, 3, '2025-04-07 14:00:00', 5.1),
    (14, 14, 2, 4, '2025-04-08 02:00:00', 5.4),
    (15, 15, 3, 5, '2025-04-08 14:00:00', 5.7),
    (16, 16, 4, 1, '2025-04-09 02:00:00', 6.0),
    (17, 17, 5, 2, '2025-04-09 14:00:00', 6.3),
    (18, 18, 6, 3, '2025-04-10 02:00:00', 6.6),
    (19, 19, 1, 4, '2025-04-10 14:00:00', 6.9),
    (20, 20, 2, 5, '2025-04-11 02:00:00', 7.2)
]

cursor.executemany(sql, val)

# Commit the changes and close the connection
connection.commit()
connection.close()
import sqlite3

# Connect to your SQLite database
connection = sqlite3.connect('/Users/mouse/tornados.db')  # Update path if needed
cursor = connection.cursor()

tornado_values = [
    (21, 2, 4, 1, '2025-04-01 03:00:00', 5.7),
    (22, 3, 5, 2, '2025-04-02 06:00:00', 8.9),
    (23, 4, 6, 3, '2025-04-03 09:00:00', 6.1),
    (24, 5, 1, 4, '2025-04-04 12:00:00', 7.3),
    (25, 6, 2, 5, '2025-04-05 15:00:00', 6.5),
    (26, 7, 3, 1, '2025-04-06 18:00:00', 1.7),
    (27, 8, 4, 2, '2025-04-07 21:00:00', 6.9),
    (28, 9, 5, 3, '2025-04-08 00:00:00', 4.1),
    (29, 10, 6, 4, '2025-04-09 03:00:00', 7.3),
    (30, 11, 1, 5, '2025-04-10 06:00:00', 7.5),
    (31, 12, 2, 1, '2025-04-11 09:00:00', 8.7),
    (32, 13, 3, 2, '2025-04-12 12:00:00', 3.9),
    (33, 14, 4, 3, '2025-04-13 15:00:00', 9.1),
    (34, 15, 5, 4, '2025-04-14 18:00:00', 3.3),
    (35, 16, 6, 5, '2025-04-15 21:00:00', 8.5),
]

# --- CasualtyStats records (IDs 21–35) ---
casualty_values = [
    (21, 21, 1, 0, 8.4, 6.3),
    (22, 22, 2, 1, 8.8, 6.6),
    (23, 23, 3, 0, 9.2, 6.9),
    (24, 24, 0, 1, 9.6, 7.2),
    (25, 25, 1, 0, 10.0, 7.5),
    (26, 26, 2, 1, 10.4, 7.8),
    (27, 27, 3, 0, 10.8, 8.1),
    (28, 28, 0, 1, 11.2, 8.4),
    (29, 29, 1, 0, 11.6, 8.7),
    (30, 30, 2, 1, 12.0, 9.0),
    (31, 31, 3, 0, 12.4, 9.3),
    (32, 32, 0, 1, 12.8, 9.6),
    (33, 33, 1, 0, 13.2, 9.9),
    (34, 34, 2, 1, 13.6, 10.2),
    (35, 35, 3, 0, 14.0, 10.5),
]

# Insert both
cursor.executemany("""
    INSERT INTO Tornado (TornadoID, StateID, RatingID, EventTypeID, StartTime, PathLengthMi)
    VALUES (?, ?, ?, ?, ?, ?)
""", tornado_values)

cursor.executemany("""
    INSERT INTO CasualtyStats (StatID, TornadoID, Injuries, Fatalities, PropertyDamage, CropDamage)
    VALUES (?, ?, ?, ?, ?, ?)
""", casualty_values)

# Commit the changes and close the connection
connection.commit()
connection.close()
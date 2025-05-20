import sqlite3

# Connect to your SQLite database
connection = sqlite3.connect('/Users/mouse/tornados.db')  # Update path if needed
cursor = connection.cursor()

# SQL insert statement
sql = '''
INSERT INTO State (StateID, Name, Abbreviation, Region, Population, AreaSqMi)
VALUES (?, ?, ?, ?, ?, ?)
'''

# Sample 20 records for State table
val = [
    (2, "Oklahoma", "OK", "South", 3956971, 69899),
    (3, "Kansas", "KS", "Midwest", 2937880, 82278),
    (4, "Nebraska", "NE", "Midwest", 1961504, 77348),
    (5, "Alabama", "AL", "South", 5024279, 52420),
    (6, "Georgia", "GA", "South", 10711908, 59425),
    (7, "Missouri", "MO", "Midwest", 6169270, 69707),
    (8, "Iowa", "IA", "Midwest", 3193079, 56273),
    (9, "Illinois", "IL", "Midwest", 12587530, 57914),
    (10, "Indiana", "IN", "Midwest", 6785528, 36420),
    (11, "Arkansas", "AR", "South", 3025891, 53179),
    (12, "Mississippi", "MS", "South", 2961279, 48432),
    (13, "Louisiana", "LA", "South", 4657757, 52378),
    (14, "Tennessee", "TN", "South", 6916897, 42144),
    (15, "South Dakota", "SD", "Midwest", 895376, 77116),
    (16, "North Dakota", "ND", "Midwest", 779094, 70698),
    (17, "Minnesota", "MN", "Midwest", 5706494, 86936),
    (18, "Kentucky", "KY", "South", 4509394, 40408),
    (19, "Ohio", "OH", "Midwest", 11799448, 44825),
    (20, "Wisconsin", "WI", "Midwest", 5893718, 65496)
]

# Execute insert
cursor.executemany(sql, val)

# Commit the changes and close the connection
connection.commit()
connection.close()
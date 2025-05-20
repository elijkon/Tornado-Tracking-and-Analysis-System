import sqlite3

# Connect to a new SQLite database (it will be created if it does not exist)
connection = sqlite3.connect('/Users/mouse/tornados.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
# Create State table
cursor.execute('''CREATE TABLE IF NOT EXISTS State (
    StateID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Abbreviation TEXT,
    Region TEXT,
    Population INTEGER,
    AreaSqMi REAL
)''')

# Create Rating table
cursor.execute('''CREATE TABLE IF NOT EXISTS Rating (
    RatingID INTEGER PRIMARY KEY,
    Code TEXT NOT NULL,
    Description TEXT,
    MinWindSpeed INTEGER,
    MaxWindSpeed INTEGER,
    DamageLevel TEXT
)''')

# Create EventType table
cursor.execute('''CREATE TABLE IF NOT EXISTS EventType (
    EventTypeID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Description TEXT,
    LandOrWater TEXT,
    FrequencyRank INTEGER,
    ExampleRegion TEXT
)''')

# Create Tornado table
cursor.execute('''CREATE TABLE IF NOT EXISTS Tornado (
    TornadoID INTEGER PRIMARY KEY,
    StateID INTEGER NOT NULL,
    RatingID INTEGER NOT NULL,
    EventTypeID INTEGER NOT NULL,
    StartTime TEXT NOT NULL,
    PathLengthMi REAL,
    FOREIGN KEY (StateID) REFERENCES State(StateID),
    FOREIGN KEY (RatingID) REFERENCES Rating(RatingID),
    FOREIGN KEY (EventTypeID) REFERENCES EventType(EventTypeID)
)''')

# Create CasualtyStats table
cursor.execute('''CREATE TABLE IF NOT EXISTS CasualtyStats (
    StatID INTEGER PRIMARY KEY,
    TornadoID INTEGER NOT NULL,
    Injuries INTEGER,
    Fatalities INTEGER,
    PropertyDamage REAL,
    CropDamage REAL,
    FOREIGN KEY (TornadoID) REFERENCES Tornado(TornadoID)
)''')

# Commit the changes and close the connection
connection.commit()
connection.close()

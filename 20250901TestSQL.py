import sqlite3

# Connect to an in-memory SQLite DB
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);")

# Insert sample data
cursor.executemany("INSERT INTO users (name) VALUES (?)", [("Alice",), ("Bob",), ("Carla",)])

# Query data
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

print("✅ SQLite is working inside Codespaces!")
for row in rows:
    print(row)

conn.close()
    
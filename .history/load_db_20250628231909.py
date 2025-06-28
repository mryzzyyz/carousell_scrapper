import sqlite3

# Step 1: Connect to the database

conn = sqlite3.connect('carousell_laptops.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

# Step 2: Run a SELECT query
c.execute("SELECT listing_url FROM listings")

# Step 3: Fetch all rows
rows = c.fetchall()

# Step 4: Process/display
for row in rows:
    print(row[0])  # or customize: print(row[2], row[3]) for title and price

# Close connection
conn.close()

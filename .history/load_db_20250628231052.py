import sqlite3
import os
print("📍 Current working directory:", os.getcwd())

# Step 1: Connect to the database
conn = sqlite3.connect('carousell_laptops.db')
c = conn.cursor()

# Step 2: Run a SELECT query
c.execute("SELECT * FROM listings")

# Step 3: Fetch all rows
rows = c.fetchall()

# Step 4: Process/display
for row in rows:
    print(row)  # or customize: print(row[2], row[3]) for title and price

# Close connection
conn.close()

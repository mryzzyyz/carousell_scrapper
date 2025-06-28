import sqlite3
from datetime import datetime

# Step 1: Connect to the database
conn = sqlite3.connect('carousell_laptops.db')
c = conn.cursor()
c.execute("SELECT listing_url, datetime FROM listings WHERE DATE(datetime) = ")

# Step 3: Fetch all rows
rows = c.fetchall()

print(rows)
# Close connection
conn.close()

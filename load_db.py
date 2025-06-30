# import sqlite3
# from datetime import datetime

# FETCH_UNTIL = 3
# # Step 1: Connect to the database
# conn = sqlite3.connect('carousell_laptops.db')
# c = conn.cursor()
# c.execute(F"SELECT * FROM listings WHERE DATE(datetime) >= DATE('now', '-{FETCH_UNTIL} days')")

# # Step 3: Fetch all rows
# rows = c.fetchall()

# print(rows)
# # Close connection
# conn.close()
import os
print(os.getcwd())
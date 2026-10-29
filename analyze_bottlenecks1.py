import pandas as pd
import sqlite3

# Connect to your new database
conn = sqlite3.connect('smart_supply_chain.db')

# Write a SQL query to find the worst delays
sql_query = """
SELECT 
    Delivery_Status, 
    COUNT(*) as Total_Orders
FROM shipments
GROUP BY Delivery_Status
ORDER BY Total_Orders DESC;
"""

# Run the query and print the results
results = pd.read_sql_query(sql_query, conn)
print(results)

conn.close()
import pandas as pd
import sqlite3

# 1. Load the Kaggle dataset
print("Reading the Kaggle dataset...")
# DataCo often uses 'latin1' encoding, which prevents read errors
csv_file = 'DataCoSupplyChainDataset.csv' 
df = pd.read_csv(csv_file, encoding='latin1')

# 2. Clean up the column names for SQL (replacing spaces with underscores)
df.columns = [col.replace(' ', '_').replace('(', '').replace(')', '') for col in df.columns]

# 3. Create the SQL Database
print("Building the SQL database...")
# This creates a local database file right in your VS Code folder
conn = sqlite3.connect('smart_supply_chain.db')

# 4. Push the data into a SQL table named 'shipments'
df.to_sql('shipments', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
print("Success! Your SQL database 'smart_supply_chain.db' is ready for analysis.")
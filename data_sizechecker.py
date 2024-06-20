import mysql.connector

def get_row_size(row):
    return sum(len(str(col).encode('utf-8')) for col in row)

def get_cell_sizes(row):
    return [len(str(col).encode('utf-8')) for col in row]

conn = mysql.connector.connect(
    user='YOUR_USERNAME',
    password='PASSWORD_FOR_THE USER',
    host='localhost',
    database='EXAMPLE_DB',
    port= '3306'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Wohnung_kaufen_AT")

rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

for idx, row in enumerate(rows, start=1):
    row_size = get_row_size(row)
    cell_sizes = get_cell_sizes(row)
    print(f"Row {idx}: Total size = {row_size} bytes")
    for col, size in zip(columns, cell_sizes):
        print(f"  Column {col}: {size} bytes")

cursor.close()
conn.close()

import pymssql

SERVER = '<server-address>'
DATABASE = '<database-name>'
USERNAME = '<username>'
PASSWORD = '<password>'

connectionString = f'server={SERVER};database={DATABASE};user={USERNAME};password={PASSWORD},as_dict=True'

conn = pymssql.connect(connectionString)

cursor = conn.cursor()
cursor.execute("Select @@version")

records = cursor.fetchall()
for r in records:
    print(r)
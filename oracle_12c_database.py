import oracledb

# If the port number is 1521, there's no need to specify it.
con = oracledb.connect(user="USER_ID", password="PASSWORD", dsn="HOSTNAME:PORT_NUMBER/SID")

cursor = con.cursor()

for row in cursor.execute("SELECT * FROM V$VERSION"):
    print(row)
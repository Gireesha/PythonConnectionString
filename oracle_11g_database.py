import cx_Oracle

# Ensure that the directory containing the Oracle InstantClient 
# installation matches the location where the extracted files are located.
cx_Oracle.init_oracle_client(lib_dir=r"C:\OracleInstantClient")

# If the port number is 1521, there's no need to specify it.
con = cx_Oracle.connect(user="USER_ID", password="PASSWORD", dsn="HOSTNAME:PORT_NUMBER/SID")

cursor = con.cursor()

for row in cursor.execute("SELECT * FROM V$VERSION"):
    print(row)
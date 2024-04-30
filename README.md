# Python Connection String
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
________________________

 Here are several examples demonstrating how to establish connections to various data sources using Python.

## Software required
Python compiler --> https://www.python.org/downloads/  
Visual Studio code --> https://code.visualstudio.com/download  

## oracle_11g_database.py

### Step 1
Install cx_Oracle.  
  
  On Linux or Mac:  
    
    pip install --upgrade cx_Oracle

  On Windows:  

    pip install cx_Oracle --upgrade

### Step 2
Download Oracle Instant Client and then extract it.  
For Windows --> https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html:

  
### Step 3
Notify the cx_Oracle module of the location of the Instant Client.

    cx_Oracle.init_oracle_client(lib_dir=r"C:\{{FOLDER_NAME}}")

## oracle_12c_database.py

### Step 1
Install oracledb.  
  
  On Linux or Mac:  
    
    pip install --upgrade oracledb

  On Windows:  

    pip install oracledb --upgrade

## mssql_mssql.py

### Step 1
Install oracledb.  
  
  On Linux or Mac:  
    
    pip install --upgrade pymssql

  On Windows:  

    pip install pymssql --upgrade

## mssql_odbc.py

### Step 1
Get and install the Microsoft ODBC driver for SQL Server.  
For Windows --> https://learn.microsoft.com/en-us/sql/connect/odbc/windows/system-requirements-installation-and-driver-files?view=sql-server-ver16#installing-microsoft-odbc-driver-for-sql-server
  
### Step 2
Install pymssql.  
  
  On Linux or Mac:  
    
    pip install --upgrade pymssql

  On Windows:  

    pip install pymssql --upgrade

## ascii_json.py

### Step 1
Ensure that the .json file is present in the directory where the .py file resides.

### Step 2
Verify that the data within the .json file conforms to the JSON format.

## References
https://cx-oracle.readthedocs.io/en/latest/  
https://python-oracledb.readthedocs.io/en/latest/  
https://learn.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server?view=sql-server-ver16  
https://docs.python.org/3/library/json.html

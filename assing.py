import mysql.connector

host = 'localhost'
database = 'sam'
user = 'root'
password = '11223344'

try:
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print('Connected to MySQL database')

        # Execute a sample query
        cursor = connection.cursor()
        cursor.execute('SELECT VERSION()')

        # Fetch the result
        db_version = cursor.fetchone()
        print('MySQL Database Version:', db_version[0])

except mysql.connector.Error as e:
    print('Error connecting to MySQL:', e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')

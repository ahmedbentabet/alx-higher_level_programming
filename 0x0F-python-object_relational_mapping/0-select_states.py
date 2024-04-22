#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    # Extract MySQL connection parameters from command-line arguments
    username = sys.argv[1]
    print(username)
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = username,
        passwd = password,
        db = database
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    conn.close()

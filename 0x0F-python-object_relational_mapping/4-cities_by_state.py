#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Extract MySQL connection parameters and state name from command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute SQL query
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM states, cities
        WHERE cities.state_id = states.id
        ORDER BY cities.id
    """)

    # Fetch all rows from the result set
    # The fetched rows are returned as a list of tuples
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    conn.close()

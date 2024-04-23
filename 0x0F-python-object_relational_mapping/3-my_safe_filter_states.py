#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, safe from SQL injection.

Usage: ./3-my_safe_filter_states.py <username> <passwrd> <db> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Extract MySQL connection parameters and state name from command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Use a parameterized query to prevent SQL injection
    query = """
        SELECT * FROM states
        WHERE BINARY name LIKE %s
        ORDER BY id
        """
    cursor.execute(query, (state_name_searched,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    conn.close()

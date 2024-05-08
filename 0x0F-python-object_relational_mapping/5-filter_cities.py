#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <username> <password> <database> <state name>
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Extract MySQL connection parameters & state name from command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_neme = sys.argv[4]

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
    query = """
        SELECT cities.name
        FROM states, cities
        WHERE cities.state_id = states.id AND states.name= %s
        ORDER BY cities.id
    """
    cursor.execute(query, (state_neme,))

    # Fetch all rows from the result set
    # The fetched rows are returned as a list of tuples
    rows = cursor.fetchall()

    # Display the cities
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    # Close cursor and database connection
    cursor.close()
    conn.close()

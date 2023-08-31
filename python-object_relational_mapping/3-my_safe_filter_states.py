#!/usr/bin/env python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor
        cursor = db.cursor()

        # Create the SQL query with user input
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"

        # Execute the SQL query with the state name
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if db:
            db.close()


if __name__ == "__main__":
    main()
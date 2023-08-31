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

        # script that takes in the name of a state as an argumant and lists all 
        # cities of that state
        query ="SELECT cities.name FROM cities JOIN states ON cities.state_id \
            = states.id WHERE BINARY states.name = %s ORDER BY cities.id ASC"

        # Execute the SQL query with the state name
        cursor.execute(query, (state_name,))
        # Fetch all the rows
        rows = cursor.fetchall()
        # Display the results
        print(", ".join([row[0] for row in rows]))

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if db:
            db.close()


if __name__ == "__main__":
    main()
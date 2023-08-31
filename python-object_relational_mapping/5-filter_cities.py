#!/usr/bin/env python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database
        )

        # Create a cursor
        cursor = db.cursor()

        # Create the SQL query with a parameter placeholder
        query = """SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities
                 JOIN states ON cities.state_id = states.id
                 WHERE states.name = %s ORDER BY cities.id ASC"""

        # Execute the SQL query with the state name parameter
        cursor.execute(query, (state_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Display the results
        if result and result[0]:
            print(result[0])
        else:
            print("No cities found for the state:", state_name)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if db:
            db.close()


if __name__ == "__main__":
    main()
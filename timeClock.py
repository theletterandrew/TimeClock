# timeClock.py
# CLI for a time manager application
import sqlite3
import sql_backend

sqlite_file = 'data/timeClock.sqlite'

def main():
    while True:
        response = input("Enter a CMD or type HELP for more info: ")

        if response == "HELP":
            print("Enter START to start a new project.")
            print("Enter CONT to continue an existing project.")
            print("Enter STOP to stop working on a project.")
            print("Enter QUIT to exit program.")

        elif response == "START":
            name = input("Enter a project name: ")
            conn = sql_backend.connectToDB(sqlite_file)
            sql_backend.create_project_table(conn, name)
            sql_backend.add_new_time_instance(conn, name)
            sql_backend.closeDB(conn)
            print("Now tracking " + name)

        elif response == "CONT":
            existingName = input("What was the project's name? : ")
            conn = sql_backend.connectToDB(sqlite_file)
            sql_backend.add_new_time_instance(conn, existingName)
            sql_backend.closeDB(conn)
            print("Continuing to track " + existingName)

        elif response == "STOP":
            stopName = input("What was the project's name?: ")
            conn = sql_backend.connectToDB(sqlite_file)
            sql_backend.add_time_out(conn, stopName)
            sql_backend.closeDB(conn)
            print("No longer tracking " + stopName)

        elif response == "QUIT":
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()

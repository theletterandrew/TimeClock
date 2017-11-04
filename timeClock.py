# timeClock.py
# CLI for a time manager application
import sqlite3
sql_create_table = """CREATE TABLE IF NOT EXISTS (
                        entryNum integer PRIMARY KEY,
                        timeIn text,
                        timeOut text,
                        total integer
);"""

def main():
    while True:
        response = input("Enter a CMD or type HELP for more info: ")

        if response == "HELP":
            print("Enter START to start a new project.")
            print("Enter CONT to continue an existing project.")
            print("Enter QUIT to exit program.")

        elif response == "START":
            name = input("Enter a project name: ")
            newTable(name)
            print("Now tracking " + name)

        elif response == "CONT":
            existingName = input("What was the project's name? : ")
            print("Continuing to track " + existingName)

        elif response == "QUIT":
            print("Goodbye!")
            break

def newTable(name):
    sqlite_file = "data/times.sqlite"
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS " + name + " (entryNum integer PRIMARY KEY, timeIn text, timeOut text, total integer);")
    conn.commit()
    conn.close()

def startProject(name):
    sqlite_file = "data/times.sqlite"
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    


if __name__ == '__main__':
    main()

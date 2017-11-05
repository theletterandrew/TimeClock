import sqlite3

sqlite_file = 'data/timeClock.sqlite'

def connectToDB(sqlite_file):
    try:
        conn = sqlite3.connect(sqlite_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_project_table(conn, projectName):
    entry_field = "entryNum"
    start_field = "time_in"
    end_field = "time_out"

    field_type_text = "text"
    field_type_int = "INTEGER"

    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS {pn} ({ef} {fti} PRIMARY KEY, {sf} {ftt} NOT NULL, {edf} {ftt})'\
            .format(pn = projectName, ef= entry_field, fti= field_type_int, sf=start_field, ftt=field_type_text, edf=end_field))
    # Save changes
    conn.commit()

def add_new_time_instance(conn, projectName):
    start_field = "time_in"
    c = conn.cursor()

    c.execute("INSERT INTO {pn} ({sf}) VALUES (datetime('now', 'localtime'))"\
            .format(pn = projectName, sf = start_field))
    # Save changes
    conn.commit()

def add_time_out(conn, projectName):
    end_field = "time_out"
    id_field = "entryNum"
    c = conn.cursor()

    c.execute("UPDATE {pn} SET {ef} = datetime('now', 'localtime') WHERE {idf} = (SELECT MAX({idf}) FROM {pn})"\
            .format(pn = projectName, ef = end_field, idf=id_field))
    # Save changes
    conn.commit()

def get_projects(conn):
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return res

def closeDB(conn):
    conn.close()

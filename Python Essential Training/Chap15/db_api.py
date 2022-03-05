import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor() # allows us to keep track of where we are in the database ase we run database commands
    print('create')
    cur.execute("DROP TABLE IF EXISTS test") # call exexcute to actually execute SQL
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
    INSERT INTO test (string, number) VALUES ('one', 1)
    """)
    print('insert')
    cur.execute("""
    INSERT INTO test (string, number) VALUES ('two', 2)
    """)
    cur.execute("""
    INSERT INTO test (string, number) VALUES ('two', 3)
    """)
    print('commit')
    db.commit()
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone() [0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()
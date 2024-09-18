import sqlite3

filename= 'example.py.db'
def setup_database():

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, 
    name TEXT)
    ''')

    cursor.execute('INSERT INTO users (name) VALUES ("Alice")')
    cursor.execute('INSERT INTO users (name) VALUES ("Bob")')
    cursor.execute('INSERT INTO users (name) VALUES ("Cartman")')
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    print(f"executing query: {query}")
    cursor.execute(query)
    user = cursor.fetchall()
    conn.close()
    return user

setup_database()
print("fetching a single user")
user_regular_query= get_user("1")
print(user_regular_query)

print("injecting SQL")
user_hacked = get_user("1 OR 1=1")
print(user_hacked)
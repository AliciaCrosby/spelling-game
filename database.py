import sqlite3
users = sqlite3.connect('users.db')
c = users.cursor()
def createtable():
    try:
        c = users.cursor()
    # Check if table users does not exist and create it
        c.execute('''
                      CREATE TABLE IF NOT EXISTS users(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL,
                      score INT NOT NULL,
                      badges TEXT NOT NULL)
                  ''')
        users.commit()
    except Exception as e:
        users.rollback()
        raise e
        c.execute('''CREATE TABLE users
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INT NOT NULL,
            badges TEXT NOT NULL);''')
        users.commit()
    
def selectall():
    c.execute('SELECT * FROM users')
    allresults = c.fetchall()
    return allresults

def finduserdata(username):
    alls = selectall()
    for each in alls:
        if each[1]==username:
            return each
        
def insertnew(username):
    username = username
    score = 0
    badges = "A"
    c.execute("INSERT INTO users (username,score,badges) VALUES (?, ?, ?)", (username, score, badges))
    users.commit()
    
def updatescore(username,score):
    c.execute('''UPDATE users SET score = ? WHERE username = ? ''',(score, username))
    users.commit()

def findscore(username):
    c.execute('''SELECT score FROM users WHERE username=?''', (username,))
    current = c.fetchone()
    return current



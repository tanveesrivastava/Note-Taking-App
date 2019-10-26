import sqlite3

def connect():
    conn=sqlite3.connect("notes.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS b(id INTEGER PRIMARY KEY, title text)")
    conn.commit()
    conn.close()

def insert(title):
    conn=sqlite3.connect("notes.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO b VALUES (NULL,?)",(title,))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("notes.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM b")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title=""):
    conn=sqlite3.connect("notes.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM b WHERE title=?", (title))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("notes.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM b WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title):
    conn=sqlite3.connect("notes.db")
    cur=conn.cursor()
    cur.execute("UPDATE b SET title=? WHERE id=?",(title,id))
    conn.commit()
    conn.close()

connect()



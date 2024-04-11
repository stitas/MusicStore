import sqlite3

class database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY,title TEXT,author TEXT,date TEXT,link TEXT)")
        self.conn.commit()

    def add_entry(self,title,author,date,link):
        self.cur.execute("INSERT INTO music VALUES (NULL,?,?,?,?)",(title,author,date,link))
        self.conn.commit()

    def view_all(self):
        self.cur.execute("SELECT * FROM music")
        rows = self.cur.fetchall()
        return rows

    def search_entry(self,title="",author="",date="",link=""):
        self.cur.execute("SELECT * FROM music WHERE (title)=? OR (author)=? OR (date)=? OR (link)=?",(title,author,date,link))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM music WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,date,link):
        self.cur.execute("UPDATE music SET title=?,author=?,date=?,link=? WHERE id=?", (title,author,date,link,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

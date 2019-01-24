import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("Create table if not exists Books(Id integer primary key,Title varchar(20),Auther varchar(20),Year integer,ISBN integer)")
    con.commit()
    con.close()

def Insert(title,auth,year,isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("insert into books values(NULL,?,?,?,?)",(title,auth,year,isbn))
    con.commit()
    con.close()

def Delete(id):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("Delete from books where Id=?",(id,))
    con.commit()
    con.close()

def Update(id,title,auth,year,isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("update books set Title=?,Auther=?,Year=?,ISBN=? where id=?",(title,auth,year,isbn,id))
    con.commit()
    con.close()


def Search(title="",auth="",year="",isbn=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("Select * from books where Title=? OR Auther=? OR Year=? OR ISBN=? ",(title,auth,year,isbn))
    rows=cur.fetchall()
    con.close()
    return rows

def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("Select * from books")
    rows=cur.fetchall()
    con.close()
    return rows

connect()
#print(view())
#Insert("ccc","sss srd",2009,124123)
#Delete(3)
#Update(2,"Cpp","Y.Kanatkar",2010,124124)
#print(view())
#print(Search(year="2008"))

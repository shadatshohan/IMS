import sqlite3
def create_db():
    con=sqlite3.connect(database=r'IMS.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(empid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text, address text, sallary text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS supply(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()
create_db()

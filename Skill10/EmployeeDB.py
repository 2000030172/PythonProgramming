import sqlite3
con=sqlite3.connect("feedback.db")
print("DataBase Opened Successfully..!")
con.execute("create table Feedback(id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT UNIQUE NOT NULL, feedback TEXT "
            "UNIQUE NOT NULL)")
print("Table created Successfully")
con.close()
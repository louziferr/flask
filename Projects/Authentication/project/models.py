# project/models.py
import sqlite3
from flask_login import UserMixin

class Login():
    def __init__(self, db_file):
       self.file = db_file
       con = sqlite3.connect(self.file) 
       cur = con.cursor()
       res = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
       if res.fetchone() is None:
           cur.execute("CREATE TABLE user(email, password, name)")
           con.commit()
           con.close()

    def new_user(self, mail, password, name):
        con = sqlite3.connect(self.file) 
        cur = con.cursor()
        res = cur.execute(f"SELECT email FROM user WHERE email='{mail}'")
        if res.fetchone() is not None:
            con.commit()
            con.close()
            return False
        cur.execute(f"""
                         INSERT INTO user VALUES
                         ('{mail}', '{password}', '{name}')
                         """)
        con.commit()
        con.close()
        return True
    
    def login(self, mail, password):
        con = sqlite3.connect(self.file) 
        cur = con.cursor()
        password_db = ""
        for row in cur.execute(f"SELECT email, password FROM user WHERE email='{mail}'"):
            password_db = row[1]
        con.close()
        return password == password_db
    
class User:
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
    
    def get_id(self):
        return 0
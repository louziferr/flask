import json
import sqlite3

class BankSQL:
    def __init__(self, db_file):
        self.accounts = dict()
        self.file = db_file
        con = sqlite3.connect(self.file) 
        cur = con.cursor()
        res = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bank'")
        if res.fetchone() is None:
            cur.execute("CREATE TABLE bank(account_number, name, balance, type)")
            con.commit()
            con.close()
        self.load_data()

    def new_account(self, account_number, name):
        if len(str(account_number)) != 6:
            raise ValueError(f"Account number must be exactly 6 digits long.")
        self.accounts[account_number] = {"name": name, "balance": 0, "history": []}
        con = sqlite3.connect(self.file) 
        cur = con.cursor()
        res = cur.execute(f"SELECT account_number FROM bank WHERE account_number='{account_number}'")
        if res.fetchone() is not None:
            con.commit()
            con.close()
            return False
        cur.execute(f"""INSERT INTO bank VALUES ('{account_number}', '{name}', 0, 'CREATE')""")
        con.commit()
        con.close()
        return True
    
    def load_data(self):
        con = sqlite3.connect(self.file) 
        cur = con.cursor()
        res = cur.execute(f"SELECT account_number, name, balance FROM bank").fetchall()
        for (acc_num, name, balance) in res:
            self.accounts[acc_num] = {"name": name, "balance": float(balance), "history": []}
        con.close()

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError(f"{account_number} not registered.")
        self.accounts[account_number]["balance"] += float(amount)
        self.accounts[account_number]["history"].append(("deposit", amount))
        self.new_entry(account_number, "DEPOSIT")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError(f"{account_number} not registered.")
        self.accounts[account_number]["balance"] -= float(amount)
        self.accounts[account_number]["history"].append(("withdraw", amount))
        self.new_entry(account_number, "WITHDRAW")

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError(f"{account_number} not registered.")
        return self.accounts[account_number]["balance"]
    
    def get_account_number(self, name):
        for acc_num in self.accounts:
            if self.accounts[acc_num]["name"] == name:
                return acc_num
        return
    
    def new_entry(self, acc_num, type):
        con = sqlite3.connect(self.file) 
        cur = con.cursor()
        balance = self.accounts[acc_num]["balance"]
        name = self.accounts[acc_num]["name"]
        cur.execute(f"""INSERT INTO bank VALUES ('{acc_num}', '{name}', {balance}, '{type}')""")
        con.commit()
        con.close()
        


if __name__ == "__main__":
    bank_sql = BankSQL('bank.db')
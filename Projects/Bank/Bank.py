import json

class Bank:
    def __init__(self):
        self.accounts = dict()

    def new_account(self, account_number, name):
        if len(str(account_number)) != 6:
            raise ValueError(f"Account number must be exactly 6 digits long.")
        self.accounts[account_number] = {"name": name, "balance": 0, "history": []}

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError(f"{account_number} not registered.")
        self.accounts[account_number]["balance"] += float(amount)
        self.accounts[account_number]["history"].append(("deposit", amount))

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError(f"{account_number} not registered.")
        self.accounts[account_number]["balance"] -= float(amount)
        self.accounts[account_number]["history"].append(("withdraw", amount))

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError(f"{account_number} not registered.")
        return self.accounts[account_number]["balance"]
    
    def get_account_number(self, name):
        for acc_num in self.accounts:
            if self.accounts[acc_num]["name"] == name:
                return acc_num
        return
    
    def save(self, filename):
        json_object = json.dumps(self.accounts, indent=4)
        with open(filename, "w") as outfile:
            outfile.write(json_object)

    def load(self, filename):
        with open(filename, "r") as f:
            self.accounts = json.load(f)
from flask import Flask, render_template, request
from Bank import Bank

# the flask app
app = Flask(__name__)

# the bank object
bank = Bank()

bankfile = "bank.json"

bank.load(bankfile)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account', methods=["GET", "POST"])
def account():
    if request.method == "GET":
        return render_template('account.html')
    
    if request.method == "POST":
        account_number = request.form['account_number']
        name = request.form['name']
        bank.new_account(account_number, name)
        bank.save(bankfile)
        return render_template('account.html')
    
@app.route('/accounts', methods=["GET"])
def accounts():
    return render_template('accounts.html', bank=bank)


@app.route('/deposit', methods=["GET", "POST"])
def deposit():
    if request.method == "GET":
        return render_template('deposit.html')
    
    if request.method == "POST":
        account_number = request.form['account_number']
        amount = request.form['amount']
        bank.deposit(account_number, amount)
        bank.save(bankfile)
        return render_template('deposit.html')
    
@app.route('/withdraw', methods=["GET", "POST"])
def withdraw():
    if request.method == "GET":
        return render_template('withdraw.html')
    
    if request.method == "POST":
        account_number = request.form['account_number']
        amount = request.form['amount']
        bank.withdraw(account_number, amount)
        bank.save(bankfile)
        return render_template('withdraw.html')
    
    
@app.route('/history', methods=["GET", "POST"])
def history():
    if request.method == "GET":
        return render_template('history.html', bank=bank, acc_num=0)
    
    if request.method == "POST":
        account_number = request.form['account_number']
        return render_template('history.html', bank=bank, acc_num=account_number)

if __name__ == "__main__":
    app.run()
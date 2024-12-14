from flask import Flask, render_template, request, redirect
import pymysql.cursors
import random

app = Flask(__name__)

# Database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="PASSWORD",
    database="bank_management",
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    account_number = str(random.randint(1000000000, 9999999999))
    contact_no = request.form['contact_no']
    amount = float(request.form['amount'])
    city = request.form['city']
    state = request.form['state']
    pin = request.form['pin']

    if amount >= 1000 and pin.isdigit() and len(pin) == 4:
        query = """
        INSERT INTO customers (account_number, username, contact_no, amount, city, state, pin) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (account_number, username, contact_no, amount, city, state, pin)
        mycursor.execute(query, values)
        connection.commit()
        return render_template('dashboard.html', user={
            'account_number': account_number, 'username': username,
            'contact_no': contact_no, 'amount': amount, 'city': city, 'state': state
        }, message="Account created successfully!")
    else:
        return render_template('index.html', error="Invalid input or minimum amount not met.")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    pin = request.form['pin']
    query = "SELECT * FROM customers WHERE username=%s AND pin=%s"
    mycursor.execute(query, (username, pin))
    result = mycursor.fetchone()
    if result:
        return render_template('dashboard.html', user=result)
    else:
        return render_template('index.html', error="Account not found or incorrect PIN.")

@app.route('/credit', methods=['POST'])
def credit():
    account_number = request.form['account_number']
    amount = float(request.form['amount'])
    query = "UPDATE customers SET amount = amount + %s WHERE account_number=%s"
    mycursor.execute(query, (amount, account_number))
    connection.commit()
    return redirect('/')

@app.route('/debit', methods=['POST'])
def debit():
    account_number = request.form['account_number']
    amount = float(request.form['amount'])
    query = "SELECT amount FROM customers WHERE account_number=%s"
    mycursor.execute(query, (account_number,))
    balance = mycursor.fetchone()['amount']

    if amount <= balance:
        query = "UPDATE customers SET amount = amount - %s WHERE account_number=%s"
        mycursor.execute(query, (amount, account_number))
        connection.commit()
        return redirect('/')
    else:
        return "Insufficient balance!"

@app.route('/delete', methods=['POST'])
def delete():
    account_number = request.form['account_number']
    query = "DELETE FROM customers WHERE account_number=%s"
    mycursor.execute(query, (account_number,))
    connection.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


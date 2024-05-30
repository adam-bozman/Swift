 
from flask import render_template, request, redirect, url_for
from . import create_app, db
from .models import User, Transaction

app = create_app()

@app.route('/')
def index():
    transactions = Transaction.query.all()
    return render_template('index.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    user_id = request.form['user_id']
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    
    new_transaction = Transaction(user_id=user_id, amount=amount, category=category, date=date)
    db.session.add(new_transaction)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

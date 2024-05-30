 
from .models import db, Transaction

def add_transaction(user_id, amount, category, date):
    new_transaction = Transaction(user_id=user_id, amount=amount, category=category, date=date)
    db.session.add(new_transaction)
    db.session.commit()


from .orm import ORM

class Transaction(ORM):
    dbpath = ""
    tablename = "transactions"
    fields = ['user_id', 'ticker_symbol', 'type', 'number_shares']

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.ticker_symbol = kwargs.get('ticker_symbol')
        self.type = kwargs.get('type')
        self.number_shares = kwargs.get('number_shares')

    @classmethod
    def user_transactions(cls, user_id=None):
        if user_id is None:
            return cls.all_from_where_clause()
        else:
            return cls.all_from_where_clause("WHERE user_id=?", (user_id, ))
      

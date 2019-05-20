
from .orm import ORM

class Position(ORM):
    dbpath = ""
    tablename = "positions"
    fields = ['user_id', 'ticker_symbol', 'number_shares', 'price_per_share']

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.ticker_symbol = kwargs.get('ticker_symbol')
        self.number_shares = kwargs.get('number_shares')
        self.price_per_share = kwargs.get('price_per_share')

    @classmethod
    def user_positions(cls, user_id=None):
        if user_id is None:
            return cls.all_from_where_clause()
        else:
            return cls.all_from_where_clause("WHERE user_id=?", (user_id, ))
      
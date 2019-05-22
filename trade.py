import time
from app.util import get_price
from app.orm import ORM

""" Trade is a simple class. It only needs __init__(). The one wrinkle is
self.time should default to time.time() instead of None if its not in kwargs.
"""

class Trade(ORM):

    tablename = 'trades'
    fields = ['accounts_pk', 'ticker', 'volume', 'price', 'time']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.accounts_pk = kwargs.get('accounts_pk')
        self.ticker = kwargs.get('ticker')
        self.volume = kwargs.get('volume')
        self.price = kwargs.get('price')
        self.time = kwargs.get('time')
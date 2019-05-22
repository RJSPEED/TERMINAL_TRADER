import os
import time
from app.orm import ORM
from app import Account, Position, Trade

DIR = os.path.dirname(__file__)
DBFILENAME = 'ttrader.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    
    mike_bloom = Account(username='mike_bloom', balance=10000.00)
    mike_bloom.set_password('password')
    mike_bloom.save()

    # trade for a purchase of 10 shares yesterday
    # trade for a sell of 5 shares today

    tsla_position = Position(ticker='tsla', shares=5, accounts_pk=mike_bloom.pk)
    tsla_position.save()

    ms_position = Position(ticker='ms', shares=10, accounts_pk=mike_bloom.pk)
    ms_position.save()

    tsla_trade = Trade(ticker='tsla', volume=5, price=95.20, time = time.time(), accounts_pk=mike_bloom.pk, )
    tsla_trade.save()

    ms_trade = Trade(ticker='ms', volume=10, price=25.50, time = time.time(), accounts_pk=mike_bloom.pk, )
    ms_trade.save()


    
    
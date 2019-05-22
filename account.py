
import sqlite3
from app.orm import ORM
from app.util import hash_password
from app.position import Position
from app.trade import Trade

class Account(ORM):

    tablename = "accounts"
    fields = ["username", "password_hash", "balance", "api_key"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.balance = kwargs.get('balance')
        self.api_key = kwargs.get('api_key')

    @classmethod
    def login(cls, username, password):
        """ login TODO: check password hash """
        return cls.select_one_where("WHERE username = ? AND password_hash = ?",
                                    (username, hash_password(password)))

    def set_password(self, password):
        self.password_hash = hash_password(password)

    def get_bal(self, username, password):
        cur_balance = Account.select_one_where("WHERE username = ? \
                                                AND password_hash = ?",
                                                (username, hash_password(password)))  
        return (cur_balance.balance, cur_balance.pk)       

    def deposit(self, username, password, deposit_amount):
        cur_balance = Account.select_one_where("WHERE username = ? \
                                                AND password_hash = ?",
                                                (username, hash_password(password)))
        self.pk = cur_balance.pk
        self.username = cur_balance.username
        self.password_hash = cur_balance.password_hash
        self.balance = round(cur_balance.balance + deposit_amount,2)
        self.api_key = cur_balance.api_key
        return round(cur_balance.balance + deposit_amount, 2)

    def get_positions(self):
        return Position.select_many_where("WHERE accounts_pk = ?", (self.pk, ))

    def get_position_for(self, ticker):
        """ return a specific Position object for the user. if the position does not
        exist, return a new Position with zero shares. Returns a Position object """
        position = Position.select_one_where(
            "WHERE ticker = ? AND accounts_pk = ?", (ticker, self.pk))
        if position is None:
            return Position(ticker=ticker, accounts_pk=self.pk, shares=0)
        return position

    def get_trades(self):
        """ return all of the user's trades ordered by time. returns a list of
        Trade objects """
        return Trade.select_many_where("WHERE accounts_pk = ?", (self.pk, ))

    def get_trades_for(self, ticker):
        """ return all of a user's trades for a given ticker """
        trade = Trade.select_one_where(
            "WHERE ticker = ? AND accounts_pk = ?", (ticker, self.pk))
        if trade is None:
            return None #Todo: Info msg stating no trades for that ticker
        return trade

    def buy(self, ticker, amount):
        """ make a purchase. raise KeyError for a non-existent stock and
        ValueError for insufficient funds. will create a new Trade and modify
        a Position and alters the user's balance. returns nothing """
        #Check stock exists and if so retrieve current price
        #Check sufficient funds - retrieve balance from Accounts table and
        #compare against amount*price
        #Insert Trade row
        #Update or insert Position row
        #Update balance on Account row
        pass

    def sell(self, ticker, amount):
        """ make a sale. raise KeyErrror for a non-existent stock and
        ValueError for insufficient shares. will create a new Trade object,
        modify a Position, and alter the self.balance. returns nothing."""
        #Check stock exists in Positions table and if shares => amount
        #Retieve current price
        #Insert Trade row
        #Update Position row
        #Update balance on Account row
        
        pass

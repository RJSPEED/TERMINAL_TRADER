import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'terminal_trader.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS users;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE users (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            balance FLOAT,
            login_name TEXT,
            login_id TEXT
        ); """
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS positions;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE positions (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            ticker_symbol TEXT,
            number_shares INTEGER,
            price_per_share FLOAT
        ); """
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS transactions;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE transactions (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            ticker_symbol TEXT,
            type BOOLEAN,
            number_shares INTEGER
        ); """
        cur.execute(SQL)        


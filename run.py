#! /usr/bin/env python3

from app.users import User

from app import controller
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'terminal_trader.db')

User.dbpath = DBPATH
#controller.run()

me = User(name = "Richard Speed", age = 48, email = "RJSPEED@ICLOUD.COM", \
          balance = 250.00, login_name = "speedr", login_id = "password16" )
al = User(name = "Alistair Fraser", age = 43, email = "AFRASER@ICLOUD.COM", \
          balance = 950.00, login_name = "frazzle", login_id = "password17" )
hamo = User(name = "Steven Hamilton", age = 44, email = "HAMO@ICLOUD.COM", \
          balance = 550.00, login_name = "hamo", login_id = "password18" )
hemel = User(name = "Stuart Head", age = 45, email = "HEMEL@ICLOUD.COM", \
          balance = 650.00, login_name = "hemel", login_id = "password19" )
hygers = User(name = "Simon Hygate", age = 45, email = "HYGERS@ICLOUD.COM", \
          balance = 750.00, login_name = "hygers", login_id = "password20" )

al._insert()
hamo._insert()
hemel._insert()
hygers._insert()


User.one_from_where_clause("login_name", "speedr")

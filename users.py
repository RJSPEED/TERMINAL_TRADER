
from .orm import ORM

class User(ORM):
    dbpath = ""
    tablename = "users"
    fields = ['pk', 'name', 'age', 'email', 'balance', 'login_name', 'login_id']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.email = kwargs.get('email')
        self.balance = kwargs.get('balance')
        self.login_name = kwargs.get('login_name')      
        self.login_id = kwargs.get('login_id')
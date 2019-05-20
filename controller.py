from app import views
from app.users import User
from app.positions import Position
from app.transactions import Transaction

def user_login():
    #Request login_name and login_id
    login_name = views.login("Login Name")
    login_id = views.login("Login Id")
    #Validate and return boolean
    
def main_loop():
    if not user_login():
        while True:
            choice = views.main_menu()
            if choice is None:
                views.bad_input()
            elif choice == 5:
                views.goodbye()
                break
            elif choice == 1:
                #Lookup ticker symbol from company name
            elif choice == 2:
                #Quote
            elif choice == 3:
                #Buy
            elif choice == 4:
                #Sell
    else:
        views.goodbye()
        break
   
def run():
    main_loop()

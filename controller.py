from app.account import Account
from app import views
from app import util

def main():
    while True:
        selection = views.welcome_menu()
        if selection is None:
            #Bad input
            views.generic_msg("Please enter a number that corresponds to a stated option")
        elif selection == 3:
            #Exit
            views.generic_msg("Bye: Thanks for using Terminal Trader")
            break
        elif selection == 1:
            #Create account
            new_username = views.get_input("Username")
            new_password = views.get_input("Password")            
            new_account = Account(username=new_username)
            new_account.set_password(new_password)
            new_account.save()
        elif selection == 2:
            #Login
            login_username = views.get_input("Username")
            login_password = views.get_input("Password")      
            if not Account.login(login_username, login_password):
                views.generic_msg("Failed to find an account for the given Username/Password, pls retry")
            else:
                #Retrieve account balance & pk for re-use 
                balance = Account()
                current_bal, pk = balance.get_bal(login_username, login_password)
                while True:
                    choice = views.main_menu()
                    if choice is None:
                        #Bad input
                        views.generic_msg("Please enter a number that corresponds to a stated option")
                    elif choice == 7:
                        #Exit
                        break
                    elif choice == 1: #View Balance & Positions
                        views.generic_msg("Your current balance = {}".format(current_bal))
                        while True:
                            position_choice = views.position_menu()    
                            if position_choice is None:
                                #Bad input
                                views.generic_msg("Please enter a number that corresponds to a stated option")
                            elif position_choice == 3:
                                #Exit
                                break
                            elif position_choice == 1:
                                #Retrieve and display a given position, taking in a ticker symbol
                                ticker = views.get_input("Please enter a Ticker Symbol")
                                user_position = Account(pk=pk)
                                position = user_position.get_position_for(ticker)
                                views.show_positions(position)
                            elif position_choice == 2:
                                #Retrieve and display all positions
                                user_positions = Account(pk=pk)
                                positions = user_positions.get_positions()
                                for position in positions:
                                    views.show_positions(position)
                    elif choice == 2: #Deposit money
                        deposit_amount = float(views.get_input("Deposit Amount"))
                        account_deposit = Account()
                        new_bal = account_deposit.deposit(login_username, login_password, deposit_amount)
                        account_deposit.save()
                        views.generic_msg("New Balance = {}".format(new_bal))
                    elif choice == 3: #Look up stock price
                        ticker = views.get_input("Please enter a Ticker Symbol")
                        print(util.get_price(ticker))
                    elif choice == 4: #Buy stock
                        ticker = views.get_input("Please enter a Ticker Symbol")
                        shares_buy = views.get_input("Please enter the number of shares to buy")

                    elif choice == 5: #Sell stock
                        ticker = views.get_input("Please enter a Ticker Symbol")
                        shares_sell = views.get_input("Please enter the number of shares to sell")
                    elif choice == 6: #View Trade History
                        while True:
                            trade_choice = views.trades_menu()    
                            if trade_choice is None:
                                #Bad input
                                views.generic_msg("Please enter a number that corresponds to a stated option")
                            elif trade_choice == 3:
                                #Exit
                                break
                            elif trade_choice == 1:
                                #Retrieve and display trades re a give ticker symbol
                                ticker = views.get_input("Please enter a Ticker Symbol")
                                user_trade = Account(pk=pk)
                                trades = user_trade.get_trades_for(ticker)
                                views.show_trades(trades)
                            elif trade_choice == 2:
                                #Retrieve and display all trades
                                user_trades = Account(pk=pk)
                                trades = user_trades.get_trades()
                                for trade in trades:
                                    views.show_trades(trade)    
                        

def run():
    main()



"""
Sample execution

Welcome to Terminal Trader!
    
    1. create account
    2. login
    3. quit

Your choice: 2.


Main Menu:

    1. see balance & positions  
    2. deposit money  
    3. look up stock price
    4. buy stock
    5. sell stock
    6. trade history

etc.


you should have useful output if a user inputs a stock that does not exist

you should not allow a user to spend money they don't have or sell
shares they don't have

your display of positions or trades should be well-formatted, don't
just print a python list
"""

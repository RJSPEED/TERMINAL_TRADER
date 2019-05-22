import os

def get_input(param):
    print()
    print(param, " : ", end="")
    return input()

def generic_msg(param):
    print()
    print(param)
    print()

def show_positions(position):
    print()
    print("Ticker Symbol: {}, Shares: {}".format(position.ticker, position.shares))

def show_trades(trade):
    print()
    print("Time: {}, Ticker Symbol: {}, No. of Shares: {}, Price per Share: {}". \
          format(trade.time, trade.ticker, trade.volume, trade.price))


def welcome_menu():
    print()
    print("Welcome to Terminal Trader !")
    print()
    print("1. Create Account")
    print()
    print("2. Login")
    print()
    print("3. Quit")
    print()
    
    selection = input().strip()
    try:
        selectionnum = int(selection)
    except ValueError:
        return None
    return selectionnum

def main_menu():
    print()
    print("1. View Balance & Positions")
    print()
    print("2. Deposit Money")
    print()
    print("3. Lookup Stock Price")
    print()
    print("4. Buy Stock")
    print()
    print("5. Sell Stock")
    print()
    print("6. View Trade History")
    print()
    print("7. Exit")
    print()

    selection = input().strip()
    try:
        selectionnum = int(selection)
    except ValueError:
        return None
    return selectionnum

def position_menu():
    print()
    print("1. View position for a single stock")
    print()
    print("2. View all positions")
    print()
    print("3. Exit")
    print()
    
    pos_selection = input().strip()
    try:
        pos_selectionnum = int(pos_selection)
    except ValueError:
        return None
    return pos_selectionnum

def trades_menu():
    print()
    print("1. View trades for a single stock")
    print()
    print("2. View all trades")
    print()
    print("3. Exit")
    print()
    
    pos_selection = input().strip()
    try:
        pos_selectionnum = int(pos_selection)
    except ValueError:
        return None
    return pos_selectionnum
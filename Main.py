"""This game will generate random stock conditions and prompt the user to buy or sell.  The goal
of the game is to accumulate the highest score possible by timing purchases and sales.
"""

import random

# ---------- Pseudocode ----------

# Randomly generate a set of stocks and their prices

# Set initial value of user's cash on hand

# Prompt user to buy, sell, hold, or inspect their holdings

# If the user selects buy, prompt them for the stock to buy and for how much

# Validate inputs for existing stock tickers and to limit upper thresholds not to exceed balance

# ELSE IF user selects sell, validate for existing holdings and show them, then prompt which to sell

# Validate for a nonzero quantity and add the balance of proceeds to their account

# Repeat loop


# ---------- Main Code ----------

# User data
cash_balance = 5000
holdings = []
# Holdings will be dictionaries to include {"ticker": "", "shares": 0, "price": 0}
portfolio_value = 0

global_turn_counter = 0

global_stocks = [
    {"ticker": "AAA", "price": 10, "volatility": 1.8},
    {"ticker": "BBB", "price": 20, "volatility": 1.7},
    {"ticker": "CCC", "price": 30, "volatility": 1.6},
    {"ticker": "DDD", "price": 40, "volatility": 1.5},
    {"ticker": "EEE", "price": 50, "volatility": 1.4},
    {"ticker": "FFF", "price": 60, "volatility": 1.3},
    {"ticker": "GGG", "price": 70, "volatility": 1.2},
    {"ticker": "HHH", "price": 80, "volatility": 1.1},
    {"ticker": "III", "price": 90, "volatility": 1}
]

# TODO: Randomly seed the initial prices and volatilities with new starting values for each game

def prompt_user():
    # Do things
    choosing = True
    
    while choosing:
        prompt = "\nType which action you would like to perform: \n _ _ Buy _ _ _ Sell _ _ _ Wait _ _ _ Holdings _ _ _ Quit _ _"
        print(prompt+"\n")
        # Check for a valid input
        user_choice = input()
        if (user_choice.title() == "Buy"):
            print("Choose a stock to buy")
            choosing = False
            
        elif (user_choice.title() == "Sell"):
            print("Choose a holding to sell")
            choosing = False
        
        elif (user_choice.title() == "Wait"):
            print("No action taken.  Progressing to the next trading day...")
            choosing = False
            
        elif (user_choice.title() == "Holdings"):
            print("Showing your current holdings...")
            choosing = False
            
        elif (user_choice.title() == "Quit"):
            print("Cashing out holdings.  Your final score is xyz.")
            
        else:
            print("Not a valid choice.\n")
        
    
    
def adjust_balance():
    print("New balance")
    
    
def buy_stock(stock):
    print("Bought "+stock)
    
    
def sell_stock(stock):
    print("sold "+stock)
    

def change_prices(days=1):
    for iteration in range(days):
        print("\nnew trading day")
        print("iteration "+str(iteration)+"...")
        for stock in global_stocks:
            move_direction = random.choice(["Up", "Down"])
            # Adjust the stock price by a maximum of 20% multiplied by the volatility and round to 2 places
            move_amount = round(random.uniform(0, (stock["price"] * 0.2) * stock["volatility"]), 2)
            if (move_direction == "Up"):
                stock["price"] += round(move_amount, 2)
            else:
                stock["price"] -= round(move_amount, 2)
            
            print("Adjusting "+stock["ticker"]+" "+move_direction+" by $"+str(move_amount)+" to $"+str(round(stock["price"], 2)))
        
        print(global_stocks)
    
# ---------- Testbed ----------

change_prices(5)
    
    

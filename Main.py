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
            
            # Validate another input to decide which stock to buy, or back out to the prior loop
            
            # Ensure the stock is a valid choice, and then prompt for the number of shares
            
            # The number of shares must be a positive nonzero integer and cannot contain other chars.
            
            # Validate whether the user has enough cash on hand to make that purchase
            
        elif (user_choice.title() == "Sell"):
            print("Choose a holding to sell")
            choosing = False
            
            # Validate that the choice is contained in the user's holdings
            
            # Prompt for a number of shares to sell at the market price
            
            # Validate that the input was a nonzero integer and did not contain disallowed chars
            
            # Cast to int
            
            # Validate that the user has at least that number of shares
            
            # Package the validated input and send as an argument to the sell_stock() function
        
        elif (user_choice.title() == "Wait"):
            print("No action taken.  Progressing to the next trading day...")
            choosing = False
            
            # Call the change_prices() function and return the prompt recursively
            change_prices()
            prompt_user()
            
        elif (user_choice.title() == "Holdings"):
            print("Showing your current holdings...")
            print(holdings)            
            
        elif (user_choice.title() == "Quit"):
            score = calculate_portfolio_value()
            print("Cashing out holdings.  Your final score is $"+score)
            
        else:
            print("Not a valid choice.\n")
        


def calculate_portfolio_value():
    sum_total = 0
    for holding in holdings:
        sum_total += (holding["price"] * holding["shares"])

    # print("Portfolio value: $"+str(sum_total))
    sum_total += cash_balance
    return sum_total

    
def adjust_balance():
    print("Beginning balance: "+str(calculate_portfolio_value()))
    # Find which holdings the player has
    
    # Find the matching holdings in the global_stocks array
    
    # Grab the prices for those stocks and use them to update the prices (but not shares) of the holdings
    
    # Return the updated calculate_portfolio_value() function result
    
    
def buy_stock(ticker, shares, price):
    # NOTE: This function will not handle prompts.  It is simply called once validation of eligible
    # purchase and quantity have been validated
    print("\nBuying "+str(shares)+" shares of "+ticker+" at $"+str(price)+"...")
    
    # Check to see whether the stock is in the player's holdings
    global cash_balance
    
    for item in holdings:
        if (ticker in item["ticker"]):
            print("You own "+str(item["shares"])+" shares of this stock.")
            item["shares"] += shares
            print("Added "+str(shares)+".  New shares = "+str(item["shares"]))
            cash_balance -= (price * shares)
            print("New cash balance: $"+str(cash_balance))
            return        
        
    print("New stock.")
    holdings.append({"ticker": ticker, "shares": shares, "price": price})
    cash_balance -= (price * shares)
    print("New cash balance: $"+str(cash_balance))
    
    
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

holdings.append({"ticker": "BBB", "shares": 5, "price": 55.27})
print(holdings)
buy_stock("BBB", 1, 100)
    

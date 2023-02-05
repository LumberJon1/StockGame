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
holdings = []
# Holdings will be dictionaries to include {"ticker": "", "shares": 0, "price": 0}
cash_balance = 5000
investments_value = 0
portfolio_value = 0

# Other Globals
global_turn_counter = 0

global_trend = 0.6

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

# TODO: Add arrays to track historical data so it can be charted and displayed
# Historical data will be an array of values ordered [cash balance, investment balance, total value]
historical_data = []

# Historical prices will be an array of solely the prices of each stock in order
historical_prices = []


# TODO: Randomly seed the initial prices and volatilities with new starting values for each game
def seed_start():
    for stock in global_stocks:
        stock["price"] = round(random.uniform(0, 100), 2)
        stock["volatility"] = round(random.uniform(0.1, 3.6), 1)

def prompt_user():
    # Do things
    choosing = True
    
    while choosing:
        prompt = "\nType which action you would like to perform: \n _ _ Buy _ _ _ Sell _ _ _ Wait _ _ _ Holdings _ _ _ Prices _ _ _ Quit _ _"
        print(prompt+"\n")
        # Check for a valid input
        user_choice = input()
        if (user_choice.title() == "Buy"):
            print("Choose a stock to buy")
            choosing = False
            
            # Validate another input to decide which stock to buy, or back out to the prior loop
            print("\nNow in the choice loop")
            
            choosing_stock = True
            while choosing_stock:
                valid_tickers = []
                print("\nType one of the tickers to buy.  Type \"Back\" to go back.")
                for stock in global_stocks:
                    print(stock["ticker"]+": $"+str(stock["price"]))
                    valid_tickers.append(stock["ticker"])
                print("\n")
                
                ticker_choice = input()
                if (ticker_choice.title() == "Back"):
                    choosing_stock = False
                    prompt_user()
                    
                elif ticker_choice.upper() in valid_tickers:
                    
                    # Enter into quantity loop
                    selecting_quantity = True
                    while selecting_quantity:
                        global cash_balance
                        
                        print("\nChose "+ticker_choice.upper())
                        print("\nChoose number of shares to buy.")
                        
                        current_price = 0
                        for stock in global_stocks:
                            if (ticker_choice.upper() == stock["ticker"]):
                                current_price = stock["price"]
                        print("\nPurchase price: $"+str(round(current_price, 2)))
                        print("\n(cash available: $"+str(cash_balance)+")")
                        
                        quantity_choice = input()
                        # Check that the input quantity of shares is a positive integer > 0
                        if (int(quantity_choice) > 0) and (float(quantity_choice).is_integer()):
                            if (int(quantity_choice) * current_price <= cash_balance):
                                buy_stock(ticker_choice.upper(), quantity_choice, current_price)
                                
                                # Progress the prices and run the main prompt again
                                selecting_quantity = False
                                choosing_stock = False
                                change_prices()
                                prompt_user()
                            else:
                                print("\n"+quantity_choice+" shares at $"+str(current_price)+" exceeds cash balance of $"+str(round(cash_balance, 2)))
                        else:
                            print("\n"+quantity_choice+" is not a valid quantity of shares.")
                            print("Enter a nonzero whole integer (i.e. 5, not 5.1)")
                else:
                    print("\nPlease type a valid ticker symbol.")                    

            
        elif (user_choice.title() == "Sell"):
            print("Choose a holding to sell")
            choosing = False
            
            # Array to hold useful info like available tickers and related prices and shares
            available_tickers = []
            available_shares = []
            available_prices = []
            
            for stock in holdings:
                print(" _ _ "+stock["ticker"]+" _ ", end=" ")
                available_tickers.append(stock["ticker"])
                available_shares.append(stock["shares"])
                available_prices.append(stock["price"])
            
            # Validate that the choice is contained in the user's holdings
            selling = True
            while selling:
                
                user_choice = input()
                if (user_choice.upper() not in available_tickers):
                    print("\nPlease choose a valid holding to sell.")
                    
                else:
                    choice_index = available_tickers.index(user_choice.upper())
                    print("You chose to sell "+user_choice.upper())
                    
                    # Prompt for a number of shares to sell at the market price
                    choosing_quantity_sold = True
                    while choosing_quantity_sold:
                        print("\nYou have "+str(available_shares[choice_index])+" shares of "+user_choice.upper()+" available to sell at $"+str(available_prices[choice_index])+" per share.")
                        print("\nChoose a number of shares to sell (in whole share quantities)")
                        quantity_choice = input()
                        if (float(quantity_choice).is_integer()):
                            if (int(quantity_choice) > 0 and int(quantity_choice) <= available_shares[choice_index]):
                                # Validate for a non-negative, non-zero integer in whole shares
                                    # Subtract the shares and add the proceeds to the balance of cash, then exit the loops
                                    sale_total = 0
                                    for item in holdings:
                                        if (item["ticker"] == user_choice.upper()):
                                            item["shares"] -= int(quantity_choice)
                                            sale_total = int(quantity_choice) * item["price"]
                                            cash_balance += sale_total
                                            
                                    # Display sales proceeds and updated balance
                                    print("\nYou sold "+quantity_choice+" shares for total proceeds of $"+str(sale_total)+".")
                                    selling = False
                                    choosing_quantity_sold = False
                                    choosing = True
                                    break                                
                            else:
                                print(str(quantity_choice)+" is not a valid quantity of shares.")
                        else:
                            print("\nPlease select a share quantity in whole shares.")
                                
        
        elif (user_choice.title() == "Wait"):
            print("No action taken.  Progressing to the next trading day...")
            choosing = False
            
            # Call the change_prices() function and return the prompt recursively
            change_prices()
            prompt_user()
            
        elif (user_choice.title() == "Holdings"):
            print("\nYour portfolio has the following assets:")
            
            # variable to store portfolio balance
            portfolio_total = 0
            
            for stock in holdings:
                print(stock["ticker"]+": "+str(stock["shares"])+" shares at $"+str(stock["price"]))
                portfolio_total += (stock["price"] * int(stock["shares"]))

            print("\nTotal invested balance: $"+str(portfolio_total))
            print("You also have an uninvested cash balance remaining of $"+str(cash_balance))
            
            print("\nYour total portfolio value is $"+str(calculate_portfolio_value()))
            
        elif (user_choice.title() == "Prices"):
            for stock in global_stocks:
                print(stock["ticker"]+" $"+str(stock["price"])+"  \u03C3 "+str(stock["volatility"]))
                print("----------------")
                
                # TODO: Show direction of movement since last price
            
        elif (user_choice.title() == "Quit"):
            score = calculate_portfolio_value()
            print("Cashing out holdings.  Your final score is $"+str(score))
            
        else:
            print("Not a valid choice.\n")
        


def calculate_portfolio_value():
    sum_total = 0
    for holding in holdings:
        sum_total += (float(holding["price"]) * holding["shares"])

    # print("Portfolio value: $"+str(sum_total))
    investments_value = sum_total
    sum_total += cash_balance
    portfolio_value = sum_total
    return sum_total

    
def adjust_balance():
    print("Beginning balance: "+str(calculate_portfolio_value()))
    # Find which holdings the player has
    
    inv_total = 0
    
    for stock in global_stocks:
        for holding in holdings:
        # Find the matching holdings in the global_stocks array
            if (stock["ticker"] == holding["ticker"]):
                holding["price"] = stock["price"]
                investment_value = holding["price"] * holding["shares"]
                print("total value of holding "+holding["ticker"]+": $"+str(investment_value)+" ("+str(holding["shares"])+" shares at $"+str(round(holding["price"], 2)))
                inv_total += investment_value
                
    # Store the summed totals of portfolio investments to add to investments_value
    print("investments total value: $"+str(round(inv_total, 2)))
    investments_value = inv_total
    print("Cash balance: $"+str(round(cash_balance, 2)))
    portfolio_value = cash_balance + investments_value
    print("Total portfolio value: $"+str(round(portfolio_value, 2)))
                
    # Push the updated balances to the global array of historical data
    historical_data.append([cash_balance, investments_value, portfolio_value])

    
    
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
    holdings.append({"ticker": ticker, "shares": int(shares), "price": float(round(price, 2))})
    cash_balance -= (price * int(shares))
    print("New cash balance: $"+str(cash_balance))
    
    
def sell_stock(ticker, shares, price):
    # This function will assume that the arguments have been validated.
    
    global cash_balance
    price = 0
    
    for item in holdings:
        if (ticker in item["ticker"]):
            item["shares"] -= shares
            
    # Determine appropriate proceeds
    for stock in global_stocks:
        if (stock["ticker"] == ticker):
            price = stock["price"]
            
    # Add the proceeds to the cash balance
    cash_balance += (price * shares)
    print("sold "+stock)
    

def change_prices(days=1):
    for iteration in range(days):
        print("\nnew trading day")
        print("iteration "+str(iteration)+"...")
        
        # Local array to push to the global historical prices array once done
        local_prices = []
        
        for stock in global_stocks:
            # Take the global trend value and use it to determine movement direction
            global global_trend
            move_direction = random.uniform(0, 1)
            if (move_direction < global_trend):
                move_direction = "Up"
            else:
                move_direction = "Down"
            # Adjust the stock price by a maximum of 20% multiplied by the volatility and round to 2 places
            move_amount = round(random.uniform(0, ((stock["price"] * 0.2) * stock["volatility"])), 2)
            if (move_direction == "Up"):
                stock["price"] += round(move_amount, 2)
            else:
                stock["price"] -= round(move_amount, 2)
            
            # Append the stock price to the local prices array so it can be then sent to the global historical prices array
            local_prices.append(round(stock["price"], 2))
        
        # Adjust the player's portfolio balance with the updated prices
        adjust_balance()
        
        for stock in global_stocks:
            print(stock["ticker"]+": $"+str(round(stock["price"], 2))+"  - Volatility: "+str(stock["volatility"]))
            
        # Push to global historical prices
        historical_prices.append(local_prices)
    
# ---------- Testbed ----------

seed_start()
prompt_user()
    

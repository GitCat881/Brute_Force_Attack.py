# Variable initialization
product_price = 50  
stock_count = 10
discount_threshold = 5
discount_rate = 0.10

# Function to calculate the total price
def calculate_total_price(quantity):
        while True:
            if quantity <= 0:
                print("Quantity should be more than zero")
            else:
                return  int(product_price * quantity)
            if quantity > discount_threshold:
                return int((product_price * quantity) * (1 - discount_rate))
            else:
                return int(product_price * quantity)

#quantity function
def is_quantity(Q):
    while True:
        quantity = input(Q)
        if quantity.isdigit():
            return int(quantity)
        else:
            print("ERROR")

# Main store management function
def store_manager():
    print("Welcome to the store!")
    print("Each product costs:", product_price, "dollars")
    quantity = is_quantity("Enter quantity to buy: ")
    while True:
        if quantity > stock_count:
            print("Error: Not enough stock")
            return
        else:
            total_price = calculate_total_price
            print("Total price is:", total_price)
            Stock_count = stock_count - quantity 
            print("Stock remaining:", Stock_count)
            return 

# Continue_shopping function
def is_continue_shopping(text):
    while True:
        continue_shopping = input(text)
        if continue_shopping == "yes":
            print("let's go back to the store\n") 
            return store_manager()
        elif continue_shopping == "no":
            break
        else:
            print("Invalid response. Please type 'yes' or 'no'.")

# Loop to keep the store open
store_manager()
while True:
        continue_shopping = is_continue_shopping("Continue shopping? (yes/no): ").lower()
        break
print("Thanks for visiting!")

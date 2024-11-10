# Online Food Ordering System with Payment Method Selection

# Sample menu
menu = {
    1: {"name": "Veg Tikka Pizza", "price": 174},
    2: {"name": "Double Cheese Chicken Pizza", "price": 254},
    3: {"name": "Fries N Chicken", "price": 155},
    4: {"name": "Corn Pasta", "price": 155},
    5: {"name": "Fried Chicken Cheese Burger", "price": 80},
    6: {"name": "Chill Cheese Pasta", "price": 155},
    7: {"name": "Blue Mint Mojito", "price": 112},
    8: {"name": "Classic Virgin Mojito", "price": 80},
    9: {"name": "Fresh Lime with Litchi", "price": 64},
    10: {"name": "Vanilla Thick Shake", "price": 128}
    
}
# Function to display the menu
def display_menu():
    print("\n-----Welcome to the Online Food Ordering System-----")
    print("Here's our menu:")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ${item['price']:.2f}")
    print()

# Function to take the user's order
def take_order():
    order = []
    total_price = 0.0

    while True:
        try:
            item_id = int(input("Enter the item number to order (0 to finish): "))
            if item_id == 0:
                break
            elif item_id in menu:
                quantity = int(input(f"How many {menu[item_id]['name']}s would you like to order? "))
                order.append((menu[item_id]['name'], quantity, menu[item_id]['price'], quantity * menu[item_id]['price']))
                total_price += quantity * menu[item_id]['price']
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return order, total_price

# Function to display the order summary
def display_order_summary(order, total_price):
    if len(order) > 0:
        print("\nYour Order Summary:")
        for item in order:
            print(f"{item[1]} x {item[0]} - ${item[3]:.2f}")
        print(f"\nTotal Price: ${total_price:.2f}")
    else:
        print("No items ordered.")

# Function to select and process payment
def process_payment(total_price):
    while True:
        print("\nPayment Methods:")
        print("1. Cash")
        print("2. Credit/Debit Card")
        payment_method = input("Select your payment method (1 or 2): ")
        
        if payment_method == '1':
            try:
                payment = float(input(f"Your total is ${total_price:.2f}. Enter cash amount: $"))
                if payment >= total_price:
                    change = payment - total_price
                    print(f"Payment successful with Cash! Your change is: ${change:.2f}")
                    break
                else:
                    print("Insufficient cash. Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif payment_method == '2':
            try:
                card_number = input("Enter your credit/debit card number: ")
                if len(card_number) == 16 and card_number.isdigit():
                    print(f"Payment successful with Credit/Debit Card ending in {card_number[-4:]}!")
                    break
                else:
                    print("Invalid card number. Please enter a valid 16-digit card number.")
            except ValueError:
                print("Invalid input. Please enter a valid card number.")
        
        else:
            print("Invalid option. Please select 1 for Cash or 2 for Credit/Debit Card.")

# Main function to run the program
def main():
    display_menu()
    order, total_price = take_order()
    display_order_summary(order, total_price)
    if total_price > 0:
        process_payment(total_price)
    else:
        print("No order was placed.")

# Run the program
if __name__ == "__main__":
    main()

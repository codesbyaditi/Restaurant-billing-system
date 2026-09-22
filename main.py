# Restaurant Billing System
# B.Tech 1st Year Python Project

# Restaurant Menu
menu = {
    1: ["Burger", 120],
    2: ["Pizza", 250],
    3: ["Pasta", 180],
    4: ["Sandwich", 100],
    5: ["French Fries", 80],
    6: ["Cold Drink", 50],
    7: ["Coffee", 60],
    8: ["Ice Cream", 90]
}


def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    print("Item No.    Item Name          Price")
    print("-------------------------------------")

    for number, item in menu.items():
        print(f"{number:<11}{item[0]:<19}₹{item[1]}")

    print("=====================================")


def generate_bill(order):
    print("\n\n========== FINAL BILL ==========")
    print(f"{'Item':<20}{'Qty':<8}{'Price':<10}{'Amount':<10}")
    print("-----------------------------------------------")

    subtotal = 0

    for item_name, quantity, price in order:
        amount = quantity * price
        subtotal += amount

        print(f"{item_name:<20}{quantity:<8}₹{price:<9}₹{amount:<10}")

    # GST calculation
    gst = subtotal * 0.05
    total = subtotal + gst

    print("-----------------------------------------------")
    print(f"{'Subtotal':<30}₹{subtotal:.2f}")
    print(f"{'GST (5%)':<30}₹{gst:.2f}")
    print(f"{'Total Bill':<30}₹{total:.2f}")
    print("===============================================")
    print("       Thank you for visiting!")
    print("===============================================")


def restaurant_billing():
    order = []

    print("=====================================")
    print("       WELCOME TO OUR RESTAURANT")
    print("=====================================")

    while True:
        display_menu()

        choice = int(input("\nEnter item number (0 to finish): "))

        if choice == 0:
            break

        if choice not in menu:
            print("Invalid item number! Please try again.")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        item_name = menu[choice][0]
        price = menu[choice][1]

        order.append([item_name, quantity, price])

        print(f"{quantity} x {item_name} added to your order.")

    if len(order) == 0:
        print("\nNo items ordered.")
    else:
        generate_bill(order)


# Start the program
restaurant_billing()
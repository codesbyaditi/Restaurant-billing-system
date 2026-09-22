# ============================================================
#          RESTAURANT BILLING SYSTEM
#          B.Tech 1st Year Python Project
# ============================================================

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


# ------------------------------------------------------------
# Function to display menu
# ------------------------------------------------------------
def display_menu():
    print("\n" + "=" * 45)
    print("              RESTAURANT MENU")
    print("=" * 45)
    print(f"{'No.':<8}{'Item Name':<22}{'Price':>10}")
    print("-" * 45)

    for number, item in menu.items():
        print(f"{number:<8}{item[0]:<22}₹{item[1]:>8}")

    print("=" * 45)


# ------------------------------------------------------------
# Function to generate final bill
# ------------------------------------------------------------
def generate_bill(order, customer_name, bill_number):

    subtotal = 0

    print("\n\n")
    print("=" * 65)
    print("                    FINAL BILL")
    print("=" * 65)

    print(f"Customer Name : {customer_name}")
    print(f"Bill Number   : {bill_number}")

    print("-" * 65)
    print(f"{'Item':<20}{'Qty':<8}{'Price':<12}{'Amount':>12}")
    print("-" * 65)

    # Display ordered items
    for item_name, quantity, price in order:

        amount = quantity * price
        subtotal += amount

        print(
            f"{item_name:<20}"
            f"{quantity:<8}"
            f"₹{price:<11.2f}"
            f"₹{amount:>10.2f}"
        )

    print("-" * 65)

    # --------------------------------------------------------
    # Discount calculation
    # --------------------------------------------------------

    if subtotal >= 500:
        discount_rate = 0.10
    else:
        discount_rate = 0.00

    discount = subtotal * discount_rate

    # Amount after discount
    amount_after_discount = subtotal - discount

    # --------------------------------------------------------
    # GST calculation
    # --------------------------------------------------------

    gst_rate = 0.05
    gst = amount_after_discount * gst_rate

    # Final amount
    total = amount_after_discount + gst

    # --------------------------------------------------------
    # Display bill summary
    # --------------------------------------------------------

    print(f"{'Subtotal':<45}₹{subtotal:>10.2f}")
    print(f"{'Discount (10%)':<45}₹{discount:>10.2f}")
    print(f"{'Amount After Discount':<45}₹{amount_after_discount:>10.2f}")
    print(f"{'GST (5%)':<45}₹{gst:>10.2f}")
    print("=" * 65)
    print(f"{'TOTAL BILL':<45}₹{total:>10.2f}")
    print("=" * 65)

    if discount > 0:
        print("Congratulations! You received a 10% discount.")
    else:
        print("Add items worth ₹500 or more to get a 10% discount.")

    print("\n          Thank you for visiting!")
    print("             Please visit again!")
    print("=" * 65)


# ------------------------------------------------------------
# Main Restaurant Billing Function
# ------------------------------------------------------------
def restaurant_billing():

    order = []

    print("=" * 45)
    print("       WELCOME TO OUR RESTAURANT")
    print("=" * 45)

    # Customer name
    customer_name = input("Enter customer name: ")

    # Bill number
    bill_number = 1001

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter item number (0 to finish): "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Finish ordering
        if choice == 0:
            break

        # Check item number
        if choice not in menu:
            print("Invalid item number! Please try again.")
            continue

        # Get quantity
        try:
            quantity = int(input("Enter quantity: "))

        except ValueError:
            print("Please enter a valid quantity.")
            continue

        # Check quantity
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        # Get item information
        item_name = menu[choice][0]
        price = menu[choice][1]

        # Add item to order
        order.append([item_name, quantity, price])

        print(f"\n✓ {quantity} x {item_name} added to your order.")

    # --------------------------------------------------------
    # Generate bill
    # --------------------------------------------------------

    if len(order) == 0:

        print("\nNo items were ordered.")
        print("Thank you for visiting!")

    else:

        generate_bill(order, customer_name, bill_number)


# ------------------------------------------------------------
# Start Program
# ------------------------------------------------------------

restaurant_billing()
# Restaurant Billing System

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

print("===== RESTAURANT BILLING SYSTEM =====")
name = input("Enter customer name: ")

# Show menu
print("\n----- MENU -----")
for n, item in menu.items():
    print(n, item[0], "₹", item[1])

total = 0

# Take order
while True:
    choice = int(input("\nEnter item number (0 to finish): "))

    if choice == 0:
        break

    if choice in menu:
        qty = int(input("Enter quantity: "))
        total += menu[choice][1] * qty
        print(menu[choice][0], "added.")
    else:
        print("Invalid item!")

# Calculate discount and GST
discount = total * 10 / 100 if total >= 500 else 0
gst = (total - discount) * 5 / 100
final_bill = total - discount + gst

# Print bill
print("\n========== BILL ==========")
print("Customer:", name)
print("Subtotal: ₹", total)
print("Discount: ₹", discount)
print("GST: ₹", gst)
print("Final Bill: ₹", final_bill)
print("==========================")
print("Thank you for visiting!")
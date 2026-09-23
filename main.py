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

print("\n--------- MENU ---------")
for no, item in menu.items():
    print(no, item[0], "₹", item[1])

total = 0

while True:
    choice = int(input("\nEnter item number (0 to finish): "))

    if choice == 0:
        break

    if choice in menu:
        qty = int(input("Enter quantity: "))

        item_name = menu[choice][0]
        price = menu[choice][1]

        amount = price * qty
        total = total + amount

        print(qty, item_name, "added.")
    else:
        print("Invalid item number!")

# Discount
if total >= 500:
    discount = total * 10 / 100
else:
    discount = 0

# GST
after_discount = total - discount
gst = after_discount * 5 / 100
final_bill = after_discount + gst

print("\n========== BILL ==========")
print("Customer Name:", name)
print("Subtotal: ₹", total)
print("Discount: ₹", discount)
print("GST (5%): ₹", gst)
print("--------------------------")
print("Final Bill: ₹", final_bill)
print("==========================")
print("Thank you for visiting!")
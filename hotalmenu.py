menu = {
    'Pizza': 199,
    'Pasta': 149,
    'Cold Drink(Glass)': 49,
    'Ice Cream': 69,
    'Chicken Biryani': 299,
    'Paneer Butter Masala': 179,
    'Veg Fried Rice': 129,
    'Chicken Lollipop': 189,
    'French Fries': 99,
    'Gulab Jamun (2 Pcs)': 59,
    'Butter Naan': 30,
    'Tandoori Roti': 20,
    'Fresh Lime Soda': 59,
    'Brownie with Ice Cream': 119,
    'Mango Shake': 79,
}

# Create lowercase lookup to handle case-insensitive input
menu_lookup = {item.lower(): item for item in menu}

print("🍽️ Welcome to Baba Da Dhaba")
print("📋 Hotel Menu")
print("-" * 35)
for item, price in menu.items():
    print(f"{item:<30} ₹{price}")

order_total = 0
orders = []

while True:
    user_input = input("\nEnter the name of the item you want to order: ").strip().lower()

    if user_input in menu_lookup:
        actual_item = menu_lookup[user_input]
        order_total += menu[actual_item]
        orders.append(actual_item)
        print(f"✅ '{actual_item}' has been added to your order.")
    else:
        print(f"❌ Sorry, the item '{user_input}' is not available.")

    another = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another != "yes":
        break

# Final Order Summary
print("\n🧾 Your Order Summary:")
for item in orders:
    print(f"- {item}: ₹{menu[item]}")
print(f"💰 Total Amount: ₹{order_total}")
print("🙏 Thanks for ordering from Baba Da Dhaba!")

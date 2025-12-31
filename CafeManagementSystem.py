

from datetime import datetime

class CafeManagementSystem:
    def __init__(self):
        self.menu = {
            "Coffee": 2.50,
            "Tea": 2.00,
            "Sandwich": 5.00,
            "Cake": 3.50,
            "Water": 1.00
        }
        self.orders = []

    def display_menu(self):
        print("\n--- CAFE MENU ---")
        for item, price in self.menu.items():
            print(f"{item:15} | ${price:.2f}")
        print("\n")

    def take_order(self):
        self.display_menu()
        current_order = {"items": [], "total": 0.0, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        
        while True:
            item = input("\nEnter item name to order (or 'done' to finish): ").capitalize()
            if item == 'Done':
                break
            
            if item in self.menu:
                try:
                    qty = int(input(f"Enter quantity for {item}: "))
                    if qty > 0:
                        cost = self.menu[item] * qty
                        current_order["items"].append({"item": item, "qty": qty, "price": self.menu[item]})
                        current_order["total"] += cost
                        print(f"Added {qty} x {item} to order. Subtotal: ${current_order['total']:.2f}")
                    else:
                        print("Quantity must be greater than zero.")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Item not found in menu.")

        if current_order["items"]:
            self.orders.append(current_order)
            print(f"\nOrder placed successfully! Total amount: ${current_order['total']:.2f}")
        else:
            print("\nOrder cancelled (no items selected).")

    def view_sales(self):
        if not self.orders:
            print("\nNo sales recorded yet.")
            return

        print("\n--- SALES REPORT ---")
        grand_total = 0.0
        for i, order in enumerate(self.orders, 1):
            print(f"Order #{i} | {order['timestamp']} | Total: ${order['total']:.2f}")
            grand_total += order['total']
        print("--------------------")
        print(f"Grand Total Sales: ${grand_total:.2f}")

    def run(self):
        while True:
            print("\n=== CAFE MANAGEMENT SYSTEM ===")
            print("1. View Menu")
            print("2. Take Order")
            print("3. View Sales Report")
            print("4. Exit")
            
            choice = input("Enter choice (1-4): ")
            
            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.take_order()
            elif choice == '3':
                self.view_sales()
            elif choice == '4':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cafe = CafeManagementSystem()
    cafe.run()

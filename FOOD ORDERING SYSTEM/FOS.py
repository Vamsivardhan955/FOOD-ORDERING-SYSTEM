class FoodOrderingSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "Pizza", "price": 10.0},
            2: {"name": "Burger", "price": 5.0},
            3: {"name": "Pasta", "price": 7.0},
            4: {"name": "Salad", "price": 4.0}
        }
        self.orders = []
        self.daily_sales = 0.0

    def display_menu(self):
        print("Order Menu")
        for key, item in self.menu.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")
        print("0. Finish Order")

    def take_order(self):
        self.display_menu()
        while True:
            choice = int(input("Enter the item number to order (0 to finish): "))
            if choice == 0:
                break
            elif choice in self.menu:
                quantity = int(input(f"Enter quantity for {self.menu[choice]['name']}: "))
                self.orders.append((self.menu[choice], quantity))
            else:
                print("Invalid choice. Please try again.")

    def generate_report(self):
        print("Daily Transaction Report")
        for item, quantity in self.orders:
            print(f"{item['name']} - {quantity} x ${item['price']:.2f} = ${item['price'] * quantity:.2f}")
        print(f"Total Sales: ${self.daily_sales:.2f}")

    def process_payment(self):
        total = sum(item['price'] * quantity for item, quantity in self.orders)
        print(f"Total amount due: ${total:.2f}")
        payment = float(input("Enter payment amount: "))
        while payment < total:
            print("Insufficient payment. Please enter the correct amount.")
            payment = float(input("Enter payment amount: "))
        self.daily_sales += total
        change = payment - total
        print(f"Payment received. Your change is ${change:.2f}")
        self.orders = []  # Clear orders after payment

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("(O) Order Menu")
            print("(R) Report Menu")
            print("(P) Payment Menu")
            print("(Q) Quit")
            choice = input("Enter your choice: ").upper()
            if choice == "O":
                self.take_order()
            elif choice == "R":
                self.generate_report()
            elif choice == "P":
                self.process_payment()
            elif choice == "Q":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = FoodOrderingSystem()
    system.main_menu()

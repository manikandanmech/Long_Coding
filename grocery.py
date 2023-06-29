import datetime

users = []
GroceryListItems = []
bookings_list = []

class GroceryList:
    def __init__(self, id, groceryname, quantity, price):
        self.groceryId = id
        self.groceryName = groceryname
        self.Quantity = quantity
        self.Price = price

class Bookings:
    def __init__(self, BookingID, userId, BookedAt, groceryDetails):
        self.booking_id = BookingID
        self.userId = userId
        self.booked_at = BookedAt
        self.groceryDetails = groceryDetails

class groceryApp:
    booking_count = 0

    def __init__(self, id: int, Name: str, Email: str, Password: str, Role: str):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
        self.role = Role

    def getUserName(self) -> str:
        return self.name

    def hardCodedData(self):
        users.append(self)
        return users

    def validateLogin(self, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None

    def Welcome(self):
        print('Hi Welcome Customer', self.name)

class groceryShowCase(groceryApp):
    def __init__(self, id, Name, Email, Password, Role):
        super().__init__(id, Name, Email, Password, Role)
        self.cart = []  # Initialize an empty cart for the user

    def grocery_for_customer(self):
        stayInCustomerMenu = True
        while stayInCustomerMenu:
            print("\n------------------")
            print("Customer Menu")
            print("1. Display the grocery")
            print("2. Add to cart")
            print("3. Booked History")
            print("4. Delete your history")
            print("5. Logout")
            choice = int(input("Enter your Choice: "))

            if choice == 1:
                grocery1 = GroceryList(1, 'Mango', '10', '20')
                grocery2 = GroceryList(2, 'Cauliflower', '10', '40')
                grocery3 = GroceryList(3, 'Cabbage', '10', '30')
                GroceryListItems.append(grocery1)
                GroceryListItems.append(grocery2)
                GroceryListItems.append(grocery3)

                for grocery in GroceryListItems:
                    print(grocery.groceryId)
                    print(grocery.groceryName)
                    print(grocery.Quantity)
                    print(grocery.Price)
                    print('---------------------------------------------')

            if choice == 2:
                while True:
                    print("Grocery List:")
                    for grocery in GroceryListItems:
                        print(grocery.groceryId, grocery.groceryName, grocery.Quantity, grocery.Price)
                    
                    item_id = int(input("Enter the ID of the item to add to cart (or 0 to stop adding): "))
                    if item_id == 0:
                        break
                    quantity = int(input("Enter the quantity: "))
                    selected_item = None
                    for grocery in GroceryListItems:
                        if grocery.groceryId == item_id:
                            selected_item = grocery
                            break
                    
                    if selected_item is None:
                        print("Invalid item ID. Please try again.")
                    else:
                        total_price = int(selected_item.Price) * quantity
                        cart_item = {
                            'groceryId': selected_item.groceryId,
                            'groceryName': selected_item.groceryName,
                            'Quantity': quantity,
                            'Price': total_price
                        }
                        self.cart.append(cart_item)
                        print("Item added to cart successfully.")
                    view_cart = input("Do you want to see the cart? (y/n): ")
                    if view_cart.lower() == "y":
                        if len(self.cart) == 0:
                            print("Your cart is empty.")
                        else:
                            print("Your Cart:")
                            for item in self.cart:
                                print("Grocery ID:", item['groceryId'])
                                print("Grocery Name:", item['groceryName'])
                                print("Quantity:", item['Quantity'])
                                print("Price:", item['Price'])
                                print('---------------------------------------------')
                        print("Payment Options:")
                        print("1. Card")
                        print("2. UPI")
                        print("3. Cash on Delivery")
                        payment_choice = int(input("Choose a payment option: "))
                    
                        if payment_choice == 1:
                            print("Payment successful. Thank you for using card.")
                        elif payment_choice == 2:
                            print("Payment successful. Thank you for using UPI.")
                        elif payment_choice == 3:
                            print("Payment successful. Thank you for choosing Cash on Delivery.")
                        else:
                            print("Invalid payment option.")
                        booking_data = Bookings(self.booking_count, self.userID, datetime.datetime.now(), self.cart)
                        bookings_list.append(booking_data)
                        self.booking_count += 1  
                        break

            if choice == 3:
                for booking in bookings_list:
                    print(f"Booking ID: {booking.booking_id}")
                    print(f"User ID: {booking.userId}")
                    print(f"Booked At: {booking.booked_at}")
                    for item in self.cart:
                        print("Grocery Name:", item['groceryName'])
                        print("Quantity:", item['Quantity'])
                        print("Price:", item['Price'])
                    print('---------------------------------------------')
            if choice == 4:
                if len(bookings_list) == 0:
                    print("No booking history available.")
                else:
                    print("Booking History:")
                    for booking in bookings_list:
                        print("Booking ID:", booking.booking_id)
                        print("User ID:", booking.userId)
                        print("Booked At:", booking.booked_at)
                        print('---------------------------------------------')
            
                    delete_choice = input("Enter the Booking ID to delete the history (or 'n' to cancel): ")
                    if delete_choice == 'n':
                        print("Deletion canceled.")
                    else:
                        delete_choice = int(delete_choice)
                        deleted = False
                        for booking in bookings_list:
                            if booking.booking_id == delete_choice:
                                bookings_list.remove(booking)
                                deleted = True
                                break
                        if deleted:
                            print("Booking history deleted successfully.")
                        else:
                            print("Invalid Booking ID. Please try again.")
                            
            if choice == 5:
                print("Logout Successfully")
                break

class AdminFlow(groceryApp):
    def __init__(self, id, Name, Email, Password, Role):
        super().__init__(id, Name, Email, Password, Role)

    def Welcome(self):
        print('Hi Welcome Admin')
        print(self.getUserName())

class DeliveryFlow(groceryApp):
    def Welcome(self):
        print('Hi Welcome Servicer')

if __name__ == "__main__":
    app = groceryApp(1, "Priya", "kamal@gmail.com", "kamal123", "customer")
    app.hardCodedData()
    app = groceryApp(2, "Kamali", "kamali@gmail.com", "kamali123", "Admin")
    app.hardCodedData()
    app = groceryApp(3, "Kamal", "kamali@gmail.com", "kamali123", "Servicer")
    app.hardCodedData()

    login_user = app.validateLogin("kamal@gmail.com", "kamal123")

    if login_user:
        print('Login Success')
        if login_user.role == "Admin":
            admin = AdminFlow(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role)
            admin.Welcome()
        elif login_user.role == "customer":
            app.Welcome()
            grocery = groceryShowCase(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role)
            grocery.grocery_for_customer()
        elif login_user.role == "Servicer":
            servicer = DeliveryFlow(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role)
            servicer.Welcome()

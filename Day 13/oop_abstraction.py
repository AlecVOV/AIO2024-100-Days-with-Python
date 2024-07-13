from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, manufacturer, inventory):
        super().__init__()
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.inventory = inventory

    #getter and setter
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    #-----------------
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    #-----------------
    def get_manufacturer(self):
        return self._manufacturer
    
    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer
    #-----------------
    def get_inventory(self):
        return self._inventory
    
    def set_inventory(self, inventory):
        self._inventory = inventory

    #--------------
    @abstractmethod
    def get_details(self):
        pass


class Phone(Product):
    def __init__(self, name, price, product_source, avaliable, operating_system):
        super().__init__(name, price, product_source, avaliable)
        self.operating_system = operating_system

    def get_details(self):
        return f"{self.name} - {self.manufacturer} - {self.price} AUD - Operating System: {self.operating_system}"

class Laptop(Product):
    def __init__(self, name, price, manufacturer, inventory, processor):
        super().__init__(name, price, manufacturer, inventory)
        self.processor = processor

    def get_details(self):
        return f"{self.name} - {self.manufacturer} - {self.price} AUD - CPU Processor: {self.processor}"

class TV(Product):
    def __init__(self, name, price, manufacturer, inventory, screen_size):
        super().__init__(name, price, manufacturer, inventory)
        self.screen_size = screen_size

    def get_details(self):
        return f"{self.name} - {self.manufacturer} - {self.price} AUD - Screen Size: {self.screen_size}"

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.buying_items = []

    def add_item(self, product, quantity):
        self.buying_items.append((product, quantity))
        
    def calculating_price(self):
        total = 0 
        for product, quantity in self.buying_items:
            total += product.price * quantity
        return total

    def print_invoice(self):
        print(f"Invoice for {self.customer_name}")
        num = 0
        for product, quantity in self.buying_items:
            num += 1
            print(f"{num}) {product.get_details()} - {quantity}")
        print(f"Total: {self.calculating_price()} AUD")




# Creating product instances
macbook = Laptop("Macbook", 1500, "Apple", 20, "Apple Silicon")
iphone = Phone("iPhone 14", 25000000, "Apple", 50, "iOS")
LG_tv = TV("LG - SMART HOME", 1000, "LG", 100, "50 inches")


# Creating an order instance for the customer "Nguyễn Văn A"
order = Order("Nguyễn Văn A")

# Adding items to the order
order.add_item(iphone, 2)
order.add_item(macbook, 1)
order.add_item(LG_tv, 1)

# Printing the invoice for the order
order.print_invoice()

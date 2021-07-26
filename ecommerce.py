class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases =[]

    def purchase(self,inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product]>0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("We are out of stock")
        else:
                print("We dont have that product")
    
    def print_purchases(self):
        print("Customer has Purchase:")
        for item in self.purchases:
            print(item.name)

class Product:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory ={}

    def add_product(self,product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ':' + str(value))
        print()

customer = Customer('joe',"joe@gmail.com")
print(customer.name)
print(customer.email)

watch = Product('Apple Watch',299)
mac = Product('Mac','1999')

inventory = Inventory()
inventory.add_product(watch,100)
inventory.add_product(mac,198)
inventory.print_inventory()

customer.purchase(inventory,watch)
inventory.print_inventory()
customer.print_purchases()
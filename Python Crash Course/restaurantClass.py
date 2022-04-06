flavors = []

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.increment = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
        print(self.number_served)

    def increment_number_served(self, increment, tables):
        if increment >= 0 and tables >= 0:
            self.number_served += (increment * tables)
            print(f"Total of {self.number_served} customers served today")
        else:
            print("You don't want a negative person!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self, flavors):
        print(f"You're favorite flavors are {flavors}")
        
flavorsList = input("What are your favorite flavors? ")

benNjerrys = IceCreamStand("Ben and Jerry's", "Dessert")
benNjerrys.get_flavors(flavorsList)

# boudin = Restaurant("Boudin", "American")
# boudin.describe_restaurant()
# boudin.open_restaurant()
# boudin.set_number_served(4)
# boudin.increment_number_served(3, 5)

# panera = Restaurant("Panera", "American")
# panera.describe_restaurant()
# panera.open_restaurant()

# panda = Restaurant("Panda Express", "Chinese")
# panda.describe_restaurant()
# panda.open_restaurant()
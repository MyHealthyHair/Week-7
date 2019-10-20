class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\n" + self.restaurant_name + " makes " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("\n" + self.restaurant_name + " is now opening. ")

restaurant = Restaurant('the queen', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


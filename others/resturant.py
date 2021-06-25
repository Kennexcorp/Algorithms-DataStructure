class Restaurant :

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self) : 
        print("We are open for trades")
        

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}, we have {self.cuisine_type} of chairs")
        
restaurant = Restaurant("Happiness Eatery Services", "Trade Cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()

    
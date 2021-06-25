from Car import Car
from Battery import Battery

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        Car.__init__(self, make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
    
        
            

my_new_car = ElectricCar('tesla', 'model s', 2019)

print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_battery()
my_new_car.fill_gas_tank()
my_new_car.battery.get_range()
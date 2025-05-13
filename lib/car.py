from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
    # No need to redefine fill_up_tank() here unless we want different behavior
    # It will automatically inherit from Vehicle
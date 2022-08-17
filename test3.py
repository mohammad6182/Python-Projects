class vehicle:
    type_use = "No Type Provided"
    num_passenger = ""
    engine_type = ""
    fuel_type= ""

    def information(self):
        entry_type = input("what type of vehicle is this? ")
        entry_passenger = input("please enter the number pf passenger this vehicle can fit:  ")
        entry_engine = input("what type of engine this vehicle has?")
        entry_fuel = input("what type of fuel does this vehicle use?")


new_vehicle = vehicle()
new_vehicle.information()

def __init__(self,type_use,num_passenger,engine_type,fuel_type):
    self.type_use= type_use
    self.num_passenger = num_passenger
    self.engine_type = engine_type
    self.fuel_type = fuel_type

    

class suv(vehicle):
    number_row = 3
    family_vehicle= True

class airplane(vehicle):
    landing_system = " "
    number_engine = 4
    
    
    
    
    
    

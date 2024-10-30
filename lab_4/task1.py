class Plane:
       def __init__(self, name = "unnamed", number_of_passengers = 0, fuel_tank_capacity_in_liters = 0, max_speed = 0, manufacturer = "unknown",):
           self.__name = name
           self.__number_of_passengers = number_of_passengers
           self.__fuel_capacity_in_liters = fuel_tank_capacity_in_liters
           self.max_speed = max_speed
           self.manufacturer = manufacturer

       def get_name(self):
           return self.__name

       def get_number_of_passengers(self):
           return self.__number_of_passengers

       def get_fuel_capacity_in_liters(self):
           return self.__fuel_capacity_in_liters

       def __str__(self):
           return f"{self.__name}, {self.__number_of_passengers} passengers, {self.__fuel_capacity_in_liters} liters, max speed {self.max_speed} k/h manufacturer {self.manufacturer}"

       def __repr__(self):
           return f"Plane(name='{self.__name}', number_of_passengers={self.__number_of_passengers}, fuel_capacity_in_liters={self.__fuel_capacity_in_liters} max_speed={self.max_speed}, manufacturer={self.manufacturer})"

       def __del__(self):
           print(f"{self.__name} destroyed.")

       def main(self):

           plane1 = Plane("Boeing 747", 416, 238840, 920, "Boeing")
           plane2 = Plane( )
           plane3 = Plane("Airbus A380", 555, 320000, 945, "Airbus")

           print(plane1)
           print(plane2)
           print(plane3)

plane_obj = Plane()

plane_obj.main()



# def abstraktuota_funkcija(x):
#     """
#     Tai yra abstraktuota funkcija, kuri priima vieną argumentą x ir grąžina jo kvadratą.
    
#     :param x: Skaičius, kurio kvadratą norime gauti
#     :return: Kvadratas skaičiaus x
#     """
#     print("kazkokie papildomu veiksmai, funkcijoje")
#     return x ** 2

# abstraktuota_funkcija(5)

# sum([4,8,9,6,5])

# class enkapsuliuota_klase:
#     def __init__(self):
#         self.__skaiciai = [4,5,9]

#     def gauti_skaicius(self):
#         return self.__skaiciai

    
# enkapsuliuota_klase_objektas = enkapsuliuota_klase()
# print(enkapsuliuota_klase_objektas.gauti_skaicius())

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def make_sound(self):
#         print("Vroom!")
#     def go(self):
#         print(f"The {self.brand} {self.model} is moving.")

# class Car(Vehicle):
#     def __init__(self, brand, model, year, num_doors):
#         super().__init__(brand, model, year)
#         self.num_doors = num_doors

#     def display_info(self):
#         print(f"Car: {self.brand} {self.model}, Year: {self.year}, Doors: {self.num_doors}")
#     def go(self):
#         print(f"The {self.brand} {self.model} is driving on the road.")

# class Motorcycle(Vehicle):
#     def __init__(self, brand, model, year, has_sidecar):
#         super().__init__(brand, model, year)
#         self.has_sidecar = has_sidecar

# # veh = Vehicle("Toyota", "Corolla", 2020)
# # print(veh.brand, veh.model, veh.year)
# # car = Car("Honda", "Civic", 2021, 4)
# # print(car.brand, car.model, car.year, car.num_doors)
# # # veh.display_info()
# # car.display_info()
# # veh.make_sound()
# # car.make_sound()
# # veh.go()
# # car.go()
# # motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021, True)
# # motorcycle.go()

# # polymorphism
# car = Car("Toyota", "Camry", 2022, 4)
# veh = Vehicle("Generic", "Vehicle", 2020)
# moto = Motorcycle("Yamaha", "MT-07", 2021, False)

# vehicles = [car, veh, moto]

# for vehicle in vehicles:
#     vehicle.go()  # Calls the appropriate go() method based on the object type
#     if isinstance(vehicle, Vehicle): # yra tiesa dvejais atvejais, jeigu objektas yra vaikas, arba pats to tipo kuri tikrinam
#         vehicle.display_info()  # This will work for Car
#         vehicle.make_sound()  # This will work for Car
#     # vehicle.display_info()  # This will raise an AttributeError for Vehicle and Motorcycle since they don't have display_info method


# print("hello this is friends change")

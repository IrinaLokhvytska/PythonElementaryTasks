class CarsManufacture():
    cars = list ()

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def produceCar(self, kind, price, colour):
        cars = self.cars
        cars.append({kind: {'price':price, 'colour':  colour}})
        return Car(kind, price, colour)

    def getCars(self):
        return self.cars

class Car():
    cars = list ()
    def __init__(self, kind, price, colour):
        self.kind = kind
        self.price = price
        self.colour = colour
        cars = self.cars
        cars.append({kind: {'price':price, 'colour':  colour}})

    def drive(self):
        speed = {'Minivans': 60, 'Sports': 110, 'Luxury': 90}
        for key, value in speed.items():
            if self.kind == key:
                return 'My average speed: ' + str(value)
            else:
                return 'My average speed: 75'

    def getCars(self):
        return self.cars

manufacture =  CarsManufacture('Ukraine', 'Dnipro')
car1 = manufacture.produceCar('Minivans', 500, 'black')
car2 = manufacture.produceCar('Volvo', 1000, 'white')
print(manufacture.getCars())
print(car1.drive())
print(car2.getCars())
# dependency.py

class Fuel:
    def burn(self):
        print("Fuel is burning, energy released.")

class Car:
    def start(self, fuel): # Dependency (Car uses Fuel temporarily in a method)
        fuel.burn()
        print("Car has started.")

if __name__ == "__main__":
    car = Car()
    fuel = Fuel()
    car.start(fuel)


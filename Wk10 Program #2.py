#reilly Kurth
#4/3/2025
#program 2

class Car:
    def __init__(self,year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed

def main():
    car = Car(2023, "Jeep")
    print("Car is accelerating")
    for _ in range(5):
        car.accelerate()
        print(f"Current speed is {car.get_speed()}")
    print("Car is breaking")
    for _ in range(5):
        car.brake()
        print(f"Current speed is {car.get_speed()}")

if __name__ == "__main__":
    main()


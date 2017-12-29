class Car(object):
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def start(self):
        print("The car is starting.")

class RaceCar(Car):
    def __init__(self, model, color, speed, has_turbo):
        self.has_turbo = has_turbo
        return super(RaceCar, self).__init__(model, color, speed)

    def race(self):
        print("The car is racing.")

race_car = RaceCar('Chevy', 'yellor', 200, True)
print(race_car.has_turbo)
race_car.start()
race_car.race()

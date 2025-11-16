class Car:
    wheels = 4
    mirriors = 2
    lights = 4
    def fuel(self):
        return("Car runs on petrol")
    
class Bugati(Car):
    pass

v1 = Bugati()
print(v1.fuel())
print(v1.wheels)
print(v1.mirriors)
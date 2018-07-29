#! /usr/bin/env python

class Car ():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        #返回整洁的描述
        long_name = str(self.year) + " " + self.make + " " +self.model
        return  long_name.title()
    def read_odometer(self):
        #打印一条指出汽车里程的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer. ")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_used_car = Car("Geely", "outback", 2017)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(19700)
my_used_car.read_odometer()

my_used_car.increment_odometer(300)
my_used_car.read_odometer()



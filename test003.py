#! /usr/bin/env python

class Car():

    #一次模拟汽车的实验

    def __init__(self, make, model, year):
        #初始化描述汽车属性
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

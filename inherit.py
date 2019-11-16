# coding = utf-8
# __Author__ = "shicaicai"
"""
父类: Car
单独的属性类: Battery
子类: ElectricCar
子类的初始化参数比父类多一个，将属性类Battery的实例作为参数传给子类，
"""

class Car():
    """
    父类：汽车
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    """
    电池类
    """
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """
    子类：电车
    """
    def __init__(self, make, model, year, origin_battery_size):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.origin_battery_size = origin_battery_size


if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2016, Battery(80))
    # 实例化ElectricCar, 并将Battery实例化的对象作为初始化参数
    print(my_tesla.get_descriptive_name())
    my_tesla.origin_battery_size.describe_battery()

# class Person:
#     def __init__(self, name, surname, prof):
#         self.name = name
#         self.surname = surname
#         self.profession = prof
#
#     def hello(self):
#         return f"Person's name is {self.name} {self.surname}. He is {self.profession}"
#
#
# class Student(Person):
#     def __init__(self, name, surname, prof, age):
#         super().__init__(name, surname, prof)
#         self.age = age
#
#     def hello(self):
#         return f"{super().hello()} and {self.age} years old."
#
#
# student_1 = Student("Erik", "Atanesyan", "economist", 25)
# print(student_1.hello())


class Country:
    def __init__(self, country_name, continent):
        self.country_name = country_name
        self.continent = continent

    def country_1(self):
        return f"Product is from {self.country_name} which is in {self.continent}."


class Brand:
    def __init__(self, brand_name, business_start_date):
        self.brand_name = brand_name
        self.date = business_start_date

    def brand_1(self):
        return f"{self.brand_name} produced the product and has started their business in {self.date}."


class Season:
    def __init__(self, season_name, average_temperature):
        self.season_name = season_name
        self.temperature = average_temperature

    def season_1(self):
        return f"It's {self.season_name} outside and average temperature is {self.temperature} celsius."


class Product(Country, Brand, Season):
    def __init__(self, country_name, continent, brand_name, business_start_date, season_name, average_temperature,
                 product_name, product_type, product_price, product_quantity):
        super().__init__(country_name, continent)
        super().__init__(brand_name, business_start_date)
        super().__init__(season_name, average_temperature)
        self.product_name = product_name
        self.type = product_type
        self.price = product_price
        self.quantity = product_quantity

    def product_1(self):
        return f"You are buying {self.quantity} {self.product_name} {self.type} with {self.price} drams."

    def product_2(self):

    def product_3(self):

    def product_4(self):

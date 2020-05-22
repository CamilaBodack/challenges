from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department("managers", 1)

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, new_department):
        self.__departament.name = new_department

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department("sellers", 2)
        self.__sales = 0

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, new_department):
        self.__departament.name = new_department

    def get_sales(self):
        return self.__sales

    def put_sales(self, new_sales):
        self.__sales += new_sales

    def calc_bonus(self):
        return self.__sales * 0.15
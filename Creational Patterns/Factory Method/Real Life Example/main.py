from __future__ import annotations
from abc import ABC, abstractmethod


class Department(ABC):
    @abstractmethod
    def get_employee(self, id):
        pass

    def fire(self, id):
        employee = self.get_employee(id)
        employee.dismiss()


class ITDepartment(Department):
    def get_employee(self, id):
        return Programmer(id)


class AccountingDepartment(Department):
    def get_employee(self, id):
        return Accountant(id)


class Employee(ABC):
    def __init__(self, id):
        self.id = id
    
    @abstractmethod
    def dismiss(self):
        pass

class Accountant(ABC):
    def __init__(self, id):
        self.id = id

    def dismiss(self):
            print(f'Accountant {self.id} fired')

class Programmer(ABC):
    def __init__(self, id):
        self.id = id

    def dismiss(self):
            print(f'Programmer {self.id} fired')

def client_code(department: Department):
    department.fire('PERSON_123')

if __name__ == "__main__":
    print("Dismissing Accountant")
    client_code(AccountingDepartment())
    print("\n")

    print("Dismissing Programmer")
    client_code(ITDepartment())
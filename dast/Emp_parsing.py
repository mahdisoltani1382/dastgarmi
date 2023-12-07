class Employee:
    def __init__(self , firstname, lastname , salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls , employee):
        firstname , lastname , salary = employee.split('-')
        return cls(firstname , lastname , float(salary))
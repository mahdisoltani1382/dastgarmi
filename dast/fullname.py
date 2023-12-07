class Employee :
    def __init__(self , firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return self.firstname +' '+ self.lastname

    def email(self):
        return self.firstname +'.' + self.lastname + '@company.com'
    

emp_3 = Employee("Antony", "Walker")
print(emp_3.firstname)
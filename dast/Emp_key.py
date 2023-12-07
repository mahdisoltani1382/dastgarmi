class Employee:
    def __init__(self , fullname , **kwargs):
        self.name, self.lastname = fullname.split(' ')

        for k, v in kwargs():
            setattr(self, k, v)


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian") 

print(richard.height)

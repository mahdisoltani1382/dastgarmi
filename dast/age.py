class Person:

    def __init__(self , name , age ):
        self.name = name
        self.age = age

    def compare_age(self , other):
        if other.age > self.age:
            return f'{other.name} is older than me.'
        if other.age == self.age:
            return f'{other.name} is the same age as me.'
        if other.age < self.age:
            return f'{other.name} is younger than me.'

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

p1.compare_age(p2)




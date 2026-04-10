class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)
	
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def have_birthday(self):
        self.age = self.age + 1
        print(f"Happy Birthday! {self.name} is now {self.age}")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.say_hello()
person1.have_birthday()

person2.say_hello()
person2.have_birthday()

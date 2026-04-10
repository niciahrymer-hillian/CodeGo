# Understanding Python Classes: A Guide to Creating a Person Class

## What is a Class?
A class is a blueprint or template that defines the properties (attributes) and behaviors (methods) that all objects of that type can have.

## The Person Class Step by Step Guide

### Step 1: Basic Class Structure
Heres how to create a simple Person class in the Python interpreter:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Step 2: Understanding the Constructor
The `__init__` method is Python's constructor. It helps initialize a new Person object with specific values:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Step 3: Creating Person Objects
Let's create some Person objects using our class:

```python
>>> person1 = Person("Alice", 25)
>>> person1
<__main__.Person object at 0x7f8b8c0b7040>

>>> person2 = Person("Bob", 30)
>>> person2
<__main__.Person object at 0x7f8b8c0b7070>
```

### Step 4: Accessing Object Properties
You can access the properties of a Person object using dot notation:

```python
>>> person1.name
'Alice'

>>> person1.age
25
```

### Step 5: Adding Methods
Let's add some methods to our Person class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
    
    def have_birthday(self):
        self.age = self.age + 1
        print(f"Happy Birthday! {self.name} is now {self.age}")
```

### Step 6: Using Methods
Now we can use these methods with our Person objects:

```python
>>> person1.say_hello()
Hello, my name is Alice

>>> person1.have_birthday()
Happy Birthday! Alice is now 26
```

## Practice Exercise
Try creating your own Person class with:
1. Create the basic class structure
2. Add properties (name and age)
3. Create a constructor (`__init__` method)
4. Create two Person objects
5. Access their properties
6. Add and use methods

## Common Mistakes to Avoid
1. Forgetting `self` as the first parameter in methods
2. Not using proper indentation (Python uses indentation instead of braces)
3. Forgetting to use `self.` when accessing instance variables
4. Not initializing variables in the `__init__` method

## Tips for Success
1. Always test your class by creating objects and using their methods
2. Use meaningful names for variables and methods
3. Keep your code organized and properly indented
4. Remember that each object is independent and has its own set of values
5. Use `self` to refer to the current instance

## Checking Your Work
You can use these Python interpreter commands to verify your work:
- `dir(person1)` - shows all attributes and methods of the person1 object
- `vars(person1)` - shows all instance variables
- `help(Person)` - shows documentation for the Person class

## Extended Example
Here's a more complete Person class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def is_adult(self):
        return self.age >= 18
    
    def have_birthday(self):
        self.age = self.age + 1
        print(f"Happy Birthday! {self.name} is now {self.age}")
```

Try using this extended example:
```python
>>> person = Person("John", 17)
>>> person.print_details()
Name: John
Age: 17
>>> print(person.is_adult())
False
>>> person.have_birthday()
Happy Birthday! John is now 18
>>> print(person.is_adult())
True
```

This guide should give you a solid foundation for understanding
how to create and use classes in Python.
Remember to practice by creating your own variations of the Person
class and experimenting with different properties and methods.

Maybe add a method that sets and gets a person's "chirality" (left-handed or right-handed) or "handedness" (ambidextrous, left-handed, right-handed).
What type of variable would be best for this?
What would be the default value?

You have to add a variable declaration for the handedness in the `__init__` method.
And add a getter and setter for the handedness.
Be sure to add a method to print out the handedness.

```python
class Person:
    def __init__(self, name, age, handedness="right-handed"):
        self.name = name
        self.age = age
        self.handedness = handedness
    
    def get_handedness(self):
        return self.handedness
    
    def set_handedness(self, handedness):
        valid_options = ["left-handed", "right-handed", "ambidextrous"]
        if handedness in valid_options:
            self.handedness = handedness
        else:
            print(f"Invalid handedness. Choose from: {valid_options}")
    
    def print_handedness(self):
        print(f"{self.name} is {self.handedness}")
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Handedness: {self.handedness}")
```

Save it in a file called `person.py` and also do the trinity of github commands:

```bash
git add .
git commit -m "Add Person class work"
git push
```

## Python vs Java Differences
1. **No explicit type declarations**: Python figures out types automatically
2. **`self` instead of implicit `this`**: Always use `self` as first parameter
3. **Indentation matters**: Python uses indentation instead of braces
4. **`__init__` instead of constructor**: Python's special method for initialization
5. **Snake_case naming**: Python uses snake_case for method names

## Conclusion

Classes and Objects are an essential part of object-oriented programming in Python.

Be sure to do commit of all this work to your GitHub repository.

```bash
touch finished.txt
git add .
git commit -m "Finished"
git push
```

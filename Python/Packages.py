# Create a program to create two class

# Create a constructor and a method for each class

class Car:
    def __init__(self, make, model, year):
        """Constructor to initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Method to display car information."""
        return f"{self.year} {self.make} {self.model}"

class Person:
    def __init__(self, name, age, job):
        """Constructor to initialize person attributes."""
        self.name = name
        self.age = age
        self.job = job

    def introduce(self):
        """Method to introduce the person."""
        return f"Hi, I'm {self.name}, {self.age} years old, and I work as a {self.job}."

car = Car("Toyota", "Camry", 2020)
person = Person("Alice", 30, "Engineer")
print(car.display_info())
print(person.introduce())


# Create a __init__.py for adding all packages


class Car:
    def __init__(self, make):
        """Constructor to initialize the car make."""
        self.make = make

    def show(self):
        """Method to display the car's make."""
        return f"Car make: {self.make}"

class Person:
    def __init__(self, name):
        """Constructor to initialize the person's name."""
        self.name = name

    def greet(self):
        """Method to greet the person."""
        return f"Hello, I'm {self.name}"
    
if __name__ == "__main__":
    # Creating instances
    car = Car("Toyota")
    person = Person("Alice")

    # Displaying results
    print(car.show())      
    print(person.greet())



# Import the respective packages


from my_package import Car, Person

# Creating instances of Car and Person
car = Car("Toyota")
person = Person("Alice")

# Displaying results
print(car.show())      
print(person.greet())

# Call each class by creating an object to it


class Car:
    def __init__(self, make):
        """Constructor to initialize the car make."""
        self.make = make

    def show(self):
        """Method to display the car's make."""
        return f"Car make: {self.make}"


class Person:
    def __init__(self, name):
        """Constructor to initialize the person's name."""
        self.name = name

    def greet(self):
        """Method to greet the person."""
        return f"Hello, I'm {self.name}"

# Usage of the classes
if __name__ == "__main__":
    # Creating instances of Car and Person
    car = Car("Toyota")
    person = Person("Alice")

    # Displaying results by calling methods
    print(car.show())      
    print(person.greet())



# Create a program by all the above


# Class 1: Car
class Car:
    def __init__(self, make):
        """Constructor to initialize the car make."""
        self.make = make

    def show(self):
        """Method to display the car's make."""
        return f"Car make: {self.make}"

# Class 2: Person
class Person:
    def __init__(self, name):
        """Constructor to initialize the person's name."""
        self.name = name

    def greet(self):
        """Method to greet the person."""
        return f"Hello, I'm {self.name}"

# Main program to demonstrate object creation and method calling
if __name__ == "__main__":
    # Creating instances of Car and Person
    car = Car("Toyota")
    person = Person("Alice")

    # Calling methods of the created objects
    print(car.show())      
    print(person.greet())  




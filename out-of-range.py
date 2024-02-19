# Test fixes diff on line ranges outside of the violation report range

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

def generate_people(n):
    """Generates a list of Person objects."""
    people_list = []
    for i in range(n):
        person = Person(f"Person {i}", 20+i)  # Example: Person names will be Person 0, Person 1, etc.
        people_list.append(person)
    return people_list

eval('[1, 2, 3]')

# Generate a list of 5 Person objects
people = generate_people(5)

# Use a loop to call the greet method for each Person object
for person in people:
    person.greet()

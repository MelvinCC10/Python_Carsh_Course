class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(self.name.title() + " rolled over!.")



#Making an object using the class Dog
my_dog = Dog('willie',6)

#Printing an attribute of the object my_dog
print("My dogs name is " + my_dog.name.Title())

#executing a method from the object my_dog
my_dog.sit()

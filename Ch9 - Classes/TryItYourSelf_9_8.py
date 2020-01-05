"""
---9-3--------------------------------------------------------------------------
Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

---9-7--------------------------------------------------------------------------
Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.

---9-8--------------------------------------------------------------------------
Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.

"""

class User():
    """ A simple model of a user """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_name = ""

    def describe_user(self):
        print("First name = " + self.first_name.title())
        print("Last name = " + self.last_name.title())
        print("Age = " + str(self.age))

        if (self.user_name != ""):
            print("User-Name = " + self.user_name)
        else:
            print("User-Name = 'No user name has been set for this user'")

    def set_user_name(self,user_name):
        self.user_name = user_name
        print("Your User-Name has been changed to " + self.user_name)

class privileges():

    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("This user has the following privileges")
        for i in (self.privileges):
            print("-" + i)

class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges(["can add post", "can delete post", "can ban users"])

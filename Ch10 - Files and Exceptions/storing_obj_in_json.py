import json

class human():

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

john = human('john','deer', 45)

filename = 'human.json'
with open(filename, 'w') as f_obj:
    json.dump(john.__dict__, f_obj)

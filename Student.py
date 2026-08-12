#This file used to record student class
#attributes are: name ,gender ,age, phone_number ,descrimination

#1.define student class
class Student:
    #define magic method
    def __init__(self,name,gender,age,phone,desc):
        ''' initialise attributes of student'''
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.desc=desc

    #define str
    def __str__(self):
        return f'name:{self.name} , gender:{self.gender} , age:{self.age} , phone:{self.phone} , desc:{self.desc}'
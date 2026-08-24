'''
OOP ---> class,object,methods (__init__())
Encapsulation ---> public,protected,private
inheritance--->it is one of key feature of oop where we inher the propertices (attribute/methods)
from one class to another class(base class (parent class)-->dervied class (child class))
whatsapp--->personal user,business user (catalog),community advar
Features ---> code reusability,avoiding code duplication,
code maintainabilty,polymorphism (method overriding(super()),method overloading,operator overloading,__add__,__str__)



Types : 
single Inheritance(Finger print)
---->one child class inheritance properties from one parent class
multiple Inheritance(mother,father-->child)
---->one child class inheritance properties from two parent class
multilevel Inheritance(grandparent -->parent-->child)
---->level by level
hierarchical inheritance --->multiple child class
---->inheritance properties from single parent
hybrid inheritance --->it can carry one or more type of inheritance
Syntax:

single inheritance:

class baseclass:
    statement(s):
    ........
class derivedclass(baseclass):
    ............
    ............



#whatsapp scenario --->personal user,Business user

class User:
    """single Inheritance usage"""
    def send_message(self):
        print('sending message')
    def voice_call(self):
        print('making voice calls')
    def video_call(self):
        print('making video_calls')
class BusinessUser(User):
    #pass
    def create_catalog(self):
        print("Display products catalog")
u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog()


#social media login --->user ---> update_users

class Users:
    """single inheritance usage"""
    company = "codegnan"#class attribute
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("mani","kumar")
#print(u1.full_name())
#print(u1.company)

class update_users(Users):
    def update_users(self):
        return self.fname.title()+""+self.lname.title().strip()
u1 = update_users("mani","kumar")
print(u1.company)
print(u1.full_name())
print(u1.update_users())
u2 = Users("sai","harsha")
print(u2.full_name())
print(u2.company)


#what if we have constructor in child class also...
#father --->kid(property)
class father:
    """usage of constructor in single inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'father property is {self.property}')
#class Kid(father):
 #   pass
class Kid(father):
    """now childclass will have constructor"""
    def __init__(self):
        self.cash = 200000
        #self.property = 2000000
    def Kid_property(self):
        print(f'kid property is {self.cash}')

obj = Kid()
obj.father_property()
obj.Kid_property()
'''
#in above case it is giving same value for father also as 2lakhs .when 
class father:
    """usage of constructor in single inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'father property is {self.property}')
class Kid(father):
 #   pass

    """now childclass will have constructor"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        self.cash = 200000
        #self.property = 2000000
    def Kid_property(self):
        print(f'kid property is {self.cash}')

obj = Kid()
obj.father_property()
obj.Kid_property()

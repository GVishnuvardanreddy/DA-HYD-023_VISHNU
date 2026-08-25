'''
Constructor -->Instance methods -->Public Attributes
Encapsulation

Constructor --> It is a special method (__init__())
which will automatically initialize the attributes and the methods
to the object in the class

class Cars:
    """Understanding the usage of Constructor in OOP"""
    def __init__(self,brand,name,price,color):
        self.brand = brand #public attributes
        self.name = name
        self.price = price
        self.color = color
    #Methods(behaviour)
    def details(self): #Instance method
        print(f'Car Brand is {self.brand}')
        print(f'Car Model name is {self.name}')
        print(f'Car Color is {self.color}')
        print(f'Car Price is {self.price}')
u1 = Cars("Tata","Nexon","9Lakhs","Blue")
u1.details()

class Cars:
    """Understanding the usage of Constructor in OOP"""
    def __init__(self):
        self.brand = "BMW"
        self.name = "Sedans"
        self.price = "50Lakhs"
        self.color = "White"
    #Methods(behaviour)
    def details(self):
        print(f'Car Brand is {self.brand}')
        print(f'Car Model name is {self.name}')
        print(f'Car Color is {self.color}')
        print(f'Car Price is {self.price}')
u1=Cars()
print(u1.brand,u1.name,u1.color,u1.price)
u1.details()

Encapsulation --> It is one of the main feature of OOP.
It binds (bundles) the data (attributes) and the methods (behaviour)
into a single unit (class) -->multiple objects
-->Attributes --> Public,Protected,Private
#Public attributes ---> Attributes defined inside the class(Constructor)
and can be modified outside the class

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user = username #Public attribiute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
u1 = CodegnanPortal("Sakethkallepu")
u1.display()
u1.user = "Saketh Kallepu" #modifying public attribute
u1.display()
print(u1.__dict__) #returns the key-value pairs for attributes
u2 = CodegnanPortal("jaychandra")
u2.display()
print(u2.__dict__)

#Protected attributes --> we use single underscore before an
#attribute moreover it can be modified also outside the class
#and even accessible in subclasses...
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
u1 = CodegnanPortal("Saketh",23456)
u1.display()
u1._otp = 3456
u1.display()

#Private Attributes  --> we use special notation as doubleunderscore
#such as __password
#Accessible only inside the class and cannot be directly 
#modify
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
        self.__password = password #private attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
u1 = CodegnanPortal("Saketh",23456,"admin123")
#print(u1.password) AttributeError as password is private
print(u1.__dict__)
print(u1._CodegnanPortal__password) #NameMangling
'''
#In above case we are using NameMangling but the right way is
#usage of getter() and setter() methods
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
        self.__password = password #private attribute
    #Usage of getter() method
    def get_password(self):
        #return "******"
        return self.__password
    #to modify the password we use setter() method
    def set_password(self,new_password):
        if len(new_password) <= 6:
            print("Wrong Password not satisfied number of characters")
        else:
            self.__password = new_password
            print("Now password is updated")
u1 = CodegnanPortal("Saketh",23456,"admin123")
print(u1.get_password())
u1.set_password("saketh")
u1.set_password("saketh123") #compulsory morethan 6
print(u1.get_password())
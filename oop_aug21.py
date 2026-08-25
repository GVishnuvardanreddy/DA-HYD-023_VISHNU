'''
OOP --> Object Oriented Programming -->Objects
-->Attributes (Data),Methods(Behaviour)
class,object ->A Class is a blueprint(template) for an object
An object is an instance (physicl thing) which utilises the
class
Chair (object)--> Wood,Tools,Dimensions(blueprint),Carpenter
Ecommerce Platform
-->Mobiles -> Price,Features (Camera,Storage,RAM)
-->variables,def mobile()
-->Laptops --> Price,Features
-->variables,def laptop()
-->Gadgets -->Price,Features
-->variables,def gadgets()
-->Electronic Items -->price,features
-->variables,def elect()
Features of OOP -->Modularity,Scalability,
Encapsulation(binding the data(attributes),
features to the class) (Objects)
Abstraction -->Show only relevant information to the class(objects)
Inheritance -->Acquring properties (attributes,methods)
Single -->Fingerprint
Multiple --> Parents (Mother,Father) -->Child
Multilevel --> GrandParent -->parent --> child
Polymorphism -->Method Overloading,Method Overriding,
Operator Overriding
'''
#Syntax for class creation :
'''
class Class_Name:
    """Doc String"""
    attributes (characteristics) 
    .........
    def func(self): (behaviour)
        .....
        ......
    ......
obj = Class_Name()

#Student Class with basic details
class Student:
    """Understanding the usage of OOP"""
    name = "Saketh"
    id = "CGH2314"
    gender = "male"
    email_id = "saketh@codegnan.com"
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail id is {self.email_id}')
u1 = Student()
print(u1)
#print(dir(u1)) #directory (returns all avaialble methods/attr inside class)
u1.display()
u2 = Student()
u2.display()

#Student class for multiple objects
class Students:
    """Understanding the usage of OOP"""
    name = input("Enter the name:")
    id = input("Enter the ID No:")
    gender = input("Enter the Gender")
    email_id = input("Enter the Mail id:")
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail id is {self.email_id}')
u1 = Students()
u1.display()
u2 = Students()
u2.display()
print(u1.__dict__) #it returns empty dictionary
print(u2.__dict__) #it returns empty dictionary

#Students details with multiple objects
class Students:
    """Understanding the usage of OOP"""
    def data(self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail id is {self.email_id}')
u1 = Students()
u1.data("Saketh","CGH3124","male","saketh@codegnan.com")
u1.display()
print(u1.__dict__)
u2 = Students()
u2.data("Akash","CGH1234","Male","akash@gmail.com")
u2.display()
print(u2.__dict__)

#Create a class with Car Brand name,price,color --> display()
'''
class Cars:
    """Understanding the usage of OOP"""
    def car_data(self,brand,name,price,color):
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color
    #Methods(behaviour)
    def details(self):
        print(f'Car Brand is {self.brand}')
        print(f'Car Model name is {self.name}')
        print(f'Car Color is {self.color}')
        print(f'Car Price is {self.price}')
u1 = Cars()
u1.car_data("BMW","Sedans",color="White",price="50lakhs")
u1.details()
u2 = Cars()
u2.car_data("MarutiSuzuki","Swift",color="Blue",price="8Lakhs")
u2.details()
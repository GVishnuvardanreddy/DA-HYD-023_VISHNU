'''
OOP -->class (attributes,methods (Constructor,Instance Method)),
object creation/utilisation -->Encapsulation,Inheritance,Polymorphism
OOP --> Abstraction,Usage of Class methods,Static Method

#Class methods --> these are termed by using @classmethod decorator
It applies for entire class level data,thereby every object utlisation
will be modified..

#lets work on an example related to Ecommerce

class Ecommerce:
    """Usage of classmethod & class attribute"""
    company = "Flipkart" #class attribute
    delivery_charge = 50 #class attribute
    @classmethod
    def update_delivery(cls):
        cls.delivery_charge = 100
        print(f'New Delivery Charges {cls.delivery_charge}')
Product = Ecommerce()
print(Product.company)
print(Product.delivery_charge)
print(Ecommerce.company) #classatrributes can be directly accessed using class name
print(Ecommerce.delivery_charge)
Product.update_delivery() #accessing classemethod
print(Product.delivery_charge)
Mobile = Ecommerce()
print(Mobile.delivery_charge)

#Applying Inheritance and usage of classmethod,classattributes
#banking scenario --> RBI -->SBI,HDFC....
class RBI:
    """Inheritance usage and Classemethod"""
    available_cash = 5000000 #classattribute
    @classmethod
    def rbi_cash(cls):
        print(f'Available Cash with RBI is {cls.available_cash}')
class SBI(RBI):
    pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash = 3000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        #print(f'Total cash is {cls.cash+cls.available_cash}')
        print(f'Total cash is {HDFC.cash + RBI.available_cash}')
#a = SBI()
#print(a.available_cash)
#a.rbi_cash()
#SBI.rbi_cash() #we can also access with classname directly
b = HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash()
b.hdfc_cash()

class RBI:
    """Inheritance usage and Classemethod"""
    cash = 5000000 #classattribute
    @classmethod
    def rbi_cash(cls):
        #print(f'Available Cash with RBI is {cls.cash}')
        print(f'Available cash with RBI is {RBI.cash}')
class SBI(RBI):
    pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash = 3000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total cash is {cls.cash + RBI.cash}')
a = HDFC()
print(a.cash)
a.hdfc_cash()
a.rbi_cash() 
#If incase as above scenario we have same name for class attributes in
#both parent and child classes,the best approach is to call
#the class attributes is using class names such as (RBI.cash)
'''
#Static Method -->It doesnot depend either on the object or to the class.abs
#we can create it using @staticmethod decorator
#it is mainly used as utility or helper functions
'''
class Ecommerce:
    """Usage of Static Method"""
    @staticmethod
    def free_delivery(price):
        return price>500
u1 = Ecommerce()
print(u1.free_delivery(450))
print(u1.free_delivery(1000))

#Now lets relate both class method and staticmethod in a single use
class Ecommerce:
    """Usage of class&static method"""
    platform = "Flipkart" #classattribute
    @classmethod
    def show_platform(cls):
        print("Welcome to the Platform:")
        print(f'{cls.platform}')
    @staticmethod
    def free_delivery(price):
        #return price>500
        if price > 500:
            print("You are eligible for Free Delivery")
        else:
            print("You need to pay Delivery charges")
user = Ecommerce()
#print(user.platform)
user.show_platform()
print(user.free_delivery(450))
print(user.free_delivery(1200))
'''
#Abstraction : It is also one of the key feature of OOP,where it shows
#only the relevant details to the user and hides the implementation features
#Instagram --> Uploading photo,Upload video,Reel
#when we need all child classes to follow same pattern
#we have abc module to implement abstraction
import abc
from abc import ABC,abstractmethod
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
    '''def upload(self):
        print("Compressing the Picture")
        print("Edit the Picture")
        print("Photo uploaded sucessfully")'''
    pass #as we made upload as abstract method mandatory it has be followed
class Video(Content):
    def upload(self):
        print("Encoding the Video")
        print("Video Editing is in process")
        print("Video Uploaded Successfully")
class Reel(Content):
    def upload(self):
        print("Adding Effects to the Reel")
        print("Reel is Edited")
        print("Reel is Uploaded Successfully with tags..")
'''Contents = [Photo(),Video(),Reel()]
#print(Contents)
for content in Contents:
    content.upload()'''
#obj = Photo()
#print(obj) #TypeError as we are not following the upload pattern
a = Video()
print(a.upload())














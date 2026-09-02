'''
Polymorphism --> It is also of one key feature of OOP,
Poly --> many
morph --> forms
Methods with same name can take different parameters (arguments-->list,numbers,...)
-->Method Overloading (compile time polymorphism)
-->Method Overriding (Run-time)
-->Operator Overloading (+,*) (__add__,__str__)

HotStar 
->Free User -->can watch the movies with advertisements
-->Premium User --> can watch premium content without advertisements
-->VIP User --> live content,streaming quality,premium content

#Method Overloading :

class HotStar:
    """Understand polymorphism"""
    def watch(self):
        print(f'User logged into Hotstar...Opening home page')
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
app = HotStar()
app.watch("Leo")
#app.watch() it returns error as watch() is overloaded 
'''
#1)Method usage with default arguments
#2)Method usage with variable length arguments (*args)
#3)Method usage with type of arguments
'''
class Hotstar:
    """Method usage with default arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f'User logged into Hotstar...checking..')
        else:
            self.movie = movie
            print(f'User started watching {self.movie}')
app = Hotstar()
app.watch()
app.watch("Vikram")

#Method Overloading using Variable length arguments
class Hotstar:
    """Method usage with variable length arguments"""
    def add_watchlist(self,*movies):
        print(movies)
        for movie in movies:
            self.movie = movie
            print(f'User watching {self.movie}')
app = Hotstar()
app.add_watchlist()
app.add_watchlist('Leo','Vikram','Maa Inti Bangaram')

#method overloading with type of arguments usage
#Hotstar ---> one movie at a time
         --> multiple movies at a time

class HotStar:
    """Method Overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print('Playing Playlist')
            for movie in content:
                print(movie)
app = HotStar()
app.watch('leo')
app.watch(['Leo','Vikram','Spiderman'])

#method overriding --> 
# It happens in the scenario of Inheritance ,where if child class
is having method name same as parent class thats where overriding happens
#we can use super() or if we create different objects

class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage....")
class PremiumUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
obj = PremiumUser()
obj.watch("Vikram")
obj2 = Freeuser()
obj2.watch()

In above usecase we can create different objects to access same method
but in real scenario what if similar to Subscription plans

class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage....")
class PremiumUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        #super().watch() #calling superclass method
        self.movie = movie
        print(f'User watching {self.movie}')
        super().watch()
obj = PremiumUser()
obj.watch("Loki")


#Operator Overloading --> Operators (+,-,*,/) --> Operators will behave
in a different way as per user defined objects...

# + (Addtion,Concatenation,Merging)

print(3+4)  #Addition
print('code'+'gnan') #Concatenation
print([23,45]+[4,5]) #Merging

#print(3.__add__(4)) #__add__(self,other)
a = 25;b = 3
print(a.__add__(b))
a = [12,3,4,];b = [3,4,5]
print(a.__add__(b)) #Merging
print(a.__len__()) #len(a) 
print(a.__mul__(2)) #print([12,3,4]*2)
'''

#let's apply the above scenario HotStar WatchHistory
'''
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
varun = WatchHistory(100)
print(varun.hours)
akash = WatchHistory(120)
print(akash.hours)
#print(varun + akash) #TypeError unsupported operation
print(varun.hours + akash.hours)
'''

#But the preferable way is usage of __add__()
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours 
    def __str__(self):
        return f'WatchHistory is {self.hours}'
varun = WatchHistory(300)
print(varun) #__str__() method
print(varun.hours)
akash = WatchHistory(50)
print(akash)
print(varun + akash)
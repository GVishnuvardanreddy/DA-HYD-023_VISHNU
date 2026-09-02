import aug29
print(dir(aug29))
'''print(type(aug29.details))
print(type(aug29.greeting))

print(aug29.greeting())
print(aug29.details)
#we can access functions/datatypes using . operator

aug29.details['subjects'] = ['Python','SQL','EDA','PowerBI','Excel','Stats']
print(aug29.details.keys())'''

#we can use from keyword to access desired methods/datatypes
'''from aug29 import details
print(details)
#print(greeting()) as we didnot import it raises NameError

details['subjects'] = ['Python','SQL','EDA','PowerBI','Excel','Stats']
print(details)

#we want to access group of methods/datatypes we can use comma
from aug29 import details,greeting
print(greeting())
print(details)

#you want to access all functions from a module at a time
#* is recommended only for user defined modules
from aug29 import *
print(details)
print(greeting())

#Aliasing -->we use as keyword as shortcut for original file
import aug29 as mod
print(mod.details)'''

#we will work on some built-in modules --> random, math

import random
import time
#random module --> get random number generation,random text
print(dir(random))
#OTP generation
#print(random.randint(1,10))
'''for i in range(5):
    print(random.randint(1000,9999)) #start limit,endlimit
    time.sleep(5) #delays exection sleep(seconds)

print(random.random()) #returns a float value of random 

details =['A long back','Once upon a time','Apatloo','Ten years ago']
print(random.choice(details))

#You can try for story generation using choice --> try in practice..
'''
#math module -->Mathematical constants,log,exp,trignometric..abs

import math
#print(dir(math))
print(math.ceil(4.5)) #returns the next higest value
print(math.floor(4.78))
print(math.factorial(5))
print(math.pi) #returns pi value
print(math.gcd(5,3)) #returns Greatest Common Divisor
print(math.trunc(4.95))










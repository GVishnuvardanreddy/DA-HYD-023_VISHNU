'''
Functions -->Arguments Usage (Variable length arguments)
        -->Keyword variable length arguments (**kwargs)

Exception Handling / Scope of variables /Built-in Functions

Exception handling -->It is a mechanism that helps to respond or make the
flow of execution in normal way,without this errors will occur and disrup the
flow of program

Common Exceptions -->ValueError,TypeError,IndexError,AttributeError,
ZeroDivisionError...

Syntax:

try:
    #code that will cause the exception
except Exception as e:
    #code will catch the exception
finally:
    #runs irrespective of try/except...
    ....


#basic Exception handling
try:
    #a = 10
    a = int(input("Enter the value:"))
    result = 20/a
    print(result)
    #print(resul) #check for NameError
#except Exception as e:
    #print(e) #it returns the msg of error
except ValueError: #check by changing case
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of variable properly')

#Similarly if we want to check other Errors ->IndexError,AttributeError
#Multiple Exception Handling
try:
    a = [10,20,30]
    a.apped(24)
    print(a[5])
#except Exception as e:
    #print(e) #returns the message of Error
except IndexError:
    print(f'Check the length of list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')


def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    #print(result)
    #return result
    for key,value in b.items():
        print(f'key is {key}')
        print(f'Value is {value}')
    return result
print(sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place = "hyd",
       batch = "da23"))

#handling exceptions at a time
try:
    a = [10,20,30]
    a.apped(24)
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a = list(map(int,input("Enter").split(','))) #only for understanding
    print(a)   

#BMI --> bmi = (weight) / ((height)**2)
#Feet --> 12 inches --> 1 inch -> 2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        #write my logical condition
        if weight > 0 and height > 0:
            break #stops the flow of execution of program
            #continue #skips the current iteration and proceed for rmng iteration
            #print("Bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print(f'Make sure to enter weight as integer only,\
              height also as number')
bmi = ((weight) / (height)**2)           
print(bmi)

#Use Exception Handling along with Jumping Statement in
#Functions BMI Task
'''

#Scope of Variables --> Scope is basically the region/area where it is
#accessible
#Local Scope,Global Scope
#Global Keyword,Enclosing Scope(Nested Functions nonlocal keyword)
'''

#Local Scope -->variables defined inside the function accessible inside

def display():
    """Usage of Local Scope"""
    name = "Codegnan" #local variable
    print(name)
display()
#print(name) #it raises NameError 

#Global Scope(variables) -->Defined outside and can be accessible anywhere
#in the script

place = "Hyderabad" #global variable
def display():
    """Usage of Local&Global Scope"""
    name = "Codegnan" #local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

#Modifying global variable inside the function and accessible outside the func
count = 20
def data():
    """Usage of global keyword"""
    global count
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')

#Local variable has high priority over global variable
count = 20
def data():
    """Priority of local vs global variable"""
    count = 5 #local variable
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')

#Enclosing Scope (nonlocal keyword)

def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Funtion"""
        nonlocal count
        count = count + 10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()
'''
#Built-in functions -->variales BuiltinScope
len = 56
print(len+4)


print(len('codegnan')) #TypeError -->Never ever use Builtin functions as Identifiers















        































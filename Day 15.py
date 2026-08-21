'''
Functions --> Variable length arguments (*args)
          --> Keyword Variable length arguments (**kwargs)

variable length arguments --> The number of positional arguments are not limit
we can pass any number of positional arguments, but we need to use * representation,data is
stored in tuple.


def sample(*args):
    """Simple demo for args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,5,6) #any number
sample('codegnan','manasa',29)
details = [24,45,35,65]
sample(details) #passing a collection
sample(*details) #unpacking values from collection

a,b,c = 13,4,'da'
print(a,b,c)
#a,*b,c = 'python','codegnan',23,45,9.7,'data'
a,b,*c = 'python','codegnan',23,45,9.7,'data'
a,b,*c = 34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)


#Task -->we wanted to calculate the sum of given objects using Function
def add(*a):
    """Sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result = 0 
    for i in a:
        if type(i)== float or type(i) == int:
            print(i)
            result = result + i
    return result
print(add())
print(add(12,3,4,5))
print(add(1,2,3,4.5))
print(add(3,4,5,'poll','dear',4.5))
b = list(map(int,input("Enter the value:").split()))
print(add(*b)) #* is used to unpack the values from collection
print(b)
print(*b)
for i in b:
  print(i,end= ' ') #same as here
'''
'''
#keyword variable length arguments --> We can pass any number of keyword
#arguments we use ** representation

def details(**kwargs):
    """Usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details() #retruns empty dictionary
#details(2,3,4,6) #raises TypeError
details(name="codegnan",place="hyd",batch="da")
batch = {'number': 'da23','place': 'hyd'}
details(**batch)
'''
'''
#Now let us include both of them into a function 
def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    #print(result)
    for key,value in b.items():
        print(f'key is{key}')
        print(f'Value is {value}')
        print(result)
sample(2,4,5,'police','codegnan',3.5,
       name = "codegnan",
       place = "hyd",
       batch ="da23")
#sample(name="codegnan",23,ids=23445) #positional args follows keyword args
'''
'''
#FUNCTIONS TASKS 19-08-2026

#Task 1 Student Grade Calculater
def calculate_grade(mark):
  if mark >= 80:
     return  ("A")
  elif mark >= 60:
    return  ("B")
  elif mark >= 40:
    return  ("C")
  else:
    return ("fail")
for i in range(3):
    mark = int(input("enter mark:"))
    grade = calculate_grade(mark)
    print("mark:", mark, "grade:", grade)
'''
'''
#Task2 shopping Bill Calculator
def calculate_bill(price,quantity = 1, discount = 0):
    subtotal = price * quantity
    discount_amount = subtotal * (discount/100)
    finalamount = subtotal - discount
    return(finalamount)
print(calculate_bill(100))
print(calculate_bill(100,3))
print(calculate_bill(100,3,10))
'''
'''
#Task3 - BMI Calculator

def calculate_bmi(weight,height):
    bmi = weight/(height * height)
    return bmi
def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
for i in range(3):
     name = input("Enter name: ")
     weight = float(input("Enter weight in kg: "))
     height = float(input("Enter height in metres: "))

     bmi = calculate_bmi(weight, height)
     status = bmi_status(bmi)

     print("Name:", name)
     print("BMI:", round(bmi, 2))
     print("Category:", status)
'''
'''    
#Task4 Marks Summary Using *args
def mark_summary(*args):
    if not args:
        return 0,0.0
    total =0
    for mark in args:
        total = total +mark
    average = total/len(args)
    return total,average
print(mark_summary())
print(mark_summary(85))
print(mark_summary(10,10,10))
'''

#Task 5: Employee Details Using **kwargs

def display_employee(**kwargs):
    # Display all employee details
    for key, value in kwargs.items():
        print(key, ":", value)

    # Check salary
    if "salary" in kwargs:
        print("Salary is available")
    else:
        print("Salary is missing")

    # Check department
    if "department" in kwargs:
        print("Department is available")
    else:
        print("Department is missing")

    print("--------------------")


# Employee 1
display_employee(
    name="Manasa",
    age=22,
    salary=30000,
    department="IT"
)

# Employee 2
display_employee(
    name="Pandu",
    age=20,
    salary=35000
)






















    

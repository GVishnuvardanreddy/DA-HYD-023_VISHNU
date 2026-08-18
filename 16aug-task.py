#Question 1: Student Marks Manager
'''
marks=[]
for i in range(3):
    mark=int(input('enter the marks:'))
    marks.append(mark)

marks.insert(0,90)
marks.extend([75,85])
a=(75 in marks)
#print(a)
if a == True:
    marks.remove(75)
print("removed value is:",marks.pop())

print(marks)
print(len(marks))
'''

#Question 2: Number List Analyser

'''
numbers=[20, 10, 30, 20, 40, 20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
search=int(input('enter the number:'))
if search in numbers:
           print('Number found')
           print('count of the search number:',numbers.count(search))
           print('index:',numbers.index(search))
else:
    print('not found')
print('minimum number is:',min(numbers))
print('maximum number is:',max(numbers))   
print('sum of all numbers is:',sum(numbers))        
'''

#Question 3: Even and Odd Number Separator 

'''
numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print('Even list:',even)
print('Odd list:',odd)
#slicing
print('first three:',numbers[:3])
print('last three:',numbers[-3:])

backup_list=numbers.copy()
print('backup_list:',backup_list)
numbers.clear()
print('original list:',numbers)
'''


#Question 4: Unique Name Manager


'''
names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
set_names=set(names) #Asha, Rahul, John
print(set_names)

set_names.add("Meera")
print(set_names)
set_names.update(("Arun","priya"))
print(set_names)
if "John" in set_names:
    set_names.remove("John")
    #print(set_names)

    set_names.discard("David")
    print(set_names)
for i in set_names:
    print(i)
'''

#Question 5: Course Student Comparison

python_students = {"Asha", "Rahul", "John", "Meera"} 
da_students = {"Rahul", "Meera", "Arun"}

'''
students=python_students.union(da_students)
common=python_students.intersection(da_students)
difference=python_students.difference(da_students)
#difference=da_students.difference(python_students)
sym=python_students.symmetric_difference(da_students)
print(da_students.issubset(python_students))
print(python_students.issuperset(da_students))
print(python_students.isdisjoint(da_students))
print(students)
print(common)
print(difference)
print(sym)
'''

all_students = python_students.union(da_students)
print("Students from both courses:")
for student in all_students:
    print(student)


both = python_students.intersection(da_students)
print("\nStudents learning both courses:")
for student in both:
    print(student)


only_python=python_students.difference(da_students)
print("\nStudents learning only python courses:")
for students in only_python:
    print(students)


only_DataAnalysis=da_students.difference(python_students)
print("\nStudents learning only Data Analysis courses:")
for students in only_DataAnalysis:
    print(students)
    
one_course=python_students.symmetric_difference(da_students)
print("\nStudents learning only one courses:")
for student in one_course:
    print(student)

if da_students.issubset(python_students):
    print("\nDA is a subset of Python: True")
else:
    print("\nDA is a subset of Python: False")

if python_students.issuperset(da_students):
    print("Python is a superset of DA: True")
else:
    print("Python is a superset of DA: False")

if python_students.isdisjoint(da_students):
    print("The sets are disjoint: True")
else:
    print("The sets are disjoint: False")

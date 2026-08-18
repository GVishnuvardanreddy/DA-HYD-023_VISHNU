
#task------>1
'''
marks=[]
for i in range(3):
    x=int(input("Enter the marks: "))
    marks.append(x)
print(marks)
marks.insert(0,90)
marks.extend((75,85))
print(marks)
if 75 in marks:
    marks.remove(75)
print("Poped value: ",marks.pop())
print("Final list:",marks)
print("Length of the list:",len(marks))
'''


#task--------->2
'''
numbers=[20,10,30,40,20]
print(numbers)
numbers.sort()
print("ascending order list:")
for i in numbers:
    print(i)
numbers.reverse()
print("descending order list:")
for i in numbers:
    print(i)
x=int(input("Enter the number: "))
if x in numbers:
    print("count and index: ",numbers.count(x),numbers.index(x))
print("minimum number in the list:",min(numbers))
print("maximun number in the list:",max(numbers))
print("sum of the list:",sum(numbers))
'''

#task---->3
'''
numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list:",even)
print("odd list:",odd)
print("first 3 numbers:",numbers[:3])
print("first 3 numbers:",numbers[3:])
copy_numbers=numbers.copy()
numbers.clear()
print("original numbers:",numbers)
print("copy numbers:",copy_numbers)
'''

#task---->4
'''
names=['Asha','Rahul','Asha','John','Rahul']
x=set(names)
print(x)
x.add('Meera')
print(x)
x.update(("Arun","Priya"))
print(x)
if 'John' in x:
    x.remove("John")
print(x)
x.discard('John')
for i in x:
    print(i)
'''

#task------>5
'''
python_students={'Asha','Rahul','Meera','John'}
da_students={'Asha','Meera','Arun'}
x=python_students.union(da_students)
print('total students:')
for i in x:
    print(i)
y=python_students.intersection(da_students)
print('students who are taking both course:')
for i in y:
    print(i)
z=python_students.difference(da_students)
print("students who taking only python course:")
for i in z:
    print(i)
a=python_students ^ (da_students)
print("students who taking only one course:")
for i in a:
    print(i)

print('is the da set is a subset of python set???:',da_students.issubset(python_students))
print('is the da set is a superset of python set???:',da_students.issuperset(python_students))
print('is the da set is a subset of python set???:',da_students.isdisjoint(python_students))
'''
                      #or#
'''
if da_students.issubset(python_students):
    print('da set is the subset of python set')
else:
    print('da set is not subset of python set')

if da_students.issuperset(python_students):
    print('da set is the superset of python set')
else:
    print('da set is not superset of python set')

if da_students.isdisjoint(python_students):
    print('da set is the disjoint of python set')
else:
    print('da set is not disjoint of python set')
'''




















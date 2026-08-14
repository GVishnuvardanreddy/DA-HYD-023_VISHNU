'''
Sequences --> Strings,Lists,Tuples,Set,Frozenset
Mapping -> Dictionary
'''
#Sets --> A Set is a Unique Collection of objects,Unordered,Mutable,
#Hashing,Unindexed,Unique,Heterogenous 
#set(),{}
#a = {} its an empty dictionary
'''a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #TypeError

print(234 in stud_ids)
#print(stud_ids *2) #Set can't be repeated
#print(stud_ids + stud_ids) #Two sets cannot be Merged

#data = {12,3,4,5,[12,3,4],'saketh'}
#print(data) #No lists inside a Set (hashing technique) Lists are Mutable

data = {12,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)
'''
#Methods on sets -->add(),update(),remove(),discard(),pop()
names = {'sai','saketh','kiran','codegnan'}
#print(len(names))
#add() will insert an element into the set (it can be anywhere but only unique)
names.add('python')
#print(names)
#names.add('saketh','poll')
#print(names)
names.add(('poll','police'))
print(names)
da_names = {'mani','akash','sai','sonu'}
print(da_names)
#update() we can update multiple elements (set)
'''names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))

#remove(),discard(),pop(),clear()
#remove() removes an element from the set (it must be a member)
da_names.remove('sai')
print(da_names)
#da_names.remove('Sai') #KeyError
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')

da_names.pop()
print(da_names)
print(da_names.pop()) #removes and returns an arbritrary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('Saira')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)

#copy() #creates a shallow copy of set (independent of each other)
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''
#mathematical operations -->union(),intersection(),difference(),symmetric_difference()
#issubset(),issuperset(),isdisjoint()

da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
#event = da_23.union(da_24)
'''event = da_23 | da_24 #| union()
print(event)
print(len(event))
#common = da_23.intersection(da_24)
common = da_23 & da_24 #&  intersection()
print(common)
#print(len(common))
common = da_23.intersection_update(da_24)
print(common) #it returns None 
print(da_23) #common elements are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and prints rmng elements from first set
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23 - da_24
#print(f)
#symmetric_difference() -->removes common elements and prints all rmng
#elements from two sets
symm = da_23.symmetric_difference(da_24)
#print(symm)
h = da_23 ^ da_24
#print(h)

#issubset() -->checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))
'''
#Length of Unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids

n = int(input())
student_ids = input().split()
#print(student_ids)
result = set(student_ids)
print(len(result))































































































































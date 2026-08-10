'''
Strings --> CaseConversions,Searching & Finding,String testing methods,
Replace,Space removal
'''
#Searching,Finding,Replacing,Joining...
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))
'''
b = a.index('g') #it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('n',6) #it returns the next occurance
print(d)
#e = a.index('n',8) #ValueError
#print(e)
#f = a.index('t') #ValueError
#print(f)
g = a.index('n',1,4)
print(g)

#rindex() --> returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns ValueError
#print(d)

#count() -->returns the number of items object is repeating

print('Codegnan'.count('n'))
print('Code'.count('w')) #it returns 0 as we dont have 'w' in 'Code'
print('Cakshjasaksajs'.count('a'))

#find() -->first occurance but it avoid error returns -1 if substring is
#not found
print('codegnan'.find('r')) #it returns -1

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))

a = "Data"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))


#Replacing,Splitting,Joining

#Strings are Immutable
a = 'Codegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('fghyujiki#jkasjkajska#nmasnam'.replace('#',''))
print(a.replace('x','saketh'))

a = 'code saketh python'
print(len(a))
b = a.split() #by default if we have space it splits (returns list)
print(b)
print(len(b))
c = 'code,saketh,python'
d = c.split()
print(d)
e = c.split(',')
print(e)

#join(iterable) -->concatenate any number of strings

a='code'
b ='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('saketh'))
print(' '.join('saketh'))

#String testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower().....

a = 'Codegnan123'
print(a.isalnum()) #returns True for alphanumeric strings else False
b ='Codegnan'
print(b.isalnum())
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True only for digit string
print('8106429771'.isdigit())
print('2345'.isnumeric()) #this has upper edge (numbers,fractions,romans)
#startswith() -->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower()) #returns True for all lowercase
print('COdegann'.isupper()) #returns True for all uppercase
print('Codegnan Python'.istitle())

#Space removal --> strip() (removes leading and trailing spaces)

a=' codegnan '
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#center(),ljust(),rjust() -->Alignment of strings (check length and then
#modify the width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#')) 
print('hai'.rjust(6,'#'))

































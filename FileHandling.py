'''
File Handling in Python : Files are mainly used to store the data
It supports --> r,w,a (read,write,append) using open() 
'''
#First lets understand how we can access .txt files using Python
'''
import os
if os.path.exists('sample.txt'):
    file = open('sample.txt','r')
    print("File is loaded Successfully")
else:
    print("File not present")


#Now let us access the content from the file
file = open('sample.txt','r')
#print(file)
#print(file.read()) #reads the entire content from the file
#print(type(file.read()))
#a = file.read()
#print(a)
#print(len(a)) #assign to a variable and check the length and apply desired functions
#readline(),readlines()
print(file)
#print(file.readline()) #reads single line from the file
print(file.readlines()) #reads all lines from the file in a list
'''

#'w' mode --> It automatically creates a new file,if the file is existing
#it overrides the content in it
'''
file = open('data.txt','w')
print(file)
#as the file is automatically create lets write content to it
file.write("Good Afternoon guys,how are you doing?")
file.write("Today is Wednesday..")
file.close()

#we can also with keyword to avoid close()
with open('data.txt','w')as f:
    f.write("Now checking what happened")

#'a' --> it also automatically creates a file,but if the file is already
#existing it appends the content to the previous file

with open('data.txt','a') as g:
    g.write('\n Okay let us see how its going')

#+ --> read and write
with open('data.txt','r+')as h:
    print(h.read())
    h.write("Today is Wednesday")
#In the above case we can perform both read and write operations

#File operations size and path
import os
file='data.txt'
if os.path.exists('data.txt'):
    print("File size is",os.path.getsize('data.txt'),"Bytes")
    print("File Absolute path is",os.path.abspath('data.txt'))
else:
    print("File is not present")
'''

#If your project is requiring File Handling use it... 
#Tokens --> Operators --> Control Statement(for,while,if,else,elif,break,continue)
#POP (Functions(*args/**kwargs)) -->OOP
#Data Analysis --> Numpy,pandas,Data Visualization
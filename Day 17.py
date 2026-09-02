'''
OOP-->>Object oriented programming
An Object programming is a mechanism or a process which revolves creating a objects.
It consits of 2 important procedures
1)Attributes-->> or Data which carry data to the class.
2)Methos-->> A is a function is defined inside the class, which carry behaviour of the objects.
example:
chair(object)-->>wood,tools,Dimensions(blueprint),carpenter.
A class a blue print of the object
****Features of OOP -->> Modularity,scalability,Encapsulation
Encapsulation(binding the data(attributes),features of the class)(objects)
***Abstract-->>show only the relevent information to the class
**Inheritence-->>Acquring properities(Attributes,Methods)
single-->>Fingerprint
Multiple-->>parents(mother,father)-->>child
multi-level--->>>grandparent-->>parent-->>child
**polymorphism-->>method overloading,method overriding,operator overriding
'''

#syntax for class creation:
'''
class Class_Name:
    
    attributes(characteristices)
    ......
    def func(self):(behaviour)
        ......
        .....
    .....
obj=Class_Name()
'''
#Student class with basic details
'''
class student:
    name='venky'
    id='CGH4052'
    gender='male'
    email_id='venkateshvalmiki864@gmail.com'
    #Methods(behaviour)
    def display(self):
        print(f'student name is {self.name}')
        print(f'student id is {self.id}')
        print(f'student gender is {self.gender}')
        print(f'student email_id is {self.email_id}')
u1=student()
u2=student()
print(u1)
#print(dir(u1))
u1.display()
u2.display()
'''
#student class for multiple objects
'''
class students:
    name=input('enter the name:')
    id=input('enter the id:')
    gender=input('enter the gender:')
    email_id=input('enter the email_id:')
    #Methods(behaviour)
    def display(self):
        print(f'student name is {self.name}')
        print(f'student id is {self.id}')
        print(f'student gender is {self.gender}')
        print(f'student email_id is {self.email_id}')
u1=students()
#print(u1)
#print(dir(u1))
u1.display()
u2=students()
u2.display
print(u1.__dict__)#it returns empty dictionary
print(u2.__dict__)#it returns empty dictionary
'''
#students details with multipel objects 
class students:
    def data(self,name,id,gender,email_id):
        self.name=name
        self.id=id
        self.gender=gender
        self.email_id=email_id
    #Methods(behaviour)
    def display(self):
        print(f'student name is {self.name}')
        print(f'student id is {self.id}')
        print(f'student gender is {self.gender}')
        print(f'student email_id is {self.email_id}')
u1=students()
u1.data('venky','CGH123','male','venky@gmail.com')
u1.display()

u2=students()
u2.data('vamshi','CGH223','male','vamshi@gmail.com')
u2.display()
print(u1.__dict__)#it returns empty dictionary
print(u2.__dict__)#it returns empty dictionary




























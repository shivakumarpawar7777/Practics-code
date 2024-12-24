"""# Data type in python
1. Numaric type :- 
i. intager:- whole number worth can be any lenth like >>> 1, 99, 555, 9876   ........etc
ex:- 
age = 21
print(type(age)) 

ii. float :- float store drifting point number like >>> 1.9, 12.12, 9999.098 ......etc
ex:- 
precentage = 99.099
print(precentage)
print(type(precentage))

iii. complex:- complex numbers are represented useing the complex type. A complex consists of two ports: a real part and an imaginary part.
ex:- 
z = 5 + 7j
print(z)
print(type(z))
"""
#2. String:- a sequence of charecters inside single, duble and thriple quation.
#Ex:- 
#  single quation         |     duble quation        |         triple quation
#  'shiva'                |    "shiva"               |   #         """shiva"""              
#  name = 'shiva'         |    name = "shiva"        |   #         name = """shiva"""    |  name = """shiva
#  print(name)            |    print(name)           |   #         print(name)           |             laxman
#  print(type(name))      |    print(type(name))     |   #         print(type(name))     |                  pawar"""

"""
3. list:-  list is a sequence elements in between a square brakets [1,2,3,4,5], mutable data type.
note :- we can updata the data
ex:- 
number = [1,2,3,4,5,6,7,8,9,0]
print(number)
print(type(number))

4. tuple :- tuple is a sequence of charecters in between peranthesis (1,2,3,4,5,6,7,8,9,0,), it is a inmutable data type
note : -we connot updata the data.
ex:- 

tuple = (1,2,3,4,5,6,7,8,9,0,)
print(tuple)
print(type(tuple))

5. set :- set is a sequence of charecters in between curly braces {1,2,3,4,5,6,7,8,9,0} not allows duplicate values 
Ex:-
s = {1,2,3,4,5,6,7,8,9,0,1,2,3,4}
print(s)
print(type(s))  #output :- {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}     <class 'set'>
print("--------------")

s = set ()
s1 = {1,2,3,4,5,6,7,8,9,0,1,2,3,4}
print(s, s1)
print(type(s))

6. Dictionary :- storing element in the form of key and value pair.
note:- value my be dulicate blat not key.
ex:- 
d = {"name" : "shiva" , "age" : 25}
print(d)
print(type(d))

7. boaleanan :- True and False are two default values is called boolean.
ex:- 
print(type(True))
print(type(False))
"""



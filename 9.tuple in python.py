"""tuple :- tuple is a sequence of charecters in between peranthesis (1,2,3,4,5,6,7,8,9,0,), it is a inmutable data type
note : -we connot updata the data.
ex:- 

tuple = (1,2,3,4,5,6,7,8,9,0,)
print(tuple)
print(type(tuple))"""

# decleration of a tuple 
t = ("remu", 29.9888, 00, True)
print(type (t)) 
print(t)
print("--------")

# type elements to the tuple

#type conversion 
t = ("remu", 29.9888, 00, True)
it = list(t)
print(it)
it.append(2000)
print(it)
print(t)

#methods 
print(t.count("rama"))

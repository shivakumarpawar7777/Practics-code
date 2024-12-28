#2. String:- a sequence of charecters inside single, duble and thriple quation.
name = 'shiv'
name1 = "shiv"
name2 = """shiv"""

print(name)
print(name1)
print(name2)

print(type(name))
print(type(name1))
print(type(name2))
print("_________________________________")

name = "shivakumar"
print(name[1])
print(name[9])

print(name[-1])  # to fine the last value
print("_________________________________")

# slicing :- veriablename[startingdex : endingdex : stop]
name = "shivakumar"
print(name[0:6])     #shivak
print(name[0:6+2])   #shivakum
print(name[2:6])     # ivak
print(name[0:-1])    # shivakuma
print(name[0:-3])    # shivaku
print("_________________________________")

number = "1234567890"
print(number[0:10:2])   #13579
print(number[1:10:2])   #24680
print(number[0:10:3])   #1470
print(number[2:10:3])   #369



"""3. list:-  list is a sequence elements in between a square brakets [1,2,3,4,5], mutable data type.
note :- we can updata the data
ex:- """
number = [1,2,3,4,5,6,7,8,9,0]
print(number)
print(type(number))
print("-----------")
# removing elements from list
# pop():- removing & return last element from the list

ls = [1,2,3,4,5,6,7,8,9]
pop = ls.pop()
print(pop)
print(ls)

ls = ["as","sd","fg","hj","kl"]
pop = ls.pop()
print(pop)
print(ls)
print("-----------")

# remove():- remover specified element from the list
l = [10,20,30,40,50,60,70,80,90]
rm = l.remove(90)
print(rm)

#clear():- it will remove all element from list & return empty list
l = [10,20,30,40,50,60,70,80,90]
rm = l.clear()
print(rm)

# Ordering of lish 
#reverse()
n = [10,20,30,40,50,60,70,80,90]
n.reverse()
print(n)

# reverse a list using slicing
n = [10,20,30,40,50,60,70,80,90]
print(n[::-1])
print("-----------")

#sort()
n = [0,9,8,7,6,-5,4,-3]
n.sort()
print(n)

# aliasing & cloning
data = "student data"
data_copy = "student data"

x = [1,2,3,6]
y = x
print(id(x))
print(id(y))

y[1] = 20
print(id(x))
print(id(y))

# list comprekensin :- python program to find even numbre in a list

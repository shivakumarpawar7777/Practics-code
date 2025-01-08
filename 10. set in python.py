"""set :- set is a sequence of charecters in between curly braces {1,2,3,4,5,6,7,8,9,0} not allows duplicate values 
Ex:-
s = {1,2,3,4,5,6,7,8,9,0,1,2,3,4}
print(s)
print(type(s))  #output :- {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}     <class 'set'>
print("--------------")

s = set ()
s1 = {1,2,3,4,5,6,7,8,9,0,1,2,3,4}
print(s, s1)
print(type(s))"""

s = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,"set",1,2.3,3,4, True}
print(s)

s = {}
print((s))

"""# accesing 
s = {0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,"set",1,2.3,3,4, True}
print(s[0])"""

#adding elements to the set

s = {"preveen", "rama", "shiva", "kishor"}
s.add("pawar")
print(s)

s.remove("pawar")
print(s)
print("-----")

#Updata()
s = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,"set",1,2.3,3,4, True}
s1 = {"preveen", "rama", "shiva", "kishor", "pawar"}
s.update(s1)
print(s)

#removin element from the set
#rmove()
s = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,"set",1,2.3,3,4, True,"preveen", "rama", "shiva", "kishor"}

s.remove("preveen") # only one element can remove
print(s)


a
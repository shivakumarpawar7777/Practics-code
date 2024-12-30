#2. String:- a sequence of charecters inside single, duble and thriple quation.
name = 'shiv'
name1 = "shiv"
name2 = """shiv"""

"""print(name)
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
print("_________________________________")

#Membership checking in string 
# in and not in

s = "Hello welcome to world of python"
ss = "python"
print(ss in s )  #True
print(s in ss )  #False
print("_________________________________")

s = "Hello welcome to world of python"
ss = "java"
print(ss in s )  #False
print(s in ss )  #False
print("_________________________________")

s = "Hello welcome to world of python"
ss = "python"         #ss is available in s
if ss in s:
    print("ss is available in s") 
if ss not in s: 
    print("ss is notavailable in s")
print("_________________________________")

s = "Hello welcome to world of python"
ss = "java"         #ss is notavailable in s
if ss in s:
    print("ss is available in s") 
if ss not in s: 
    print("ss is notavailable in s")"""

#removing spaces from string 
#strip()
username = "shivakumar "
print(len(username))

ss = username.strip()
print(ss)
print(len(ss))
print("_________________________________")

#rstrip()
username = " shivakumar "
print(len(username))

rs = username.rstrip()
print(rs)
print(len(rs))
print("_________________________________")

#lstrip()
username = " shivakumar "
print(len(username))

ls = username.lstrip()
print(ls)
print(len(ls))
print("_________________________________")

#replace
s = "Hello welcome to world of python"
rp = s.replace(" ", "")
print(rp)

rp = s.replace(" ", "@")
print(rp)

rp = s.replace(" ", "$")
print(rp)

rp = s.replace(" ", "#")
print(rp)

rp = s.replace("python", "java")
print(rp)

rp = s.replace("welcome", "come")
print(rp)

# Finding of substring in main string 
#find():- return index position on substring in main string 
s = "welcome to world of python"
print(s.find("o"))

print(s.find("p"))
print(s.find("y"))
print(s.find("t"))
print(s.find("h"))
print(s.find("o"))
print(s.find("n"))
print("_________________________________")

#index():- returns index position on substring in main string 
s = "welcome to world of python"
print(s.index("w"))
print(s.find("l"))
print(s.find("e"))
print("_________________________________")

#split()
s = "welcome to world of python"
print(len(s))

ss = s.split()    #['welcome', 'to', 'world', 'of', 'python']
print(len(ss))
print(ss)

s = "welcome to world of python"
print(len(s))

ss = s.split("o")   #['welc', 'me t', ' w', 'rld ', 'f pyth', 'n']
print(len(ss))
print(ss)

ss = s.split("w")   #['', 'elcome to ', 'orld of python']
print(len(ss))
print(ss)
print("_________________________________")

#join()
l = ['welcome', 'to', 'world', 'of', 'python']
js = "-".join(l)
print(js)

js = "=".join(l)
print(js)

js = "+".join(l)
print(js)

js = "@".join(l)
print(js)

js = "#".join(l)
print(js)

js = "%".join(l)
print(js)

js = "*".join(l)
print(js)
print("_________________________________")

#changing case of a string : 5 method 
#1.upper():- converts all charectors into uppercase
s = "welcome to world of python"
print(s.upper())

#2.lower():- converts all charecters into lower
s = "WELCOME TO WORLD OF PYTHON"
print(s.lower())

#3.swapcase():- converta all lowercae into upper and all into lowercase
s = "welcome to world of python"
print(s.swapcase())

s = "WELCOME TO WORLD OF PYTHON"
print(s.swapcase())

#4.titile():- convert fist charecter into each word into uppercase
s = "welcome to world of python"
print(s.title())

s = "WELCOME TO WORLD OF PYTHON"
print(s.title())

#5. Capitaliza():- converts only fist charecter into uppercase

s = "welcome to world of python"
print(s.capitalize())

s = "WELCOME TO WORLD OF PYTHON"
print(s.capitalize())


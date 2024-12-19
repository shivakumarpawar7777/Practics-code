"""# function :- is a block statement that performa specific task
#Ex: 
def clac_sum(a,b):
    s = a+b    #  a-b or a*b or a/b...... 
    print(s)
    return s
clac_sum(2,2)


def calc_sum(y,z):
    return y-z   #  a+b or a*b or a/b...... 
sum = calc_sum(10,5)
print(sum)

# avarage of 3 numbers 
def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(sum)
    return avg
calc_avg(98, 97, 95)"""

# two type of function 1.Build in function   2.user defined function
# Default parameter:- assigning a defalult value to parameter, which is used when no argument is parsed

def cal_peod(a=5, b=5):
    print(a*b)
    return a*b 
cal_peod()
print("-----------------")

# lets practies
#1. WAF to print the length of a list (list is the parameter)

cities = ["delhi", "Bengluru", "Hyderbad", "pune","Mumbai"]
numbers = [1,11,13,2,3,44,55,65,76,99]

def length_list(list):
    print(len(list))
length_list(cities)
length_list(numbers)

# WAF to print the elements of a list in line. (list in the parameters)
cities = ["delhi", "Bengluru", "Hyderbad", "pune","Mumbai"]
Heroes = ["thor", "ironman", "captain", "shaktiman"]
numbers = [1,11,13,2,3,44,55,65,76,99]

def elements_line(list):
    for item in list:
        print(item, end=" ")   # end = " " (it will in horizontal line all the elements)

elements_line(cities)
elements_line(Heroes)
elements_line(numbers)
print("-----------------------")

def elements_line(list):
    for item in list:
        print(item)   # it will print all the elements in vertical line

elements_line(cities)
elements_line(Heroes)
elements_line(numbers)

print("__________________")
#3. WAF to find the factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)    #1*2*3*4*5 = 120
cal_fact(6)    #1*2*3*4*5*6 = 720
cal_fact(7)    #1*2*3*4*5*6*7 = 5040

#4. WAF to convert USD to INR
def convert(UDS):
    INR = UDS * 83
    print(UDS, "USD = ", INR, "INR")

convert(1)
convert(2)
convert(500)
convert(999)


def odd_no_or_even_no(n):
    if n % 2 == 0:
        return "even number"
    else:
        return "odd number"
        
print(odd_no_or_even_no(2))
print(odd_no_or_even_no(3))
print(odd_no_or_even_no(888))
print(odd_no_or_even_no(999))


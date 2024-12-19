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





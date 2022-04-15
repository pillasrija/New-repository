print(len("python"))
print(len([1,2,3,4,5,6]))

def length(container):
    counter=0
    for i in container:
        counter+=1
        return counter
    print(length("python"))

# reverse function
s="python"
print(s[::-1])
def reverse_of_string(str1):
    return str1[::-1]
print(reverse_of_string("python"))


def hello():
    return("hello world")
print(hello())

def employee_details(emp_name,emp_job):
   return"employee_name is {}and his job is {}".format(emp_name,emp_job)
print(employee_details("madhu","automation developer"))

def employee_details(emp_name,emp_job,location="india"):
    return"employee_name is {}and his job is {},he stays in {}".format(emp_name,emp_job,location)
print(employee_details("madhu","automation developer","vizag"))
print(employee_details(emp_job="dev",emp_name="srija"))



def print_arguments(*args):
    print(args,type(args))
    print(args[0])
print_arguments(1,2,3,4,5,6,7,8,9,10)

def print_keyward_args(**kwargs):
    print(kwargs, type(kwargs))

print_keyward_args(emp_name="madhu",emp_salary=50000,emp_dept="dev")

def outer(a, b):
     return a+b
print(outer(5,4))


def count_down(num):
     if num <= 0:
        print("stop")
     else:
        print(num)
        count_down(num-1)

count_down(4)

import time
def fun():
    print("apple")
    time.sleep(1)
    fun()

fun()


def fun(n):
    if n > 0:
        print(n)
        fun(n-1)

fun(5)
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(6))


x = 100
# print(globals())

def my_func():
    global x
    x+=42
    print(x)

my_func()
print(x-10)

#enclosing scop
def f1():
    x=45
    def f2():
        x = 0
        print(x)
    f2()
    print(x)

f1()


def f1():
    x=55
    def f2():
        nonlocal x
        x=45
        print(x)
    f2()
    print(x)

f1()

def hello1():
    print("hello word")
def hello2():
    print("hello srij")
def greet(func):
    func()

greet(hello1)
greet(hello2)

def outer_func():
    def inner_func():
        print("inner_func")
    inner_func()
outer_func()


#returning a function

def greet():
    def hello(name):
        print("hello,my name is {}".format(name))
    return hello

greet_user=greet()
greet_user("srija")

# simple decorator

def decorate_function(func):
    def wrapper():
        print(" This is before executing the function ")
        func()
        print(" This is after executing the function ")
    return wrapper
@decorate_function
def hello():
    print("Hello srija")
decorate_function(hello())

def stars(func):
    def inner(*args,**kwargs):
        print("*"*30)
        func(*args,**kwargs)
        print("-"*30)
    return inner

@stars
def hello():
    print("hello srija")
hello()

def cal_square(numbers):
    result=[]
    for number in numbers:
        result.append(number**2)
    return result

def cal_cube(numbers):
        result = []
        for number in numbers:
            result.append(number**3)
        return result
print(cal_square(range(1000)))
print(cal_cube(range(1000)))


import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("function cal_square has taken{}micro seconds".format(str((end-start)*1000)))
        return result
    return wrapper

@timer
def cal_square(numbers):
    result=[]
    for number in numbers:
        result.append(number**2)
    return result
@timer
def cal_cube(numbers):
        result=[]
        for number in numbers:
            result.append(number**3)
        return result

cal_square(range(1000))
cal_cube(range(100000))






















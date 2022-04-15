students=['divya','srija','dundi','montu']
for student in students:
     print(student)

ls=[1,2,3,4]
print(dir(ls))

l1=[1,2,3,4,5]
l2=iter(l1)
print(l2)
l3=iter(l2)
print(l3)
print(l2==l3)
print(l2 is l3)

#text sequence type str
a="welcome to python training"
b=iter(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))

a=range(1,10)
print(a)
print(type(a))
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))


dictionary

a={'a':1,'b':2,'c':3,'d':4}
b=iter(a)
b=iter(a.values())
b=iter(a.items())
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#file objects

with open('sample.txt')as i_data:
    print(i_data.readlines())
    print(i_data.readlines())
    print(i_data.readlines())
    print(i_data.readlines())
    print(i_data.readlines())
    print(i_data.readlines())
    print(i_data.readlines())

def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

l1=[1,2,3,4,5]
t1=(1,2,3,4,5)
str1="srija"
dict1={'a':1,'b':2,'c':3}
num=100
for data_type in[l1,t1,str1,dict1,num]:
    print("{} is iterable {}".format(data_type,iterable(data_type)))

def my_sample_generator():
    yield 1
    yield 2
    yield 3

g=my_sample_generator()
print(next(g))
print(next(g))
print(next(g))
print(sorted(g))
print(sum(g))

def store_numbers_using_list(n):
    numbers=[]
    num=0
    while num<n:
        numbers.append(n)
        num+=1
    return numbers

def store_numbers_using_generator(n):
    numbers=[]
    num=0
    while num<n:
        yield num
        num+=1
    return numbers

print(sum(store_numbers_using_list(10)))
print(sum(store_numbers_using_generator(10)))
import sys
print(sys.getsizeof(store_numbers_using_list(10)))
print(sys.getsizeof(store_numbers_using_generator(10)))

import memory_profiler
m1=memory_profiler.memory_usage()
size_using_list=store_numbers_using_list(100000)
m2=memory_profiler.memory_usage()
diff_memory=m2[0]-m1[0]
print("memory usage is {}mb".format(diff_memory))
m1=memory_profiler.memory_usage()
size_using_generators=store_numbers_using_generator(100000)
















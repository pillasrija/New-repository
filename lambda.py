# def double_num(x):
#     return x*2
# print(double_num(x=3))
# print(double_num(x=4))
# print(double_num(x=5))


# doubler=lambda x:x*2
# print(doubler(x=3))
# print(doubler(x=4))
# print(doubler(x=5))

# multiple_paramers=lambda a,b,c:a+b+c
# print(multiple_paramers(2,3,4))

# max number
# multiple_params=lambda a,b,c:a if a>b and a>c else (b if b>a and b>c else c)
# print(multiple_params(2,4,5))


# even or odd numbers
# even_or_odd=lambda x:'even' if x%2==0 else'odd'
# print(even_or_odd(9))
# print(even_or_odd(22))

# add=lambda x,y,z:x+y+z
# print(add(2,3,4))
# print(add(x=2,y=5,z=4))

# add=lambda*args:sum(args)
# print(add(4,5,6,7))
#
# add=lambda**kwargs:sum(kwargs.values())
# print(add(a=5,b=6,c=7,d=9))

# numbers=[1,2,3,4,5,6,7]
# def square_of_num(number):
#     return number**2
# print(list(map(square_of_num,numbers)))
# print(list(map(lambda x:x**2,numbers)))

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# print(list(map(lambda a,b:((a+b)/2),l1,l2)))

# dict_of_names=[{'name':'madhu','dept':'qa'},{'name':'srija','dept':'dev'}]
# names=[]
# for item in dict_of_names:
#     names.append(item.get("name"))
# print(names)
# # print(list(map(lambda a:a.get("name"),dict_of_name)))

# students = ['dundi','montu','dumbu','abhi','avi']
# print([i.capitalize()for i in students])
# print(list(map(lambda str_item:str_item.capitalize(),students)))


# names=[
#     {'first':'lokesh','last':'sri'},
#     {'first':'astha','last':'venky'},
#     {'first':'jiu','last':'vsn'}
# ]
# print(list(map(lambda a:a.get("last"),names)))

# filter functions
# def check_age(age):
#     if age>18:
#         return true
#     else:
#         return false
# ages=[10,20,30,40,50,60,13]
# print(list(filter(lambda x:x>15, ages)))
# students=['thulasi','sagar','ajay','mahi']
# print(list(filter(lambda name:len(name)>5,students)))

# from functools import reduce
# # ls=[1,2,3,4,5]
# # summing =reduce(lambda x,y:x+y,ls)
# # print(summing)
#
#
# ls=[1,2,3,4,5]
# max_element=reduce(lambda x,y:x if x>y else y,ls)
# print(max_element)

users=[
    {"username":'usha',"tweets":["i love cake","i am good"]},
    {"username":'divya',"tweets":[]},
    {"username":'srija',"tweets":["india","python"]},
    {"username":'dundi',"tweets":["i am good"]},
]
print(list(filter(lambda a:a['tweets'],users)))
print(list(filter(lambda a:not a['tweets'],users)))
print(list(map(lambda x:x.get("username"),filter(lambda a:not a['tweets'],users))))

























# student_dict={
#     'name':'python',
#     'roll_no':456,
#     'CGPA':68,
#     'subject':['telugu','english','maths'],
#     'native_place':'india'
# }
# print(student_dict["name"])
# print(student_dict["subject"])
# print(student_dict["subject"][2])
# print(student_dict.get('company'))
#
# # How to add new keys in a dictionry
#
# student_dict["company"]=["google"]
# print(student_dict)
#
# # How to update keys in a dictionary
#
# student_dict["company"]=["google","micro"]
# print(student_dict)
# student_dict["company"].append("hpe")
# print(student_dict)
#
#
# keys=['name','job','salary']
# values=['srija','dev',5000]
# d=zip(keys,values)
# print(dict(d))
#
#
# keys=['a','b','c']
# default_value=None
# d=dict.fromkeys(keys,default_value)
# print(d)

# person={}
# person["first_name"]='srija',
# person["last_name"]='pilla',
# person["age"]=26,
# person["children"]=['jiyansh','dundi','montu'],
# person["pets"]={'dog':'Tommy'}
# print(person)
# print(person["age"])
# print(person["children"])
# person.clear()
# print(person)
# print(person.keys())
# print(list(person.keys()))
# print(person.values())
# print(person.items())
#

x, y = 5, 5
if x>y:
    print("x is greater than y")
else:
    print("x is less than y")


x,y,z = 0,4,2
if x>y:
    print("x is greater than y")
if x>z:
    print("x is greater than y")


d={'a':10,'b':20,'c':30,'b':450}
print(d)
foo={42:'aaa',3.14:'pi',True:'ccc','name':'madhu'}
print(foo)









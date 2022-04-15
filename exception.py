# try:
#     name="venkat"
#     print(name[10])
# except:
#     print("you're trying invalid index")
#     print(name[3])

# try:
#     f=open('hello_madhu.txt')
#     print(f)
# except:
#     print("file you're looking is not present,hence creating the file")
#     with open('hello_madhu.txt','w')as ip:
#         pass


# name="srija"
# try:
#     name[10]
# except:
#     print("hello")


# name="madhu"
# try:
#     name[10]
# except IndexError:
#     print("you're trying to access max index")
# except exception:
#     print("hello")

# name="venkat"
# try:
#     n
# except EnvironmentError:
#     print("from environment error")
# except Exception as v:
#     print("hello \n{}".format(v))
#

class underage(Exception):
    pass
def verify_age(age):
    if int(age)<18:
        raise underage
    else:
        print("you're is{}".format(age))

verify_age(30)
verify_age(50)








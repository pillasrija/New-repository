# class student:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last=last_name
#     def print_name(self):
#         return self.first_name+" "+self.last
# mahi=student(first_name="mahendra",last_name="perugu")
# print(mahi.first_name)
# print(mahi.print_name())
#
#
# class data:
#     pass
# d=data()
# print(type(d))
#
#
# class data:
#     def __init__(self,data1):
#         pass
# d=data(data1="asa")
# print(type(d))
#
#
# class father:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def print_name(self):
#         print(self.first_name+" "+last_name)

# simple inheritance
class A:
    x=10
    def show (self):
        print("from class A")

class B(A):
    def display(self):
        print("from child class B")


b=B()
print(b.x)
b.show()
b.display()


# multilevel inheritance
# class A:
#     def method_a(self):
#         print("from class A")
#
# class B(A):
#     def method_b(self):
#         print("from father class B")
#
# class C(B):
#     def method_c(self):
#         print("from grandson class C")

#
# c=C()
# c.method_a()
# c.method_b()
# c.method_c()
#
#
#
#
# # multiple inheritance
# class A:
#     def method_a(self):
#         print("from father class A")
#
# class B:
#     def method_b(self):
#         print("from father class B")
#
# class C(A,B):
#     def method_c(self):
#         print("from grandson class C")
#
#
# c=C()
# c.method_a()
# c.method_b()
# c.method_c()
#


# hierarchical inheritance
# class A:
#     def method_a(self):
#         print("from father class A")
#
# class B(A):
#     def method_b(self):
#         print("from father class B")
#
# class C(A):
#     def method_c(self):
#         print("from grandson class C")
#
#
# c=C()
# c.method_a()
# c.method_c()
#
# b=B()
# b.method_a()
# b.method_b()
#
#

# # hybrid inheritance
# class A:
#     def method_a(self):
#         print("from class A")
#
# class B(A):
#     def method_b(self):
#         print("from class C")
#
# class C(A):
#     def method_c(self):
#         print("from class C")
#
# class D(B,C):
#     def method_d(self):
#         print("from class D")
#
#
# d=D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()
# print(D.mro())

# abstraction
# class shape:
#     def area(self):
#         pass
#     def perimeter(self):
#         pass
# class square(shape):
#     def __init__(self,side):
#         self.side=side



# class without constructor
# class Data:
#     pass
# d=Data()
# print(type(d))


# class Data:
#     def --init--(self,data):
#     pass
# d=Data(data1="asa")
# print(type(d))

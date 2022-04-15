# t=('foo','bar','baz','qux','quux','corge')
# print(t)
# t=(1,2,3,)
# print(type(t))
# T=(1,'abc',True,1.234)
# print(T)

# t=('foo','bar','baz','qux','quux','corge',[1,2,3,4])
# t[-1][0] = "srija"
# print(t)
# print(t[0])
# print(t[-1])
# print(t[1:4])
# print(t[::-1])
# T=()
# print(type(T))


# t=('foo','bar','baz','qux')
# s1,s2,s3,s4=t
# print(s1,s4)
# s1,*s2,s4=t
# print(s1,s4)

#
# a=10
# b=20
# a,b=b,a
# print(a,b)
#
# email_address="pillasrija@gmail.com"
# print(email_address.split("@"))
# username,domain_name=email_address.split("@")
# print(username)
# print(domain_name)


# s={}
# print(type(s))

#
# s=set()
# print(type(s))
# s={'red','blue','green','red'}
# print(s)
#
#
# s='quux'
# print(set(s))
#
#
# s={0,'abc','1.23','5+6j','1',False}
# print(s)
# s.add('yellow')
# print(s)
# s.update(['purple','red'])
# print(s)
#
#
# s={'red','yellow','blue'}
# # s.remove('blue')
# # s.discard('yellow')
# print(s)
# x=s.pop()
# print(s)
# print(x)
#

x1={'foo','bar','baz'}
x2={'baz','qux','quux'}
print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))


x1={'foo','bar','baz'}
x2={'ree','qux','quux'}
print(x1.isdisjoint(x2))

x1={'foo','bar','baz'}
x2={'baz','qux','quux'}
superset={'foo','bar','baz','qux','quux'}
print(x1.issubset(superset))
print(x1>x2)
print(x1<x2)
print(x1==x2)




# a = ['foo','bar','baz','qux']
# b = ['baz','qux','bar','foo']
# print(id(a),id(b))
# print(a is b)
# print([1,2,3,4]==[1,2,3,4])

# a = ['foo','bar','qux','quux','corge']
# print(a[4],a[-2])
# print(a[1],a[-5])
# print(a[0])

# a = ['foo','bar','baz','qux','quux','corge']
# print(a[2:5])
# print(a[1:4])
# print(a[:4])
# print(a[:4] + a[4:])
# print(a[::])
# print(a[2:len(a)])
# print(a[2:6])


# l = ['a','b','c','d','e','f','g','h','i']
# print(l[2:7:3])
# print(l[::2])
# print(l[0:6:2])
# print(l[::-1])
# print(l[::-2])
# print(l[4:4])
# print(l[6:0:-2])
# print(l[0:6:2])
# print(l[2::2])

# a = ['foo','bar','baz','qux','quux','corge']
# a[0]='srija'
# print(a)
# print('bar' in a)

# x = ['a',['bb',['ccc','ddd'],'ee','ff'],'g',['hh','ii'],'j']
# print(x[1][0])
# print(x[1][1][0])
# print(x[3][0])
# print(x[-1])
# print('ddd' in x[1][1])qwq12

# a = ['foo','bar','baz','qux','quxx','corge']
# print(a)
# del a[3]
# print(a)
# # del a[1:5]
# # print(a)
# a +=['madhu','python']
# print(a)
# l = ['srija']
# print(l*3)
# print(l*-3)
# a = ['foo','bar','baz','qux','quxx','corge']
# print(a)
# # a.append("python")
# # print(a)
# # a.append(['python','hello'])
# # print(a)
# a.extend(["python",3.9])
# print(a)


# a = ['foo','bar','baz','qux','quxx','corge']
# print(a)
# a.insert(3,"python")
# print(a)
# a.remove('baz')
# print(a)
# a.pop(2)
# print(a)
# x = a.pop(2)
# print(a)
# print(x)
# a.clear()
# print(a)
# print(a.count('baz'))


#
# a,b,c,d,e,f,g = students
# print(f)
# print(d)
# # *stud3==srija,vinay,dinu,dundi,montu
# stud1,*stud2,stud3 = students
# print(stud3)
# print(stud2)


# students = ['divya','srija','vinay','dinu','dundi','montu','dumbu']
# print(students)
# students.sort()
# print(students)


l = ['a','b','c','d','e','f','g','h','i']
print(l[2:7])
print(l[-7:-2])
print(l[2:4])
print(l[2:7:2])
print(l[:3])
print(l[-3:])
print(l[::-1])
print(l[1:5])
l[1:5]=[1,2,3,4,]
print(l)
l[0]='srija'
print(l)
l1=[1,2,3,4]
l.append(l1)
print(l)
l[len(l):] = [1,2,3,4]
print(l)























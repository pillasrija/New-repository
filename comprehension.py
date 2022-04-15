# list1=[-2,-1,0,1,2,3]
# list2=[4,5,6,7,8]
# print([x*y for x in list1 for y in list2])
# print([x*y for x in list1 for y in list2 if x>0 if y%2==0])


# presidents_usa=["george washinton","jhon adams","thomas jefferson","james madison"]
# presidents_splitted=[name.split(" ")for name in presidents_usa]
# print(presidents_splitted)
# print([split_name[1] + " " + split_name[0]for split_name in presidents_splitted])


# # convert height from cms to feet using list comprehension:1cm=0.0328 feet
# height_in_cms=[('tom',183),('daisy',171),('mary',179),('michaet',190)]
# print([height for height in height_in_cms])
# print([height[0] for height in height_in_cms])
# print([height[1]*0.0328 for height in height_in_cms])
# print([round(height[1]*0.0328)for height in height_in_cms])

# new_dictionary={key:value for (key,value) in iterable}
# d={}
# for i in range(0,10):
#     d[i]=i**2
#     print(d)

d = {'a':1,'b':2,'c':3,'d':4}
for key, value in d.items():
     if value>3:
        print(key,value)

# 1-50,num%4,num**2
print({num:num**2 for num in range(1,50)if num%4==0})

# # {'hello':3,'hi':1}
# my_list=['hello','hi','hello','today','mrg','again','hello']
# print({k:my_list.count(k)for k in my_list})

d={0:'a',1:'b',2:'c',3:'d',4:'e'}
selected_keys=[0,2,4]
print({k:d[k] for k in selected_keys})

d={'delhi':121,'mumbai':221,'newyork':302,'london':250}
selected_keys=['delhi','mumbai']
print({i:d[i]for i in selected_keys})

roll_number=[123,345,554,323]
names=['alex','bob','can','don']
print(dict(zip(roll_number,names)))











































































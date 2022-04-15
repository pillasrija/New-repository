# contacts=[
#     ('john','john.deer@gmail.com'),
#     ('alex','alex.barner@yahoo.com'),
#     ('brad','brad.cooper@hotmail.com'),
#     ('cindy','cindy.barner@hotmail.com'),
#     ('matt','matt.damon@gmail.com'),
#     ('george','george.cloony@yahoo.com'),
#     ('mec','mc.barner@hotmail.com')
#  ]
# # print([name for name,email in contacts if'barner' in email])
#
# names=[]
# for name,email in contacts:
#     if "barner"in email:
#         names.append(name)
# print(names)


# trans=[(1237, 87522),
#        (1234, 1000),
#        (1236, 6754),
#        (1234, 2000),
#        (1236, 1700),
#        (1234, 400),
#        (1234, 600),
#        (1236, 788),
#        (1234, 500),
#        (1237, 126653)
#        ]
# deposits={}
# for customer_id,amount in trans:
#     if not customer_id in deposits:
#         deposits[customer_id]=[amount]
#     else:
#         deposits[customer_id].append(amount)
# print(deposits)
# print({transaction_id:sum(amount)for transaction_id,amount in deposits.items()})
# print(max(deposits.items(),key=lambda x:len(x[1])))
# print(min(deposits.items(),key=lambda x:len(x[1])))

# prepare contact list for given cdr
# cdr=[
#     ('9816724398','9810485623'),
#     ('98378217965','9895170862'),
#     ('9816724398','9858932761'),
#     ('98378217965','9816724398'),
#     ('9858932761','9810485623'),
#     ('9858932761','9895170862')
# ]
# mobile_history={}
# for mobile_number,dialled in cdr:
#     if mobile_number not in mobile_history:
#         mobile_history[mobile_number]=[dialled]
#     else:
#         mobile_history[mobile_number].append(dialled)
# print(mobile_history)


new_word=[]
for character in s:
     if character not in string.punctuations:





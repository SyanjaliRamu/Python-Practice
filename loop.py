# # for, while, nested loop
# # data = ["ram",'sita',"gita", "Hari","Binita"]
# # for user in data:
# #     if user=="gita":
# #         print(user)
# data = [
#     ['Ram', 'Sita', 'Hari', 'Gobind'],
#     ['Laxmi', 'Sophia', 'Kabita', 'Kalpana'],
#     ['Gopal', 'Gaundel', 'Mdan', 'Nahir', ]
# ]
# for users in data:
#     for user in users:
#         print(users)
# # for x in range(5, 10):
# #     print(x)
# # x = 1
# # while x < 10:
# #     print(x)
# #     x += 1
# num = int(input("ENter number" ""))
# x = 1
# print(x)
#
# # printdata[0])
# # printdata[1])
# # printdata[2])
# # printdata[3])
# # printdata[4])
# # for abc in data
# # for user in data:
# #     # print(user)
# #     print(user, end=',')
# data=["ram',"sita",'Gita','Hari']
#       for name in data:
#           print(name)

num = int(input("enter any number:"))
total_even = 0
total_odd = 0
x = 1
while x <= num:
    if x % 2 == 0:
        total_even += x
    else:
        total_odd += x
    x += 1
    total_even
    print(f"total even number: {total_even}")
    print(f"total even number: {total_odd}")

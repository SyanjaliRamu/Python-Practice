# define functions
#
# def message():
#     print("Hello Python")
#
# message()
# def add(x,y):
#     print(x+y)
# a= int(input("Enter First number: "))
# b= int(input("Enter Second number: "))
# add(a, b)
# def pr(data):
#     print(data)
# pr("Hello !!")
# pr(1+21)

# def introduction(name, age=''):
#     print(name)
#     print(age)

#
# introduction("Sita")
# def students(s1,s2,s3,s4,s5):
#     print(s1)
#     print(s2)
#     print(s3)
#     print(s4)
#     print(s5)
# students('ram', 'sita' ,'hari','gita' ,'gyanu')
#
# def students(*names, **data):
#     print(names)
#     print(data)
# students('ram', 'sita' ,'hari','gita' ,22,'gyanu')
# fucntion return value
# def add(x,y)
#     return x + y
#
# result =add(2,4)
# print (add(2,4))
# def add_sub(x, y):
#     tot = x + y
#     sub = x - y
#     return [tot, sub]
#
#
# result = add_sub(20, 10)
# print(result[0])
# print(result[1])

# Global Scope
# x=10
#
# def test():
#     global x
#     x = x + 20
#     print(x)


# def data(**values):
#     for key, val in values. items():
#         print(key)
#         print(val)
#
# data(name= 'ram' , age=20)

# def my_fun():
#     def test(name=None):
#         return f"My name is {name}"
#     return test
#
# print(my_fun()())

# Anonymous fucntion: lamdba
# add = lambda x, y: x+ y
# print(add(10,20))

# Recursioncls
# functions.py
import calculator
from calculator import *
# print(calculator.add(10,20))
print("Total")
print(add(10,20))
print("Total")
print(mul(3,5))


# import sys
# print(dir(sys))
import datetime
print (dir(datetime))


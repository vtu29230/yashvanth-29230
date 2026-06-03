"""a=5
b=10.5
name="Yash"
status=True
print(type(a))
print(type(b))
print(type(name))
print(type(status))
#data types in python"""
# variables in python
"""
a=5
name = "yash"
"""
#add two numbers in python
"""a = 5
b = 10
sum = a+b
print("sum =",sum)
"""
#swap two number in python
"""a=5
b=10
print("before swapping")
print("a =",a)
print("b =",b)
a ,b = b ,a
print("after swapping")
print("a =",a)
print("b =",b) 
"""
# data types in python
"""
a=5
b=10.5
c="yash"
print(type(a))
print(type(b))
print(type(c))
"""
#input and output in python
"""
name = input("enter your namme: ")
age = input("enter your age:")
print("your name is",name)
print("your age is",age)
"""
#input and out put number in python
"""
a = int(input("enter the fisrt number:"))
b = int(input("enter the second number:"))
sum = a+b
print("sum =", sum)
"""
#even or odd number in python
"""
num = int(input("enter a numbber:"))
if num %2 == 0:
    print("even number")
else:
    print("odd number")
"""
#largest of threee numbers iin python
"""
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a > b and a > c:
    print("largest number is A")
else:
    if b > a and b > c:
        print("largest number is B")
    else:
        print("largest number is C")
        """
# grade calculation program
"""
marks = int(input("enter your marks:"))
if marks >= 90:
    print("grade A")
elif marks >= 80:
    print("grade B")
else:
    print("grade C")
    """
#multiplication table
"""
num = int(input("enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    """
# factorial program
"""num = int(input("enter a number:"))
fact = 1
for i in range(1, num+1):
    fact = fact * i
    print("factorial of = ", fact)
    """
# fibonacci series program
"""n = int(input("enter the number of terms:"))
a = 0
b = 1
print("fibonacci series:")
for i in range(n):
    print(a, end="")
    c = a + b
    a = b
    b = c
    """
# function foere additon
"""def add(a ,b):
    return a + b
print(add(5,10))
"""
# prime number checking program
"""def  prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "it is not prime")
                break
            else:
                print(n, "it is prime")
        else:
           print(n, "it is not prime")
prime(9)
"""
# list in python
"""
list = [1,2,3,4,5]
"""
# find the largest number in a list
"""list = [2,23,45,46,67,78,89]
largest  = max(list)
print("Largest element =", largest)
"""
# sort list
"""
list = [70, 29, 45, 21, 56]
list.sort()
print("sorted list =", list)
"""
# descending order
"""
list = [70, 29, 45, 21, 56]
list.sort(reverse = True)
print(list)
"""
# rmove duplicate from list
"""
num = [10, 20, 30, 40, 40, 50]
unique = list(set(num))
print("num after removing duplicate =", unique)
"""

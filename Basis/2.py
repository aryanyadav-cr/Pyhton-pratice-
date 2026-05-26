#chapetr 2

#String 
'''
str = 'delhi'
print(str)
'''
#sum of 2 string
'''
str1 = "Hello"
str2 = "World"
sum = str1 + str2
print(sum)
'''
#indexing
'''
str1 = "Hello this is new test"
print(str1[6]) 
print(str1[-2])
'''
#Slicing

# str = "Aryan Yadav"
# print(str[1:8])
# print(len(str))
# print(str[-8:-1])

#String function
'''
str = "my name is aryan yadav"
print(str.endswith("v"))
print(str.capitalize())
print(str.replace("my","the"))
print(str.find("is"))
print(str.count("i"))'''

#WAP to input there name and print it's length
"""
str = input("enter you first name:")
print("the length of name :",len(str))
"""
#WAP to find the occurence of a "$" in  a string
'''
str = "Aryan %$ dhjvdljd "
print(str.find("%"))
'''

#Conditional statement
'''
marks = float(input("Enter your marks : "))
if(marks>90):
   print("grade=A")
elif (90>marks>=80):
   print("grade=B")
elif (80>marks>70):
   print("grade=C")
elif (70>marks):
   print("grade=D")
else:
   print("N")
'''

#Pratice question
# 1 WAP to check number is odd or even also user input
'''
Num = int(input("Enter a number to check no is odd or even: "))
if(Num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")
'''
# 2 WAP to find the greatest of 3 number entered by the user 
'''
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))

if n1>n2 and n1>n3:
    print("the greater number is ", n1)
elif n2>n1 and n2>n3:
    print("the greater number is ", n2)
else:
    print("the greater number is ", n3)
'''

# 3 WAP to check if a number is a multple of 7 or not
num = int(input("enter your number:"))
if num%7==0:
    print(num,"is multiple of 7")
else:
    print(num,"is not  multiple of 7")
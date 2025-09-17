#if-elif-else condition practies 

a , b = 5 , 4 #1 ques
if(a>=b):
    print("a is maximum")
else:
    print("b is maximum")
'''
'''
a,b,c = 10,30,40 # 2 quesion 
if(a>b):
    print("a is max")
elif(b>c):
    print("b is max" )
#elif(c>a):
else:
    print("c is max")
    

n = int(input()) # 3 ques
if(0 < n):
    print("The num is positive")
elif(0 > n):
    print("The num is negative")
else:
    print("The num is zero")


num = int(input()) #ques4
if(num % 5 == 0):
    print("The num is divisible 5")
elif(num % 11 == 0):
    print("The num is divisible 11")
else:
    print("The num is not")


num = int(input()) # 5 ques
if(num % 2 == 0):
    print("This num is even")
else:
    print("This num is odd")
    

year = int(input()) # 6 ques
if(year % 4 == 0):
    print("This is leap year")
else:
    print("Thie is not leap year")


ch = (input()) # 7 ques
if('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
    print("this is alphabet")
else:
    print("this is not alphabet")


#-----List comprehension--------#

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
    
print("--------------")
n = int(input()) # 3 ques
if(0 < n):
    print("The num is positive")
elif(0 > n):
    print("The num is negative")
else:
    print("The num is zero")

print("-----------------")
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


ch = input("Enter any character: ")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'): # this is a to z this condition and input will be "a to z" print alphabet.
    print("Alphabet")
elif '0' <= ch <= '9':
    print("Digit")      # this condition print digit given input "0 to 9".
else:
    print("Special Character")   # this is input special character print.

print("-------------")
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase Alphabet")
elif 'a' <= ch <= 'z':
    print("Lowercase Alphabet")
else:
    print("Not an alphabet")


print("--------------")
week = int(input("Enter week number (1-7): "))

if week == 1:            # User given input "1 to 7 week" this condition are cheak 1 == 1 and print 'monday.
    print("Sunday")
elif week == 2:
    print("Monday")
elif week == 3:
    print("Tuesday")
elif week == 4:
    print("Wednesday")
elif week == 5:
    print("Thursday")
elif week == 6:
    print("Friday")
elif week == 7:
    print("Saturday")
else:
    print("Invalid week number")

print("--------------")
month = int(input("Enter month number (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]: # this condition are follow months and print the month day.
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month number")

print("----------------")
amount = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(note, "=", count)

print("---------------")
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:  # triangle ki tino anglr same hote he 60+60+60.
    print("Valid Triangle")
else:
    print("Invalid Triangle")

print("-----------------")
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

print("----------------")
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):  # this condition all true than print valid.
    print("Valid Triangle")
else:
    print("Invalid Triangle")

print("----------")
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:      # Is condition me sare angle same hone chahiye.
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle") # is me do angle same hote he  .
else:
    print("Scalene Triangle")

print("--------------")
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")
    
# 19. Program to calculate percentage and grade
print("----- Grade Calculator -----")
phy = int(input("Enter Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
bio = int(input("Enter Biology marks: "))
maths = int(input("Enter Mathematics marks: "))
comp = int(input("Enter Computer marks: "))

total = phy + chem + bio + maths + comp
percentage = total / 5

print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)









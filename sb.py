# print("Hello world")
# print(17*13)
# print("I am best inthe world \nand always happy me")
# print("Hey",6 ,5, sep="~" , end="009\n")
# print("Shweta")
# a = "Shweta"
# b ="Mandloi"
# print(a )
# print(a+b)
# print("The type of a is ", type(a))

# list = [1,2,3 ,["apple","banana"]]
# print(list)
# tuple = (12,13,123, ("lion"),("tiger"))
# print(tuple)

# dict = {'name':"Shweta", 'age': 20 }
# print(dict)

'''
# CALCULATOR:-----
n = 10
m = 3
ans1 = n+m
print("Addition of",n,"and", m,"is =",ans1)
ans2 = n-m
print("Subtractor of",n,"and", m,"is =",ans2)
ans3 = n*m
print("Multiply of",n,"and", m,"is =",ans3)
ans4 = n/m
print("Dvision of",n,"and", m,"is =",ans4)
ans5 = n%m
print("Modules of",n,"and", m,"is =",ans5)
ans6 = n//m
print("Floor Division of",n,"and", m,"is =",ans6)
ans7 = n**m
print("Exponent of",n,"and", m,"is =",ans7)
'''
'''
a ="34"
b = "24"
print(a+b) # both value is string form the o/p like 3424
print(int(a) + int(b)) #String data type a and b convert 'int' form this method using is cld typecasting.

x = 5
y = 2.5
print(type(x), "and ", type(y))
print(x+y)
'''

'''
 #string 
name = "Shweta"
name2 = "Mandloi"
print(name)
apple = """Hello i am shweta.  
i belong to shajapur
i am best """   # """s--sss """ this cot using in multiple string 
print(apple)
print(name[0]) # one charector array form is print 

print("lets use a for loop\n")
for character in apple:
    print(character)
'''
'''
fruit ="Mango"
len1 = len(fruit)
print("The mango len is" ,len1)
print(fruit[0:5])
print(fruit[0:-3])
print(fruit[-3:-1])
print(fruit[-1:len(fruit) - 3])
'''
'''
nm = "Shubham"
print(nm[-4:-2])
print()
# String are immutable
a = "Shweta!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Shweta","Vartika"))
'''

'''
# Excise --2
import time
# Get current hour, minute, and second
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

# Print each timestamp
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")

# Greeting logic based on hour
if 5 <= hour < 12:
    greeting = "Good morning sir!"
elif 12 <= hour < 18:
    greeting = "Good afternoon sir!"
elif 18 <= hour < 22:
    greeting = "Good evening sir!"
else:
    greeting = "Good night sir!"

print(greeting)
'''
'''
#for loop --->
name = "Shweta Mandloi"
print(name)
for i in name:
    print(i, end=", ")

for i in range(5):# loop for in range like this program 
    print(i)
    

for i in range(3):
    if i == 2:
        break
    print(i)
'''
'''
# While loop --> condition if true run the program end false
i = int(input("Enter the num:"))
while(i<=20):
    i = int(input("Enter the num:"))
    print(i)
    print("Done with the program")

# while loop with else
count = 5
while(count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")
'''
'''
#Break and continoue 
for i in range(1,12):
    if(i == 10):
        break
    print("5 X",i+1 , "=", 5*(i+1))
'''
'''
for i in range(12):
    if(i == 10):
        print("THe skip the value ")
        continue
    print("5 X",i, "=", 5*(i))
    '''

'''
#Function 
def average(a=9, b=1):
    print("The average is ", (a+b)/2)

average(5,6)
average(2,2)

def name(fname, mname = "Shweta" ,lname = "Mandloi"):
    print("Hello,",fname, mname, lname)

name("Hi" ,"Arpit" , "Mandloi")
'''

# Bitwise Opreators 
print(100 + +4 + -5)
a = 10
print(a << 4) #Left side 
print(a >> 3) #Right side
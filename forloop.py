# -------- For loop ---------------
for i in range(1 , 10): # print natural num 1 to n.
    print(i)

for i in range(10, 0 , -1): # print the reverse natural num in the for loop.
    print(i)

for i in range(97 , 123):
    print(chr(i) ,end=" ")

print("-----------------")
for i in range(1, 101):
    if i % 2 == 0:       # agar number 2 se divide ho jaye (even)
        print(i, end=" ")

print("---------------")
for i in range(1,101): # num 2 se divide nhi hota he (odd)
   if i % 2 == 1:
       print(i, end=" ")

print("---------------")
n = 10  # yaha tum number change kar sakte ho
total = 0

for i in range(1, n+1):
    total += i  # total = total + i

print("Sum of natural numbers:", total)

print("----------------")
num = 5  # jis number ka table chahiye hamko 
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

print("--------------")
n = 10
odd_sum = 0

for i in range(1, n+1, 2):  # 1 se start karna hai, step = 2
    odd_sum += i

print("Sum of odd numbers:", odd_sum)

print("-----------------")
num = 12345
count = 0
temp = num

while temp > 0:
    temp //= 10   # last digit remove karna
    count += 1

print("Number of digits:", count)

print("------------")
num = int(input("Enter a number: "))
last = num % 10
first = int(str(num)[0])
print("First digit:", first)
print("Last digit:", last)

print("---------------")
num = int(input("Enter a number: "))
last = num % 10
first = int(str(num)[0])
print("Sum =", first + last)

print("------------")
num = input("Enter a number: ")

for d in range(10):  # digits 0–9
    count = 0
    for ch in num:
        if int(ch) == d:
            count += 1
    if count > 0:
        print(f"{d} occurs {count} times")

print("---------------")
num = int(input("Enter a number: "))
product = 1

for digit in str(num):
    product *= int(digit)

print("Product of digits:", product)

print("--------------")
num = int(input("Enter number: "))
num_str = str(num)
swapped = num_str[-1] + num_str[1:-1] + num_str[0]
print("Swapped number:", swapped)

# 14. Sum of digits
num = int(input("Enter number: "))
s = 0
for d in str(num):
    s += int(d)
print("Sum of digits:", s)

# 15. Product of digits
num = int(input("Enter number: "))
p = 1
for d in str(num):
    p *= int(d)
print("Product of digits:", p)

# 16. Reverse a number
num = int(input("Enter number: "))
rev = ""
for d in str(num):
    rev = d + rev
print("Reverse:", rev)

# 17. Palindrome check
num = input("Enter number: ")
rev = ""
for d in num:
    rev = d + rev
print("Palindrome:", num == rev)

# 18. Frequency of digits
num = input("Enter number: ")
for i in range(10):
    count = 0
    for d in num:
        if int(d) == i:
            count += 1
    if count > 0:
        print(i, "->", count)

# 19. Number in words
words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
num = input("Enter number: ")
for d in num:
    print(words[int(d)], end=" ")

# 20. ASCII characters
for i in range(128):
    print(i, "->", chr(i))

# 21. Power using for loop
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for i in range(exp):
    result *= base
print("Power:", result)

# 22. Factors of a number
num = int(input("Enter number: "))
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")

# 23. Factorial of a number
num = int(input("Enter number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)

# 24. HCF (GCD)
a, b = map(int, input("Enter two numbers: ").split())
hcf = 1
for i in range(1, min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf = i
print("HCF:", hcf)

# 25. LCM
a, b = map(int, input("Enter two numbers: ").split())
max_val = max(a,b)
lcm = max_val
for i in range(max_val, a*b+1):
    if i%a==0 and i%b==0:
        lcm = i
        break
print("LCM:", lcm)

# 26. Prime check
num = int(input("Enter number: "))
prime = True
for i in range(2,num):
    if num%i==0:
        prime = False
        break
print("Prime:", prime)

# 27. All primes between 1 to n
n = int(input("Enter limit: "))
for num in range(2,n+1):
    prime = True
    for i in range(2,num):
        if num%i==0:
            prime = False
            break
    if prime:
        print(num,end=" ")

# 28. Sum of primes between 1 to n
n = int(input("Enter limit: "))
sum_primes = 0
for num in range(2,n+1):
    prime = True
    for i in range(2,num):
        if num%i==0:
            prime = False
            break
    if prime:
        sum_primes += num
print("Sum of primes:", sum_primes)

# 29. Prime factors
num = int(input("Enter number: "))
for i in range(2,num+1):
    if num%i==0:
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i,end=" ")

# 30. Armstrong number check
num = int(input("Enter number: "))
power = len(str(num))
s = 0
for d in str(num):
    s += int(d)**power
print("Armstrong:", s==num)

# 31. All Armstrong numbers between 1 to n
n = int(input("Enter limit: "))
for num in range(1,n+1):
    power = len(str(num))
    s = 0
    for d in str(num):
        s += int(d)**power
    if s==num:
        print(num,end=" ")

# 32. Perfect number check
num = int(input("Enter number: "))
s = 0
for i in range(1,num):
    if num%i==0:
        s+=i
print("Perfect:", s==num)

# 33. All perfect numbers between 1 to n
n = int(input("Enter limit: "))
for num in range(1,n+1):
    s=0
    for i in range(1,num):
        if num%i==0:
            s+=i
    if s==num:
        print(num,end=" ")

# 34. Strong number check
num = int(input("Enter number: "))
s=0
for d in str(num):
    fact=1
    for i in range(1,int(d)+1):
        fact*=i
    s+=fact
print("Strong:", s==num)

# 35. All strong numbers between 1 to n
n = int(input("Enter limit: "))
for num in range(1,n+1):
    s=0
    for d in str(num):
        fact=1
        for i in range(1,int(d)+1):
            fact*=i
        s+=fact
    if s==num:
        print(num,end=" ")

# 36. Fibonacci series
n = int(input("Enter terms: "))
a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b




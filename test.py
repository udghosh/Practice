"""
print("Hello python Programming")
print("First T&T Lab Code")

b=[1,2,4,5,7,8,9]

print(b[1:8])
print(b[:4])
"""
"""
#km to metre
kilometers = float(input("Enter value in kilometers: "))

print('%0.2f kilometers is equal to %0.2f metre' %(kilometers,kilometers*100))
"""

"""
#farenheit to celcius
Fahrenheit= float(input("Enter value in Farenheit: "))  
Celsius = ((Fahrenheit-32)*5)/9  
print("Temperature in Celsius is: ");  
print(Celsius); 
"""
"""
a = float(input("Enter first number: "))
b = float(input("Enter Second number: "))
a = a+b;
b = a-b;
a = a-b;
print('Value of first number %0.2f and second number %0.2f ' %(a,b))
"""
"""
a = float(input("Enter first number: "))
b = float(input("Enter Second number: "))
print(" ")
if a>b:
    print(" A is greater than B")
else :
    print(" B is Greater than A")
"""
"""
a = float(input("Enter first number: "))

print("")
if a>0 :
    print("A is Positive")
else :
    print("A is Negative")
"""
"""
a = float(input("Enter first number: "))
b = float(input("Enter Second number: "))
choice = int(input("Enter 1 for add, 2 for sub, 3 for mult, 4 for div : "))

if choice==1 :
    print("result is :",(a+b))
elif choice==2 :
    print("result is :",(a-b))
elif choice==3 :
    print("result is :",(a*b))
elif choice==4 :
    print("result is :",(a/b))
else :
    print("Invalid choice!!!!")
 """

"""
lower = int(input("Enter lower number:"))
upper = int(input("Enter upper number:"))
for i in range(lower, upper+1):
   if(i%3==0):
      print(i)
 num = 407
"""

"""
num = int(input("Enter a number: "))
if num > 1:

   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")     

"""

"""
n = int(input("Enter a number: "))
sum = 0
for digit in str(n):   
    sum += int(digit)        
print("The sum of digits is",sum)
 """


"""
num = input("Enter a number ") 

if num == num[::-1]: 
    print("Yes its a palindrome") 
else: 
    print("No, its not a palindrome") 
"""
'''
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
   '''
   
dict = {'name': 'Uday', 'Roll': 1805174, 'Batch' : 'CSE-3','Yop': 2022}

for values in dict.values() :
    print(values)
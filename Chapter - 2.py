#Data Types and Operators in python
# food = "samosa"
# age = 25
# area = 670.98
# name = "khushi"

# print(type(food))
# print(type(age))
# print(type(area))
# print(type(name))


# WAP to take age as input and print age and data type also
# age = int(input("Enter Your Age: \n"))
# print("Your age is:", age)
# print("Data Type of age is:", type(age)) 

#WAP to input two numbers and print their sum
# input1 = int(input("Enter 1st Number: \n"))
# input2 = int(input("Enter 2nd Number: \n"))
# sum = input1+input2
# print("Sum is :", sum)

#WAP to print average of two numbers taken as input
# input1 = int(input("Enter 1st Number : \n"))
# input2 = int(input("Enter 2nd Number: \n"))
# average = (input1+input2)/2
# print("Average of these two numbers is: ", average)

#Data Types Conversion

#Implicit Conversion (Jo Automatically hota hai python mein)
# x = 5 #int
# y = 2.5 #float
# z = x+y #iska answer aayega float kyunki python badi value leta hai aur flot badi value hai
# print("Answer is ", z)
# print("data Type of z is", type(z))

#WAP to take number as input, convert it into float and print both original and converted value with thier data type also

# num = input("Enter a number: \n")
# flo = float(num)

# print("Original Value:", num, "Converted Value", flo, "Data Type of original is:", type(num), "Data type of converted is:", type(flo))



#Operators in Python

#Arithmetic Operators
# x = 10
# y = 5
# print('sum',x+y) 
# print('difference',x-y)
# print('multiplication',x*y)
# print('division',x/y)
# print('modulo',x%y)
# print('floor division',x//y)



#Comparison Operators
# a = 10
# b= 5
# print(a==b)
# print(a>=b)
# print(a<=b)
# print(a>b)
# print(a<b)
# print(a!=b)



#Logical Operators
# a = 10
# b = 20
# print(a>b and a<b)

# print(b<a or a<b)
# print(not(a<b))



#Assignment operators
# a = 2
# b = 4

# a+=6
# print(a) #8

# b-=2
# print(b) #2

# a*=10
# print(a)  #80 (Kyunki upar hum a ko 8 bana chuke hai)

# b/=2
# print(b)  #1.0  (Kyunki upar hum b ko 2 bana chuke hai)




#WAP that takes two numbers and prints their sum, difference and product, and also check whether the first number is greater than the second or not??

# input1 = int(input("Enter 1st Number: \n"))
# input2 = int(input("Enter 2nd Number: \n"))

# print("sum", input1+input2)
# print("difference", input1-input2)
# print("product", input1*input2)

# print(input1>input2)


## Smart temperature converter (Degree celsius to fahrenheit and kelvin)
# formula : fahrenheit = (C * 9/5) + 32, kelvin = C + 273.15

# cel = int(input("Enter Temperature in degree celsius: \n"))
# fah = (cel * 9/5) + 32
# kel = cel + 273.15

# print("Temperature in fahrenheit: ", fah)  
# print("temperature in kelvin: ", kel)  




## Bill Split Calculator Program 
# total = float(input("Enter Total bill amount: \n"))
# friends = int(input("Enter Number of friends: \n"))

# Split = total/friends

# print("Each wil pay: ", Split)
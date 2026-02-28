#Python variables and fundamentals
name = " Prashant Yadav"
age1 = 25
age2 = 40
print("Actual Value: ",  age2)
favsubject = "Maths"
age2 = age1
print("Changed Value: ", age2)

#Taking input from user
print("Sample program to take input from user")
name = input("Enter your good name: ")
print("Your good name is:", name)

#Question - take diameter as input and calculate area of circle

dia = input("Enter diameter: \n")
dia1 = int(dia)  

rad = dia1/2
pi = 3.14
area = pi*(rad**2)
print("Area Of Cirlce is :", area)
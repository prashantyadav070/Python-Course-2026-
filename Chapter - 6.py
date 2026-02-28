## Loops in python 
## While loop and for loop

# print the name 100 times

num = 1
while num<=10:
    print("Prashant")
    num +=1

print("Now we are out of the loop")


#Q - WAP to print numbers from 1 to 10 using while loop

# i = 1
# while i<=10:
#     print(i)
#     i+=1

#Q - WAP to print numbers from 10 to 1 using while loop
# j = 10
# while j>=1:
#     print(j)
#     j-=1  



#Q - WAP to print all even numbers from 1 to 50 using a while loop

# i = 1
# while i<=50:
#     if(i%2==0):
#         print(i)

#     i+=1


#Q - WAP to print the sum of first n natural numbers

# n = int(input("Enter a number: \n"))

# i = 1 
# sum = 0
# while i<=n:
#     sum = sum + i
#     i+=1

# print(f"Sum of first {n} numbers is {sum}")


#Q - WAP to print this star pattern
# *
# **
# ***
# ****
# *****


# i = 1
# while i<=5:
#     print("*"*i)
#     i+=1


#Q - WAP to print your name with  a number in front of it

# i = 1
# while i<=5:
#     print(f"{i}. Prashant Yadav")
#     i+=1




#Q - WAP to print multiplication table of a number

# n = int(input("Enter a number: \n"))

# i = 1
# while i<=10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1




## For loop in python 

# food = ["cake", "mango", "pizza"]
# print(food[0])

# for item in food:
#     print(item)

# colleges = ("NIT delhi", "ABES", "BBAU", "IITD")

# for eachitem in colleges:
#     print(eachitem)            


# range in for loop

for item in range(1,8,1):
    print(item)  

for item in range(2,21,2):
    print(item)

#Q - WAP to print all even numbers between 1 and 20 using for loop and range

# for item in range(2,21,2):
#     print(item)

#Q - WAP 


## Break in python

# for num in range(1,10):
#     if num==5:
#         break
#     print(num)




# Continue in python 
# for num in range(1,10):
#     if num==6:
#         continue
#     print(num)


#Pass in python

for i in range(1,7):
    pass   #future code will go here

## Countdown timer project in python 
import time
count = int(input("Enter the Counter number: \n"))
print("Countdown Starts Now: \n")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)

print("Woohoo! Happy new year 2026!!")

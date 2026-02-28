#Conditional Statements
# marks = 95

# if(marks>=90):
#     print("Your grade is A")
# elif(marks>=80):
#     print("Your grade is B")

# age = 16

# if(age>=18):
#     print("you are eligible to vote")
# else:
#     print("You are not eligible to vote")

# print("My code ends here")

#Q - Take input and print positive if number is greater than 0, negative if less than 0

# num = int(input("enter a number: \n"))
# if(num>0):
#     print("positive")
# elif(num==0):
#     print("zero")
# else:
#     print("negative")





## Lists Basics:-

food = ["chhole bhature", "choco waffle", "gulab jamun", "apple", "mango",7]

print(len(food))  #size of the list

print('first value of the list:', food[0]) #list indexing

## List Method:-
#indexing
marks = [99, 100, 90, 95]
print(marks[1])
print(marks)

#Modifying elements of list

marks[1] = 98
print(marks)


## Slicing in list:-
marks = [99, 100, 90, 95]
print(marks[1:3])         



#Some methods in list:-
print(max(marks))
print(min(marks))

marks.append(92)
print(marks)

marks.sort()
print(marks)

marks.pop(1)
print(marks)

marks.remove(100)
print(marks)

marks.insert(1,100)
print(marks)




#Q - WAP that takes the name of three foods from the user and store in list, print list and its length

# food1 = input("Enter food 1: \n")
# food2 = input("Enter food 2: \n")
# food3 = input("Enter food 3: \n")


#1st method
# foodlist = [food1,food2,food3]
# print(foodlist)
# print("length of list: ", len(foodlist))


#2nd method
# foodlist = []
# foodlist.append(food1)
# foodlist.append(food2)
# foodlist.append(food3)
# print(foodlist)


## Tuples in python:-


mytuple = (78,90,75)
studenttuple = ("Khushi", "divya", "ishaan")

# studenttuple[1] = "aanchal" tuples are immutable/not changeable

print(studenttuple[2])


#empty tuples
emptytuple = ()
print(type(emptytuple))
print(type(studenttuple))


#single tuple
single = (1,)
print(type(single))

print(studenttuple.index("ishaan"))
print(studenttuple.count("ishaan"))
print(studenttuple.count("Khushi"))



#ask the user for their 3 favorite movies and store them in a list?

movie1 = input("Enter a movie: \n")
movie2 = input("Enter a movie: \n")
movie3 = input("Enter a movie: \n")

movielist = []

movielist.append(movie1)
movielist.append(movie2)
movielist.append(movie3)

print(movielist)


     


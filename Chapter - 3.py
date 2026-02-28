## Python Strings 
# str1 = 'hello' #single quoted string
# str2 = "mango"   #double quoted string
# str3 = '''Banana'''   # triple quoted string

# print(str1)
# print(str2)
# print(str3)

#String concatenation
# print(str1 + " " + str2 + " " + str3)

#Length of string
# print(len(str1))
# print(len(str2))
# print(len(str3))


#WAP to take user name as input and print first character, last character and total length of the name

# name = input("Enter Your Name: \n")
# length = len(name)
# print(length)
# print("First character: ", name[0])
# print("Last character: ", name[-1])

#Understanding Slicing Concept

# str = 'GulabJamun'
# firsthalf = str[0:5]
# secondhalf = str[5:10]
# print(firsthalf)
# print(secondhalf)

# newfirsthalf  = str[:5]
# newsecondhalf  = str[5:]
# print(newfirsthalf)
# print(newsecondhalf)



#WAP to take favorite food name as input and print middle 3 characters and last 2 characters

# food = input("Enter your favorite  food name: \n")
# middle = len(food)//2

# mid3 = food[middle-1:middle+2]
# last2 = food[-2:]
# print(mid3)
# print(last2)

#String Methods
str = "mcdonalds"


# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.replace("don","ron"))
# print((str.find("alds")))
# print(str.count("d"))

#Q - WAP that takes a sentence as input, converts it to lowercase, replace all spaces " " with underscores _ , prints the new string

# str = input("Enter a Sentence: \n")
# str = str.lower()
# str  = str.replace(" ", "_")
# print(str)

#Formatted strings (f-strings)

# age = 22
# name = "Prashant"

# print(f"My name is {name} and my age is {age}")


#Escape sequence
# print("Python Language") #Normal
# print("Python\nLanguage")  #Backslash n for new line
# print("Python\tLanguage")   #Tab space

#Q - Convert text based emotions (like happy, sad) into emojis

# str = input("Enter a sentence: \n")

# str = str.replace("Happy","😄")
# str = str.replace("happy","😄")
# str = str.replace("Sad","😔")
# str = str.replace("sad","😔")
# print(str)


# Extra functions

#String concatenation
# print("Hello" + " " + "World")
# a = "school"
# b = "holiday"
# print(a + " " + b)

#String Repitition 
# a = "Yum!!"
# print(a*6)


#Membership

# str = " There is no class today!"
# print("no" in str)
# print("wa" in "volkswagon")


#Len() Function

# str = "Disnepland"
# print(len(str))


#Q - WAP that takes a sentence and prints total characters, uppercase and lower case version

# str = input("Enter a sentence: \n")
# total = len(str)
# print("total characters = ", total)
# print(str.upper())
# print(str.lower())

#Q - WAP to take any word or sentence as a input and print its first character, last character, and total number of characters?

# str = input("Enter a word/sentence: \n")
# first = str[0]
# last = str[-1:]
# last2 = str[-1]
# total = len(str)
# print(first)
# print(last)
# print(last2)
# print(total)








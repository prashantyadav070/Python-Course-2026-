# Dictionary & Sets

student = {
    "name" : "prashant",
    "city" : "delhi",
    "age" : 22,
    "roll no" : 58,
    "name" : "rohit"
}

print(type(student))  
print(student["name"])  
print(student)    


#updating value
student["city"] = "hyderabad"
print(student)



#adding value
student["favsub"] = "maths"
print(student)



#removing items

student.pop("favsub")
print(student)

#return all keys
print(student.keys())

# return all values
print(student.values())


#returning key value pairs
print(student.items())


#returning value of a key
print(student.get("age"))


#updates/add dictionary with another dictionary (this will append a new dictionary in the end of original one)
# student.update({"phone":"xiaomi",
#                "type":"arm64",
#                 "ram": 8,
#                  "storage":128 })

# print(student)



#Nested dictionary

profile = {
    "name" : "saumya singh",
    "details" : {
        "followers": 1300,
        "verified" : True
    }
}



#Q - Create a dictionary named marks to store marks of 3 subjects, add the subjects one by one and print the final dictionary


marks = {}

marks["maths"] = 99
marks["chemistry"] = 99
marks["computer science"] = 91

print(marks)


## Sets in python

food = {"paneer", "chhole", "sandwhich", "paneer"}
print(type(food))
print(food)

#sets do not entertain duplicate values

#create empty set
empty = set()
print(type(empty))

#adding item in set
food.add("kunafa")
print(food)

#removing item from set
food.remove("chhole")
print(food)

#clearing whole set
# food.clear()
# print(food)

#removing a random element from set
# food.pop()
# print(food)

#union of set (combining two sets with all elements)
food1 = {"mango", "jalebi"}
food=food.union(food1)
print(food)

#intersection (only common element of both sets)
food2 = {"pav", "chhole","ice","mango"}
food3 = {"pav", "juice","apple"}
food3=food3.intersection(food2)
print(food3)


#Q - You are given a list of programming languages:
# ["python", "java", "c++","java", "c"]
#convert it into a set and print how many unique languages divya knows.


programme = ["python", "java", "c++", "python", "java", "c"]
print(type(programme))
#how to convert a list into a set
programset = set(programme)
print(type(programset))
print("divya knows these many languages: ", len(programset))



#Q - Create a dictionary storing meaning of 3 english words

english = {}

english["Happy"] = "joyful"
english["escape"] = "to run away"
english["frightened"] = "fearful"

print(english)



#Q - create a set of numbers and show union and intersection with another set

set1 = {1,2,4,5,10}
set2 = {4,6,7,10,11,12}

set1 = set1.union(set2)
print(set1)

set1 = set1.intersection(set2)
print(set1)


#Q - Try to add both integer 9 and float 9.0 to a set and observe what happens.

set3 = {9,9.0}
print(set3)

set4 = {"9", 9.0}
print(set4)
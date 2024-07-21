programming_dictionary = {
    "Bug" : "part of code that stops from successfull running of program",
    "function" : "The piece of code you can over and over again",
}

# Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# Addig new items to dictionary
programming_dictionary["Loop"] =  "The action of doing something over and over again"

# print entire dictionary
#print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

#Edit an existing element in the dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Removing an element from the dictionary
programming_dictionary.pop("Loop")
# print(programming_dictionary)

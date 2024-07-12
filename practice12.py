import random

states_of_india = ['Bombay', 'Sind', 'Madras', 'Bengal', 'Burma', 'Punjab']
states_of_india[0] = 'Mumbai'
print(states_of_india[0])     # prints the element at the first position
states_of_india.append('Telengana')  #Inserts at the last position
states_of_india.insert(3,'Mysuru')   # Inserts at our req pos
states_of_india.remove('Sind')       # Removes the mentioned element
states_of_india.extend(['Jammu & Kashmir', 'Goa'])  #Extends list by appending all the elements from the iterable
states_of_india.pop()    # removes the last element
print(states_of_india)

#------NESTED LISTS---------------
dirty_dozen = ["apple", "orange", "potato", "strawberry", "avacado",
                "grapes", "peas", "capcicum", "radish","brinjal", "watermelon", "cucumber"]
print(dirty_dozen)
fruits = ["apple", "orange","strawberry", "avacado","grapes","watermelon"]
veggies = ["potato", "peas", "capcicum", "radish","brinjal", "cucumber"]
dirty_dozen = [fruits, veggies]
print(dirty_dozen)
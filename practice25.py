country = input()
visits = int(input())
cities_visited = eval(input())
# Nesting a list inside a dictionary
# travel_log = {
#     "France" : {"cities_visited":["Paris", "Lazio", "Lille"], "total_visits" : 10},
#     "Germany" : {"Cities_visited" :["Berlin", "Munich", "Dortmunc"], "total_visits" : 10}
# }

# Nesting a dictionary inside a list
travel_log = [
     {
      "country":"France", 
      "cities_visited":["Paris", "Lazio", "Lille"],
      "total_visits" : 10
      },
     {
         "country":"Germany",
         "Cities_visited" :["Berlin", "Munich", "Dortmunc"], 
         "total_visits" : 10
         }
]

def add_new_country(name, visits, list_of_cities):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)  #append {new country} into {travel log}

add_new_country(country, visits, cities_visited)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favorite city is {travel_log[2]['cities'][2]}")
print(travel_log)
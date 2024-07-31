# Nesting a list inside a dictionary
travel_log = {
    "France" : {"cities_visited":["Paris", "Lazio", "Lille"], "total_visits" : 10},
    "Germany" : {"Cities_visited" :["Berlin", "Munich", "Dortmunc"], "total_visits" : 10}
}

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


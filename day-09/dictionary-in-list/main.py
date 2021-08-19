# list with country, visits, and cities
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]all 

# define a function to add new values to travel_log
def add_new_country(country_name, number_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = number_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

# call function and print travel_log updated
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
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
]

#function added to the travel_log.
def add_new_country(country, visits, cities):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = cities
  travel_log.append(new_country)
  
add_new_country(country="Russia", visits=2, cities=["Moscow", "Saint Petersburg"])
print(travel_log)

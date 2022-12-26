programming_dictionary = {"error": "error line",
                         "other": "other error line"}
print(programming_dictionary["error"])

#Adding new item to dictionary
programming_dictionary["new"] = "new error line"

print(programming_dictionary)

#Create an empty dictionary
other_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit a item in a dictionary
programming_dictionary["new"] = "modify text new error line"
print(programming_dictionary)

#Loop through dictionary
for key in programming_dictionary:
  #key
  print(key)
  #value
  print(programming_dictionary[key])



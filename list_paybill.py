import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
len_list = len(names)-1
num_random = random.randint(0, len_list )
print(names[num_random] + " is going to buy the meal today!")
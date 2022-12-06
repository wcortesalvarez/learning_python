print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    base_value = 15
elif size == "M":
  base_value = 20
elif size == "L":
  base_value = 25
else:
  print("Pizza size error")
  
if size == "S" or size == "M" or size == "L":
  if add_pepperoni == "Y":
    if size == "S":
      base_value += 2
    else:
      base_value += 3

  if extra_cheese == "Y":
    base_value += 1
    
  print(f"Your final bill is: ${base_value}.")
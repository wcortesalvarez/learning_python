print("Welcome to the tip calculator.")
bill = float(input("What was the total bill $"))
tip = int(input("What percentage tip would you like to give?, 10, 12, or , 15 "))
people = int(input("How many people to split the bill "))

person = (bill * (1+tip/100)) / people

round_value = round(person, 2)

format_value = "{:.2f}".format(round_value)

print(f"Each person should pay: ${format_value}")

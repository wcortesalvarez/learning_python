# Game Fizz - Buzz
for number in range (1, 101):
  if number % 3 == 0 and number % 5 == 0:
    string = "FizzBuzz"
  elif number % 3 == 0:
    string = "Fizz"
  elif number % 5 == 0:
    string = "Buzz"
  else:    
    string = number
  print(string)
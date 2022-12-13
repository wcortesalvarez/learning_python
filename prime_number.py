def prime_checker(number):
  result = 0
  for num in range(2, number-1):
    if number % num == 0:
      result = 1
      break
    else:
      result = 2
  if result == 1:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")    
    
n = int(input("Check this number: "))
prime_checker(number=n)
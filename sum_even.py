v_sum_even = 0
for number in range(2, 101):
  print(number)
  if number % 2 == 0:
    v_sum_even += number
print(v_sum_even)
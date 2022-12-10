import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

for i in range(word_length):
    display += "_"

v_repeat = True
while v_repeat:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter
  print(display)      
  if "_" not in display:
    v_repeat = False
     
  


#encrypt and decrypt text 
#a single function

from logo_cipher import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function for encode and decode
def cipher(process, plain_text, shift_amount):
  cipher_text = ""
  message = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if process == 'encode':
      new_position = position + shift_amount
      message = "encoded"
    else:
      new_position = position - shift_amount
      message = "decoded"     
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The {message} text is {cipher_text}")

#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

repeat_cipher = 'Yes'
while repeat_cipher == 'Yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))  
  if direction == 'encode' or direction == 'decode':
   cipher(process=direction, plain_text=text, shift_amount=shift)
  else:
    print("Error in direction")
  repeat_cipher  = input("Repeat other cipher, Yes or No?")  


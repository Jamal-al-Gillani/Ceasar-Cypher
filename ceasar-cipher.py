#CEASAR Cypher

letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plainText, key):
  cipherText= ''
  for letter in plainText:
    letter = letter.lower()
    if not letter == '':
      index = letters.find(letter)
      if index== -1:
        cipherText += letter
      else:
        new_index = index + key
        if new_index >= num_letters:
          new_index -= num_letters
        cipherText += letters[new_index]
  return cipherText

def decrypt(cipherText, key):
  plainText= ''
  for letter in cipherText:
    letter = letter.lower()
    if not letter == '':
      index = letters.find(letter)
      if index== -1:
        plainText += letter
      else:
        new_index = index - key
        if new_index < 0:
          new_index += num_letters
        plainText += letters[new_index]
  return plainText



print()
print("****CAESAR CIPHER PROGRAM****")
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
  print('ENCRYPTION MODE SELECTED')
  print()
  key = int (input('Enter the key (1 to 26): '))
  text = input('Enter the text to encrypt: ')
  cipherText = encrypt(text, key)
  print(f'CIPHER TEXT : {cipherText} ')

elif user_input == 'd':
  print('DECRYPTION MODE SELCTED ')
  print()
  key = int (input('Enter the key(1 to 26): '))
  text = input('Enter the text to decrypt: ')
  plainText = decrypt(text, key)
  print(f'PLAIN TEXT : {plainText} ')
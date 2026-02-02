# TODO здесь писать код

def caesar_cipher(user_plaintext, user_shift):
  char_list = [(alphabet[(alphabet.index(symb) + user_shift) % 33] if symb != ' ' else ' ') for symb in user_plaintext]
  new_str = ''
  for i_char in char_list:
    new_str += i_char
  return new_str


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
plaintext = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

ciphertext = caesar_cipher(plaintext, shift)

print("Зашифрованное сообщение:", ciphertext)

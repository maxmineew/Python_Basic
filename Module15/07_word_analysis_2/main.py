# TODO здесь писать код

def is_palindrome(word):
    return word == word[::-1]

word = input("Введите слово: ")
if is_palindrome(word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
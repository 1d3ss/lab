abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzабвгґдеєжзиіїйклмнопрстуфчцчшщьюяабвгґдеєжзиіїйклмнопрстуфчцчшщьюя12345678901234567890"

encrypt = input("Enter text: ")
key = 2
# int(input("Enter a key[number from 1-25]: "))
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = abc.find(letter)
    newPosition = position + key
    if letter in abc:
        encrypted = encrypted + abc[newPosition]
    else:
        encrypted = encrypted + letter

print("Your cipher is: ", encrypted)

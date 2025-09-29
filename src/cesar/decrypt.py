with open('./output/cesar.txt') as arq:
    text = arq.read()

value = 2

print(text)
newString = ''

for letter in text:
    numberLetter = ord(letter)
    numberLetter-= value
    numberLetter = numberLetter  % 255
    newString += chr(numberLetter)

print('descriptografado -> ',newString)

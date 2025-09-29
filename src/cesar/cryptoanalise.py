with open('./output/cesar.txt') as arq:
    text = arq.read()

with open('./input/cesar.txt') as arq:
    text2 = arq.read()


print(text)

for value in range(255):
  newString = ''
  for letter in text:
    numberLetter = ord(letter)
    numberLetter+= value
    numberLetter = numberLetter % 255
    newString += chr(numberLetter)
  print('tentativa ',value,' -> ', newString)


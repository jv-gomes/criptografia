with open('./output/cesar.txt') as arq:
    text = arq.read()

with open('./output/histo_alf.txt') as arq:
    hist = arq.read()

newString = ''

newDict = dict()
for letter in text:
    newDict[letter] = newDict.get(letter, 0) + 1


def total_words(hist1):
    return sum(hist1.values())

def different_words(hist1):
    return len(hist1)

def sorted_hist(hist1):
    return sorted(hist1, key = hist1.get, reverse=True)


sortVal = sorted_hist(newDict)

copyString = text

count = 0
for val in sortVal:
    copyString = copyString.replace(val, hist[count])

    count = count + 1

print(count)
print(copyString.replace('\n',''))
# print('total -> ',total_words(newDict))
# print('diferente -> ',different_words(newDict))
# print('sorted -> ',sorted_hist(newDict))
# with open("./output/cesar.txt", "w") as f:
#     f.write(newString)
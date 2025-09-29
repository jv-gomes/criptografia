import string
import re

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        processText = re.sub(r'[^a-zA-Z]', '', line)
        process_line(processText, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for letter in line:
        hist[letter] = hist.get(letter, 0) + 1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def sorted_hist(hist):
    return sorted(hist, key = hist.get, reverse=True)

hist = process_file('./textos/obras_machado_de_assis.csv')


print('total -> ',total_words(hist))
print('diferente -> ',different_words(hist))
print('sorted -> ',sorted_hist(hist))

with open("./output/histo_alf.txt", "w") as f:
    for value in sorted_hist(hist):
      f.write(value+"\n")
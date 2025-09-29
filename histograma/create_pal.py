import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

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

with open("./output/histo_pal.txt", "w") as f:
    for value in sorted_hist(hist):
      f.write(value+"\n")
ifile = open('text.txt')
ofile = open('otext.txt' , mode = 'w')

sentence = ifile.read()

words = sentence.split()

words.sorts()
print(words)

for word in words:
    ofile.write(word +" ")

ofile.close()

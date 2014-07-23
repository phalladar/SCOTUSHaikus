from haikufinder import *
from nltk.util import ngrams
import random, re

f = open('hobbylobby.txt', 'r')
theText = f.read()

theHaiku = []

n = 2
thengram = ngrams(theText.split(), n)


# for rando in range(1, len(thengram) - 1):
# 	rando = random.randrange(0, len(thengram), 1)
# 	if count_syllables(' '.join(thengram[rando])) == 5 and ' '.join(thengram[rando]).upper() != ' '.join(thengram[rando]) and ' '.join(thengram[rando])[0] == ' '.join(thengram[rando])[0].upper() and thengram[rando][0].find(r'\d') != -1:
# 		theHaiku.append(' '.join(thengram[rando]))
# 		break

for rando in range(1, len(thengram) - 1):
	rando = random.randrange(0, len(thengram), 1)
	if count_syllables(' '.join(thengram[rando])) == 5 and ' '.join(thengram[rando]).upper() != ' '.join(thengram[rando]):
		theHaiku.append(' '.join(thengram[rando]))
		break


for rando in range(1, len(thengram) - 1):
	rando = random.randrange(0, len(thengram), 1)
	if count_syllables(' '.join(thengram[rando])) == 7 and ' '.join(thengram[rando]).upper() != ' '.join(thengram[rando]):
		theHaiku.append(' '.join(thengram[rando]))
		break

for rando in range(1, len(thengram) - 1):
	rando = random.randrange(0, len(thengram), 1)
	if count_syllables(' '.join(thengram[rando])) == 5 and ' '.join(thengram[rando]).upper() != ' '.join(thengram[rando]):
		theHaiku.append(' '.join(thengram[rando]))
		break

print ' '.join(theHaiku)


#print count_syllables("testing")

# Consider on haiku line breaks generating a bigram:
# http://nltk.googlecode.com/svn/trunk/doc/book/ch02.html#chap-corpora
# to make sure the lines flow.

# Could generate a bi-gram for ending of a line then find an instance of the 
# randomly generated word for the next line.
from haikufinder import *
from nltk.util import ngrams
import random, re

correctSylables = []
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

f = open('hobbylobby.txt', 'r')
theText = f.read()

sentences = tokenizer.tokenize(theText)
for i in sentences:
	if count_syllables(' '.join(i)) == 17:
		correctSylables.append(' '.join(i))

print correctSylables
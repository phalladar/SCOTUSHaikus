from haikufinder import *
from nltk.util import ngrams
import random, re


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


# theText = ['on others" or that require "the general public [to] pick up the tab.', 'For good reason, we have repeatedly refused to take such a step.', 'But the Lee Court made two key points one cannot confine to tax cases.', 'I part ways with JUSTICE KENNEDY on the context relevant here.', 'In no way does the dissent "tell the plaintiffs that their beliefs are flawed.']


# print correctSylables
def findAllHaikus(theText): # identifies all Haikus in a text
	correctSylables = []
	allHaikus = []
	sentences = tokenizer.tokenize(theText)
	for i in sentences:
		if count_syllables(i) == 17:
			correctSylables.append(i)
	for i in correctSylables:
		if isHaiku(i):
			allHaikus.append(i)
	return allHaikus

def isHaiku(presumptiveHaiku):
	possibleHaiku = presumptiveHaiku.split() # already identified as having 17 syllables
	line1, line2, line3 = '', '', ''

	aHaikuLine1 = ''
	for j in possibleHaiku:
		aHaikuLine1 = aHaikuLine1 + ' ' + j	
		if count_syllables(aHaikuLine1) == 5:
			possibleSecondLine = presumptiveHaiku[len(aHaikuLine1):].split()
			
			aHaikuLine2 = ''
			for k in possibleSecondLine:
				aHaikuLine2 = aHaikuLine2 + ' ' + k
				if count_syllables(aHaikuLine2) == 7:
					#print aHaikuLine1 + aHaikuLine2
					possibleThirdLine = presumptiveHaiku[len(aHaikuLine1 + aHaikuLine2):].split()

					aHaikuLine3 = ''
					for l in possibleThirdLine:
						aHaikuLine3 = aHaikuLine3 + ' ' + l
						if count_syllables(aHaikuLine3) == 5:
							return True
							break
	return False

#print isHaiku(theText[2])
f = open('hobbylobby.txt', 'r')
theText = f.read()

x = findAllHaikus(theText)
for i in x:
	print i 
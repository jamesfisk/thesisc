from __future__ import division
from corpus import *
import nltk

"""
get frequency of each single letter. put all to lower case. no punctuation
"""
def get_letter_freq(text):
	text = list(text)
	sumAll = 0
	ascii = [x-x for x in range(26)]

	for letter in text:
		if not letter.isalpha():
			continue
		sumAll += 1
		ascii[ord(letter.lower()) - 97] += 1

	ascii = [x / sumAll * 100 for x in ascii]

	return ascii
	

def print_letter_freq(corpus):
	text = list(corpus.raw())
	sumAll = 0
	ascii = [x-x for x in range(128)]

	for letter in text:
		sumAll += 1
		ascii[ord(letter.lower())] += 1

	#for i in range(33, 128):
		#if (i < 65 or i > 90):
			#print "%r"  % chr(i),
			#print (ascii[i] / sumAll * 100), ascii[i]
	print "print", [x / sumAll * 100 for x in ascii]


if __name__ == "__main__":
	zones = get_zone_corpus()
	sonnets = get_sonnet_corpus()

	for i in range(len(zones)):
		print "Corpus", i + 1
		print
		print_letter_freq(zones[i])

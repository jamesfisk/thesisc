"""
Tests
-single letter frequency
"""

from __future__ import division
from corpus import *
import nltk

"""
RETURNS FREQUENCY OF A-Z CASE INSENSITIVE PLUS "-" AND "'" AT THE END OF VECTOR
[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, -, ']

Including nullAux parameter so it will work with centroid
"""
def get_letter_freq(text, nullAux):
	text = list(text)
	sumAll = 0
	ascii = [x-x for x in range(26)]
	lil_punct = [0,0] #just for apostraphe and dash

	for letter in text:
		if not letter.isalpha():
			if letter == "-":
				lil_punct[0] += 1
				sumAll += 1
			elif letter == "'":
				lil_punct[1] += 1
				sumAll += 1

			continue
		try:
			ascii[ord(letter.lower()) - 97] += 1
			sumAll += 1
		except IndexError:
			True
			#print 'problem letter', letter

	ascii = [x / sumAll * 100 for x in ascii]
	lil_punct = [x / sumAll * 100 for x in lil_punct]
	return ascii + lil_punct

def get_semicolon_freq(text, nullAux):
	text = list(text)
	total = len(text)
	sc = 0

	for elt in text:
		if elt == ";":
			sc += 1


	return [sc, sc/total]
	


def print_letter_freq(corpus):
	text = list(corpus.raw())
	sumAll = 0
	ascii = [x-x for x in range(128)]

	for letter in text:
		try:
			sumAll += 1
			ascii[ord(letter.lower())] += 1
		except IndexError:
			print "problem letter", letter
			continue

	for i in range(33, 128):
		if (i < 65 or i > 90):
			print "%r"  % chr(i),
			print (ascii[i] / sumAll * 100) #ascii[i]
	#print "print", [x / sumAll * 100 for x in ascii]


if __name__ == "__main__":

	s = get_sonnet_corpus()
	p = get_letter_freq(s.raw(), None)
	print "Sonnets"
	for elt in p:
		print elt

	"""
	zones = get_zone_corpus()
	datas = []

	for i in range(len(zones)):
		print
		avg = 0
		for elt in zones[i].fileids():
			s = get_semicolon_freq(zones[i].raw(elt), None)
			avg += s[1] * 100
			print elt, s[0], s[1] * 100
		print "Average", avg / len(zones[i].fileids())

	"""






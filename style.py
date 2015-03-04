from __future__ import division
from corpus import *
from syllable import *
from distances import *

"""
returns vector of frequency of words at length x where x is the vector index. up to 27.
"""


def word_length(text, nullAux):
	totalwords = 0
	counts = [0.0 for x in range(18)]

	text = text.split()
	for elt in text:
		totalwords += 1
		idx = len(elt)
		if idx == 0:
			print "HAY",elt
		if idx == -1:
			print "HOO",elt
		if idx > len(counts):
			continue


		counts[idx - 1] += 1

	#return counts
	return [x / totalwords * 100 for x in counts]

def word_syllable(text, nullAux):
	totalwords = 0
	counts = [0.0 for x in range(6)]

	text = text.split()
	for elt in text:
		totalwords += 1
		syllable = sylco(elt)
		#if syllable > 8:
		#	continue
		if syllable == 0:	#let's not do zero syllable words
			syllable = 1
		if syllable > len(counts):
			print elt
			continue

		#print elt
		counts[syllable - 1] += 1

	#return counts

	#if word not present, add .5
	for i in range(len(counts)):
		if counts[i] == 0:
			counts[i] += .1

	return [x / totalwords * 100 for x in counts]

def syllable_per_line(text, delim):
	linect = 0
	sylct = 0
	counts = [0.0 for x in range(25)]

	text = text.split(delim)
	#print text
	for line in text:
		sylct = 0
		words = line.split()

		if len(words) == 0:
			continue
		#print 
		#print

		
		for word in words:
			if word.isdigit():
				continue
			sylct += sylco(word)

		if sylct == 0:
			continue
		#print line[:-1], sylct
		

		if sylct <= 25:
			linect += 1
			counts[sylct - 1] += 1



	#return counts
	return [x / linect * 100 for x in counts]

def run_test_on_zones(func, aux):
	test = get_line_number_zone_corpus()
	d = []
	for elt in test:
		d.append(func(elt.raw(), aux))
	for i in range(len(d)):
		print "Corpus", i+1
		for elt in d[i]:
			print elt
		print

	print_zone_distances(d)
	print

	for k in range(len(d)):
		print "Mean of zone", k + 1
		sump = 0
		for j in range(len(d[k])):
			sump += d[k][j] * (j + 1)
		print sump / 100.0



if __name__ == "__main__":

	run_test_on_zones(syllable_per_line, "|L")
	"""
	s = get_nopunct_sonnet_corpus()
	p = word_length(s.raw(), None)
	print "Sonnets"
	for elt in p:
		print elt
	"""

	"""
	s = get_nopunct_sonnet_corpus().raw()
	p = word_syllable(s, None)
	for elt in p:
		print elt
	print "Mean of son"
	sump = 0
	for j in range(len(p)):
		sump += p[j] * (j + 1)
	print sump / 100.0
	"""



	




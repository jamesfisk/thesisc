"""
Tests:
-frequency of top 96 digrams
"""


from __future__ import division
from corpus import *
from distances import *
import os
import io
import operator
import pickle


def strip_whitespace(text):
	text = text.split()
	text = "_".join(text)
	return text
def count_all_digrams(text, digrams):
	text = list(strip_whitespace(text))

	for i in range(len(text) - 1):
		digram = text[i].lower() + text[i + 1].lower()
		if (digram not in digrams):
			digrams[digram] = 1
		else:
			digrams[digram] += 1

	for key in digrams:
		digrams[key] = digrams[key] / (len(text) - 1)

	return digrams

def top_96_digrams_freq(text):
	digrams = count_all_digrams(text, {})
	sorted_d = sorted(digrams.items(), key=operator.itemgetter(1), reverse=True)
	sorted_d = sorted_d[:98]
	#print sorted_d
	return [y for (x, y) in sorted_d]
	#return sorted_d

def top_96_digrams_keys(text):
	digrams = count_all_digrams(text, {})
	sorted_d = sorted(digrams.items(), key=operator.itemgetter(1), reverse=True)
	sorted_d = sorted_d[:98]
	#print sorted_d
	return [x for (x, y) in sorted_d]

def top_96_corpus_digrams_keys():
	return pickle.load(open("./res/corpus_digrms.p", "r"))

"""
returns frequency array of a passed list of digrams
"""
def find_digrams(text, digrams):
	text = list(strip_whitespace(text))
	sumAll = 0
	retlist = [0 for x in range(len(digrams))]

	for i in range(len(text) - 1):
		digram = text[i].lower() + text[i + 1].lower()
		if digram in digrams:
			retlist[digrams.index(digram)] += 1

	return [x / (len(text) - 1) for x in retlist]

		




if __name__ == "__main__":
	p = get_clean_corpus()
	s = get_nopunct_sonnet_corpus()
	k = top_96_digrams_keys(p.raw())
	d = []
	for elt in k:
		print elt

	z = get_clean_zone_corpus()
	for i in range(len(z)):
		q = find_digrams(z[i].raw(), k)
		d.append(q)
		print "Zone", i + 1
		for j in range(len(q)):
			print  q[j]
		print
	print "Sonnets"
	q = find_digrams(s.raw(), k)
	for elt in q:
		print elt

	print_zone_distances(d)







"""
Tests:
-frequency of top 96 words

"""

from __future__ import division
from corpus import *
from parse import *
from distances import *
import os
import io
import json
import operator
import math


"""
returns a dictionary with word/freq pairs for given text string.
takes word list
"""
def word_freq(text, words):
	for word in text:
		word = word.lower()
		if (word not in words):
			words[word] = 1
		else:
			words[word] += 1

	for key in words:
		words[key] = words[key] / len(text)
	return words
"""
return dictionary with actual word counts of a text. should take same
input as word_freq for this to work.
"""
def count_all_words(text, words):
	for word in text:
		word = word.lower()
		if (word not in words):
			words[word] = 1
		else:
			words[word] += 1
	return words

"""
look for anomalous words in text word list obs (observed)
based on frequencies from text word list exp (expected)
"""
def chi_square_test(exp, obs):
	exp_freq = word_freq(exp, {})
	obs_count = count_all_words(obs, {})
	total = count_all_words(exp, {})

	words = []

	length = len(obs)
	anom = 0
	for key in obs_count:
		if total[key] == 1:
			continue

		wc = obs_count[key]
		ex = exp_freq[key] * length

		chi_square = ((wc - ex)**2)/ex
		
		if (chi_square >= 3.84):
			
			if (wc > ex):		#only if more words than expected
				if (key == 'was'):
					print key, "expected %.2f" % ex, "observed", wc, "total", total[key]

				words.append(key)
				anom +=1
				#print key, "expected %.2f" % ex, "observed", wc, "total", total[key]

	print "anomalous words", anom, "total words", len(obs_count)
	#print words
	return [set(words), obs_count]



def top_96_words_freq(text):
	words = count_all_words(text, {})
	sorted_d = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
	sorted_d = sorted_d[:98]
	#print sorted_d
	return [y for (x, y) in sorted_d]
	#return sorted_d

def top_96_words_keys(text):
	words = count_all_words(text, {})
	sorted_d = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
	sorted_d = sorted_d[:98]
	#print sorted_d
	return [x for (x, y) in sorted_d]

def write_top_500_words_to_file(text, name):
	fp = open("./wordfreq/" + name + ".json", 'wb')
	w = count_all_words(text, {})
	sorted_d = sorted(w.items(), key=operator.itemgetter(1), reverse=True)
	sorted_d = sorted_d[:500]
	json.dump(sorted_d, fp)

"""
returns frequency array of a passed list of words
"""
def find_words(text, words):
	text = text.split()
	retlist = [0 for x in range(len(words))]

	for word in text:
		word = word.lower()
		if word in words:
			retlist[words.index(word)] += 1

	return [x / (len(text) - 1) for x in retlist]

"""
return array of sets of distinctive words
"""
		
def get_zone_distinctive_words():
	w = []
	z = get_pos_zones()
	q = []

	for i in range(len(z)):
		 z[i] = lemmatize(z[i])
		 q += z[i]


	for elt in z:
		w.append(chi_square_test(q, elt))
	return w


if __name__ == "__main__":

	s = get_pos_sonnets()
	s = set(lemmatize(s))

	z = get_clean_zone_corpus()

	w = get_zone_distinctive_words()
	"""
	outfile = open("proportions.csv", "w")
	outfile.write(",,Period 1,Period 2,Period 3,Period 4\n")

	for i in range(len(w)):
		dwords = sorted(list(set(w[i][0]) & s))
		#print "zone", i + 1
		outfile.write("Period " + str(i + 1))
		for j in range(len(dwords)):
			key = dwords[j]
			counts = []
			for k in range(4):
				try:
					counts.append(w[k][1][key])
				except:
					counts.append(0)
			allelts = sum(counts)
			prop = [x / allelts for x in counts]
			prop = [str("%.5f" % x) for x in prop]
			#counts = [str(x) for x in counts]
			outfile.write("," + ",".join([key] + prop) + "\n")
			#print key, counts[0], counts[1], counts[2], counts[3]
		outfile.write(",,,,,\n")
		#print "\n"
	outfile.close()






	for i in range(len(w)):
		print "zone", i + 1, "has", len(w[i]), "distinctive words"
	for k in range(len(w)):
		for j in range(len(w)):
			if (k != j):
				print "zones", k + 1, "and", j + 1, "have", len(w[k] & w[j]), "words in common"
	for k in range(len(w)):
		pw = w[k]
		for j in range(len(w)):
			if (j != k):
				pw -= w[j]
		print "zone", k + 1, "has", len(pw), "unique distinctive words"


	special_words = w[0] | w[1] | w[2] | w[3]
	words = s & special_words
		"""

	

	


	


	

from __future__ import division
from corpus import *
import os
import io
import operator



def count_all_words(text, words):
	text = text.split()
	for word in text:
		word = word.lower()
		if (word not in words):
			words[word] = 1
		else:
			words[word] += 1

	for key in words:
		words[key] = words[key] / (len(text) - 1)

	return words

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

		




if __name__ == "__main__":
	zones = get_zone_corpus()
	words = {}
	for i in range(len(zones)):
		words = count_all_words(zones[0].raw(), words)
	sorted_d = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
	print sorted_d[:98]
	print [x for (x, y) in sorted_d[:98]]


from __future__ import division
from corpus import *
from parse import *
from datetime import datetime
import os
import io
import heapq


def build_word_digrams(text):
	text = text.split()
	digrams = {}
	for i in range(len(text) - 1):
		digram = text[i] + " " + text[i + 1]
		if (digram not in digrams):
			digrams[digram] = -1
		else:
			digrams[digram] -= 1
	return digrams

def build_word_trigrams(text):
	text = text.split()
	trigrams = {}
	for i in range(len(text) - 2):
		trigram = text[i] + " " + text[i + 1] + " " + text[i + 2]
		if (trigram not in trigrams):
			trigrams[trigram] = -1
		else:
			trigrams[trigram] -= 1
	return trigrams

def build_heap(digrams, trigrams):
	h = []
	for key, value in digrams.iteritems():
		tup = (value, key)
		heapq.heappush(h, tup)
	for key, value in trigrams.iteritems():
		ttup = (value, key)
		heapq.heappush(h, ttup)
	return h

def top_96_phrases():
	return



if __name__ == '__main__':
	startTime = datetime.now()		
	son = get_zone_corpus()[0].raw()
	son = remove_punct(son)
	d = build_word_digrams(son)
	t = build_word_trigrams(son)
	h = build_heap(d, t)
	for i in range(500):
		phrase = heapq.heappop(h)
		print i, phrase, len(phrase[1].split()) 
	print(datetime.now()-startTime)



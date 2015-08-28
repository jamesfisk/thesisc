from __future__ import division
from corpus import *
from parse import *


def find_play_from_phrase(phrase):
	phrase = " ".join([word_minus_punct(word.lower()) for word in phrase.split()])
	n = len(phrase.split())



	q = get_nopunct_sonnet_corpus()
	for elt in q.fileids():
		txt = [word.lower() for word in q.raw(elt).split()]
		for i in range(len(txt) - n + 1):
			phr = ""
			for k in range(n):
				phr += txt[i + k] + " "
			if phr.split() == phrase.split():
				print "sonnet", elt


	p = get_clean_zone_corpus()
	zone_count = [0, 0, 0, 0]
	zone_freq = [0.0, 0.0, 0.0, 0.0]
	for z in range(len(p)):		#zone loop
		ct = 0	
		sumP = 0
		for elt in p[z].fileids():		#play loop
			txtz = [word_minus_punct(word.lower()) for word in p[z].raw(elt).split()]
			for i in range(len(txtz) - n + 1):
				sumP += 1
				phrz = ""
				for k in range(n):
					phrz += txtz[i + k] + " "

				if phrz.split() == phrase.split():
					ct += 1
					print "zone", z + 1, "number", elt
		zone_count[z] = ct
		zone_freq[z] = ct / sumP
	
	for k in range(len(zone_count)):
		print zone_count[k], "total in zone", k + 1, "freq", zone_freq[k]

	print zone_count[0] + zone_count[1], "in first half and", zone_count[2] + zone_count[3], "in second half"
	#print abs((zone_count[0] + zone_count[1]) - (zone_count[2] + zone_count[3])), "difference"
				




def find_play_from_word(word):
	q = get_nopunct_sonnet_corpus()
	for elt in q.fileids():
		for g in q.raw(elt).split():
			if g.lower() == word:
				print "sonnet", elt
		
				"""
	w = get_clean_corpus()
	for elt in w.fileids():
		for h in w.raw(elt).split():
			if h.lower() == word:
				print elt"""


	p = get_clean_zone_corpus()
	zone_count = [0, 0, 0, 0]
	zone_freq = [0.0, 0.0, 0.0, 0.0]
	for i in range(len(p)):
		ct = 0	
		sumP = 0
		for elt in p[i].fileids():
			for j in p[i].raw(elt).split():
				sumP += 1
				if j.lower() == word:
					ct += 1
					print "zone", i + 1, "number", elt
		zone_count[i] = ct
		zone_freq[i] = ct / sumP
	
	for k in range(len(zone_count)):
		print zone_count[k], "total in zone", k + 1, "freq", zone_freq[k]

	print zone_count[0] + zone_count[1], "in first half and", zone_count[2] + zone_count[3], "in second half"
	#print abs((zone_count[0] + zone_count[1]) - (zone_count[2] + zone_count[3])), "difference"
				
if __name__ == '__main__':
	word = "abc"
	while True:
		word = raw_input("Word: ")
		if word == "0":
			exit()
		if len(word.split()) > 1:
			find_play_from_phrase(word)
		else:
			find_play_from_word(word)







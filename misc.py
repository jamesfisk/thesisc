from __future__ import division
from corpus import *




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

	print zone_count[0] + zone_count[1], "in first half and", zone_count[2] + zone_count[3], "in second half",
	#print abs((zone_count[0] + zone_count[1]) - (zone_count[2] + zone_count[3])), "difference"
				
if __name__ == '__main__':
	word = "abc"
	while word != "0":
		word = raw_input("Word: ")
		find_play_from_word(word)

from corpus import *
from word import *
from parse import *


def find_dislegomena(text):
	text = [word.lower() for word in text.split()]
	counts = count_all_words(text, {})
	print counts["frolic"]
	dl = set()
	for key in counts:
		if counts[key] == 2:
			dl.add(key)
	return dl

def find_trislegomena(text):
	text = [word.lower() for word in text.split()]
	counts = count_all_words(text, {})
	tl = set()
	for key in counts:
		if counts[key] == 3:
			tl.add(key)
	return tl

if __name__ == '__main__':
	q = get_clean_corpus()
	s = get_nopunct_sonnet_corpus()
	d = find_dislegomena(q.raw() + " " + s.raw())
	words = [word.lower() for word in s.raw().split()]
	play = set(words)
	for word in d:
		if word in play:
			print word


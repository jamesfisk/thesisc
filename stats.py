from __future__ import division
from nltk.tokenize import RegexpTokenizer
import os
import io
import string



def print_stats(corpus):
	print "corpus: ", corpus
	print "length: ", str(len(raw_no_punctuation(corpus).split()))
	print "length rawsplit: ", str(len(corpus.raw().split()))

	print "avg word len, avg sen len, lexical diversity"

	for ida in corpus.fileids():
	     	num_chars = len(corpus.raw(ida))
	     	num_words = len(corpus.words(ida))
	     	num_sents = len(corpus.sents(ida))
	     	num_vocab = len(set([w.lower() for w in corpus.words(ida)]))
	     	print num_chars/num_words, num_words/num_sents, num_words/num_vocab, ida




	



if __name__ == "__main__": 
	#outfile = open("sonnet_stats.txt", "w")
	path = "/Users/jamesfisk/Desktop/thesisc/son/"

	files = os.listdir(path)
	files = [x for x in files if x[-4:] == ".txt"]

	minlen = 400000
	maxlen = -1
	sumall = 0
	for sonnet in files:
		infile = open(path + sonnet, "r")
		words = infile.read().split()
		length = len(words)
		if length > maxlen:
			maxlen = length
		if length < minlen:
			minlen = length
		sumall += length

	print ("Average length: " + str(sumall / 154) + 
		  "\nMax length: " + str(maxlen) + 
		  "\nMin length: " + str(minlen) +
		  "\nTotal length: " + str(sumall))


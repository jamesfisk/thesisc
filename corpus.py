from nltk.corpus import PlaintextCorpusReader
import os
import random



def get_sonnet_corpus():
	sonnet_corpus_path = "/Users/jamesfisk/Desktop/thesisc/son/"
	sonnets = PlaintextCorpusReader(sonnet_corpus_path, ".*\.txt")
	return sonnets

def get_rvsh_corpus():
	rvsh_corpus_path = "/Users/jamesfisk/Desktop/thesisc/clean/"
	rvsh = PlaintextCorpusReader(rvsh_corpus_path, ".*\.txt")
	return rvsh

def get_zone_corpus():
	zone_corpus_path = "/Users/jamesfisk/Desktop/thesisc/div/"
	zones = []
	for i in range(4):
		zones.append(PlaintextCorpusReader(zone_corpus_path + str(i + 1) + "/", ".*\.txt"))
	return zones

def get_test_corpus():
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/div/test/"
	test = []
	for i in range(4):
		test.append(PlaintextCorpusReader(test_corpus_path + str(i + 1) + "/", ".*\.txt"))
	return test

"""
get a testing corpus for each zone exclding files used for validation
"""
def get_test_corpus_minus_validation(validation):
	excluded = []
	for elt in validation:
		excluded.append(elt.fileids()[0])
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/div/test/"
	test = []

	for i in range(4):
		path = test_corpus_path + str(i + 1) + "/"
		included = [x for x in os.listdir(path) if x != excluded[i]]
		test.append(PlaintextCorpusReader(path, included))
	return test


"""
get a random sample to use for validation
"""
def get_random_validation_corpus():
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/div/test/"
	validation = []
	for i in range(4):
		chosen_one = random.choice([x for x in os.listdir(test_corpus_path + str(i + 1)) if x[-4:] == ".txt"])
		validation.append(PlaintextCorpusReader(test_corpus_path + str(i + 1) + "/", chosen_one))
	return validation




def raw_no_punctuation(corpus):
	txt =  list(corpus.raw())
	punctuation = (set(string.punctuation) - set("'"))
	punctuation = punctuation - set("-")
	ret = ""
	for elt in txt:
		if (elt not in punctuation):
			ret += elt
	return ret

"""
let's not use this one

def get_validation_corpus():
	validation_corpus_path = "/Users/jamesfisk/Desktop/thesisc/div/test/validation/"

	validation = PlaintextCorpusReader(validation_corpus_path, ".*\.txt")
	return validation
"""
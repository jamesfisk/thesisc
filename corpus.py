from nltk.corpus import PlaintextCorpusReader
import os
import random
import json

"""
SONNETS
"""

#rvsh text. no line numbers or medadata
def get_sonnet_corpus():
	sonnet_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/son/"
	sonnets = PlaintextCorpusReader(sonnet_corpus_path, ".*\.txt")
	return sonnets

#no punctuation except whitespace, dash, apostrophe
def get_nopunct_sonnet_corpus():
	sonnet_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/nopunct"
	sonnets = PlaintextCorpusReader(sonnet_corpus_path, ".*\.txt")
	return sonnets

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


"""
CLEAN BRUSTER TEXT. words only. no commas
"""
def get_clean_corpus():
	clean_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/cleantxt/"
	clean = PlaintextCorpusReader(clean_corpus_path, ".*\.txt")
	return clean

def get_clean_zone_corpus():
	clean_zone_path = "/Users/jamesfisk/Desktop/thesisc/res/cleanzones/"
	zones = []
	for i in range(4):
		zones.append(PlaintextCorpusReader(clean_zone_path + str(i + 1) + "/", ".*\.txt"))
	return zones

def get_clean_test_corpus_minus_validation(validation):
	excluded = []
	for elt in validation:
		excluded.append(elt.fileids()[0])
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/cleansamples/"
	test = []

	for i in range(4):
		path = test_corpus_path + str(i + 1) + "/"
		included = [x for x in os.listdir(path) if x != excluded[i] and x[-4:] == ".txt"]
		test.append(PlaintextCorpusReader(path, included))
	return test

def get_clean_random_validation_corpus():
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/cleansamples/"
	validation = []
	for i in range(4):
		chosen_one = random.choice([x for x in os.listdir(test_corpus_path + str(i + 1)) if x[-4:] == ".txt"])
		validation.append(PlaintextCorpusReader(test_corpus_path + str(i + 1) + "/", chosen_one))
	return validation

"""
REDACTED TEXTS. These are 1:1 with clean texts, but include punctuation and line info
"""
def get_redacted_corpus():
	redacted_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/redactedB/"
	redacted = PlaintextCorpusReader(redacted_corpus_path, ".*\.txt")
	return redacted

def get_redacted_zone_corpus():
	redacted_zone_path = "/Users/jamesfisk/Desktop/thesisc/res/redactedzones/"
	zones = []
	for i in range(4):
		zones.append(PlaintextCorpusReader(redacted_zone_path + str(i + 1) + "/", ".*\.txt"))
	return zones


"""
RIVERSIDE TEXTS. punctuation, line breaks, the whole shebang.
"""

def get_rvsh_corpus():
	rvsh_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/clean/"
	rvsh = PlaintextCorpusReader(rvsh_corpus_path, ".*\.txt")
	return rvsh

def get_zone_corpus():
	zone_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/div/"
	zones = []
	for i in range(4):
		zones.append(PlaintextCorpusReader(zone_corpus_path + str(i + 1) + "/", ".*\.txt"))
	return zones


def get_test_corpus():
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/div/test/"
	test = []
	for i in range(4):
		test.append(PlaintextCorpusReader(test_corpus_path + str(i + 1) + "/", ".*\.txt"))
	return test

def get_line_number_corpus():
	ln_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/linenumbers_final/"
	ln = PlaintextCorpusReader(ln_corpus_path, ".*\.txt")
	return ln

def get_line_number_zone_corpus():
	zone_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/linenumbers_zones/"
	zones = []
	for i in range(4):
		zones.append(PlaintextCorpusReader(zone_corpus_path + str(i + 1) + "/", ".*\.txt"))
	return zones

"""
get a testing corpus for each zone exclding files used for validation
"""
def get_test_corpus_minus_validation(validation):
	excluded = []
	for elt in validation:
		excluded.append(elt.fileids()[0])
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/div/test/"
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
	test_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/div/test/"
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
GET POS TAGGED ZONES. FROM CLEAN TEXT. RETURNED AS LIST.
"""

def get_pos_zones():
	pos_path = "/Users/jamesfisk/Desktop/thesisc/res/pos/"
	pos = []
	for i in range(4):
		filename = str(i + 1) + "pos.json"
		with open(pos_path + filename) as data_file:
			pos.append(json.load(data_file))
	return pos

def get_pos_sonnets():
	pos_path = "/Users/jamesfisk/Desktop/thesisc/res/sonpos/"
	with open(pos_path + "sonpos.json") as data_file:
		pos = json.load(data_file)
	return pos
			
"""
let's not use this one

def get_validation_corpus():
	validation_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/div/test/validation/"

	validation = PlaintextCorpusReader(validation_corpus_path, ".*\.txt")
	return validation
"""
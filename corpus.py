from nltk.corpus import PlaintextCorpusReader
import os
import random
import json
import pickle

"""
GLOBALS
"""
PERIOD1 = ['1H6', '2H6', '3H6', 'ARD', 'ERR', 'E3', 'LLL', 'MND', 'R3', 'ROM', 'SHR', 'TGV', 'TIT', 'LUC', 'VEN']
PERIOD2 = ['1H4', '2H4', 'ADO', 'H5', 'JC', 'JN', 'STM', 'MV', 'R2', 'WIV']
PERIOD3 = ['AWW', 'AYL', 'HAM', 'MFM', 'OTH', 'TN', 'TRO', 'PHT', 'LC']
PERIOD4 = ['ANT', 'COR', 'TIM', 'CYM', 'H8', 'LR', 'MAC', 'PER', 'TMP', 'TNK', 'WT']
PERIODS = [PERIOD1, PERIOD2, PERIOD3, PERIOD4]
ALLPLAYS = ['1H6', '2H6', '3H6', 'ARD', 'ERR', 'E3', 'LLL', 'MND', 'PHT', 'R3', 'ROM', 'SHR', 'TGV', 'TIT', 'LC', 'LUC', 'VEN', '1H4', '2H4', 'ADO', 'H5', 'JC', 'JN', 'STM', 'MOV', 'R2', 'WIV', 'AWW', 'AYL', 'HAM', 'MFM', 'OTH', 'TN', 'TRO', 'ANT', 'COR', 'TIM', 'CYM', 'H8', 'LR', 'MAC', 'PER', 'TMP', 'TNK', 'WT', 'PP']
PERDICT = {'TMP': 3, 'COR': 3, 'ERR': 0, 'TIT': 0, 'R2': 1,'R2R': 1, 'PER': 3, 'MFM': 2, 'TIM': 3, 'JN': 1, 'JNR': 1, 'LUC': 0, 'TGV': 0, 'JC': 1, 'JCR': 1, 'WT': 3, 'WTR': 3, '1H6': 0, 'ROM': 0, '1H4': 1, 'AWW': 2, '2H4': 1, '2H6': 0, 'TN': 2,'TNR': 2, 'LR': 3, 'LRR': 3, 'LLL': 0, 'MND': 0, 'EDW': 0, 'E3': 0, 'AYL': 2, 'SHR': 0, 'HAM': 2, '3H6': 0, 'R3': 0, 'R3R': 0, 'STM': 1, 'TRO': 2, 'VEN': 0, 'ADO': 1, 'TNK': 3, 'LC': 2, 'LC_': 2, 'OTH': 2, 'H8': 3, 'H8R': 3, 'H5': 1, 'H5R': 1, 'ANT': 3, 'WIV': 1, 'MAC': 3, 'MV': 1, 'MOV': 1, 'ARD': 0, 'CYM': 3, 'PHT': 2}
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

#returns strings, not corpuses
def get_sonnet_list():
	sonnet_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/nopunct/"
	sonnets = []
	for i in range(154):
		f = open(sonnet_corpus_path + str(i + 1) + ".txt")
		r = f.read()
		f.close()
		sonnets.append(r)
	return sonnets

#same as above, but lemmas instead of tokens
def get_sonnet_lemma_list():
	sonnet_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/sonlem/"
	sonnets = []
	for i in range(154):
		f = open(sonnet_corpus_path + str(i + 1) + "lem.txt")
		r = f.read()
		f.close()
		sonnets.append(r)
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

def get_xml_corpus():
	rvsh_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/rivsh/"
	rvsh = PlaintextCorpusReader(rvsh_corpus_path, ".*\.TXT")
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
	names = []
	for i in range(4):
		pos_pathB = pos_path + str(i +1) + "/"
		fids = os.listdir(pos_pathB)
		z = []
		n = []
		for fid in fids:
			p = pickle.load(open(pos_pathB + fid, "r"))
			z.append(p)
			n.append(fid)
		pos.append(z)
		names.append(n)

	return pos, names
"""
def get_pos_sonnets():
	pos_path = "/Users/jamesfisk/Desktop/thesisc/res/sonpos/"
	with open(pos_path + "sonpos.json") as data_file:
		pos = json.load(data_file)
	return pos
"""

def get_pos_sonnets_list():
	pos_path = "/Users/jamesfisk/Desktop/thesisc/res/sonpos2/"
	l = []
	for i in range(1, 155):
		l.append(pickle.load(open(pos_path + str(i) + "pos.p", "r")))
	return l

"""
LEMMATIZED TEXTS
"""
def get_sonnet_lemmas():
	pos_path = "/Users/jamesfisk/Desktop/thesisc/res/sonlem/"

	sonnets = PlaintextCorpusReader(pos_path, ".*\.txt")
	return sonnets
def get_lemma_zones():
	lem_path = "/Users/jamesfisk/Desktop/thesisc/res/zlem/"
	zones = []
	for i in range(4):
		zones.append(PlaintextCorpusReader(lem_path + str(i + 1) + "/", ".*\.txt"))
	return zones
def get_lemma_corpus():
	clem_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/clem/"
	clem = PlaintextCorpusReader(clem_corpus_path, ".*\.txt")
	return clem
"""
let's not use this one

def get_validation_corpus():
	validation_corpus_path = "/Users/jamesfisk/Desktop/thesisc/res/div/test/validation/"

	validation = PlaintextCorpusReader(validation_corpus_path, ".*\.txt")
	return validation
"""
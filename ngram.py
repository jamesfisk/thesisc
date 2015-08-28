from corpus import *
from parse import *
from collections import defaultdict
import pickle


def get_ngrams(n, text, name, d):
	txt = [word_minus_punct(word.lower()) for word in text.split()]

	for i in range(len(txt) - n + 1):
		s = ""
		for k in range(n):

			s += txt[i + k] + " "

		#add to d
		if s in d:
			d[s].append(name)
		else:
			d[s]  = [name]
	return d

def repeat_ngrams(d):
	return {key:value for key, value in d.items() if len(value) > 1}
def only_sonnets(d):
	return {key:value for key, value in d.items() if [s for s in value if not s.isdigit()] != value}

def print_ngrams(d):
	if d:	
		for key in d:
			print key, d[key]

def pickle_ngrams(filename, d):
	pickle.dump(d, open(filename + ".p", 'w'))
def load_pickle(filename):
	return pickle.load(open(filename, 'r'))

def write_ngrams_to_file(filename, d):
	f = open(filename, 'w')
	for key in d:
		f.write(key + " " + str(d[key]) + "\n")
def write_ngrams_to_csv(filename, d):
	f = open(filename, 'w')
	for key in d:
		f.write(key + "," + " ".join(d[key]) + "\n")

def isempty(d):
	if d:
		return False
	return True
"""
def intersect_dicts(son, cor):
	d = {}
	for key in 
"""
def get_ngrams_from_sonnets(n):
	text = get_nopunct_sonnet_corpus()
	d = defaultdict()
	for elt in text.fileids():
		d = get_ngrams(n, text.raw(elt), elt.split(".")[0], d)
	return repeat_ngrams(d)
	#print_ngrams(d)

"""
build a hierarchy of ngrams. remove repeated substrings.
n = max ngram length m = min ngram length
"""
def build_ngram_superset(ds): 
	l = [ds[0]]

	#d = get_ngrams(n, text)
	#l.append(d)
	for i in range(1, len(ds)):#n - 1, m - 1, -1):
		d = ds[i]#get_ngrams(i, text)
		di = {}
		if d:
			for key1 in d:
				substr = False
				for k in l:
					for key2 in k:
						if key1 in key2 and d[key1] == k[key2]:
							substr = True
				if not substr:
					di[key1] = d[key1]

		l.append(di)
	return l


def get_corpus_sonnet_ngrams(n):
	q = get_clean_corpus()
	son = get_nopunct_sonnet_corpus()
	d = defaultdict()


	for elt in son.fileids():
		d = get_ngrams(n, son.raw(elt), elt.split(".")[0], d)
	for elt in q.fileids():
		d = get_ngrams(n, q.raw(elt), elt[:3], d)

	return only_sonnets(repeat_ngrams(d))


def build_sonnet_play_overlap():

	ds = []
	for i in range(8, 1, -1):
		ds.append(get_corpus_sonnet_ngrams(i))

	l = build_ngram_superset(ds)
	n = 8
	for elt in l:
		#print_ngrams(elt)
		pickle_ngrams(str(n) + "gramsD.p", elt)
		write_ngrams_to_file(str(n) + "gramsD.txt", elt)
		#write_ngrams_to_csv(str(n) + "grams.csv", elt)
		print n, "gram. count: ", len(elt)
		n -= 1
def ngrams_by_sonnet(d):
	l = [[] for x in range(154)]
	for key in d:
		plays = [x for x in d[key] if not x.isdigit()]
		sonnets = [x for x in d[key] if x.isdigit()]
		for son in sonnets:
			l[int(son) - 1] += [x.strip() for x in plays]
	return l

def merge_ngrams(l):
	fl = [[] for x in range(154)]

	for item in l:
		for i in range(len(item)):
			fl[i] += item[i]
	return fl

"""
list (154 len) of shared ngrams for each sonnet/play"""
def get_son_ngram_thing():
	p = ngrams_by_sonnet(load_pickle("4gramsD.p.p"))
	q = ngrams_by_sonnet(load_pickle("5gramsD.p.p"))
	#r = ngrams_by_sonnet(load_pickle("3gramsD.p.p"))
	#s = ngrams_by_sonnet(load_pickle("2gramsD.p.p"))

	return merge_ngrams([p, q])

if __name__ == '__main__':
	l = get_son_ngram_thing()


	f = open("./spreadsheets/45onlygram_by_play.csv", "w")

	f.write("," + ",".join([str(x) for x in range(1, 155)]) + "\n")

	for period in PERIODS:
		for play in period:
			f.write(play + ",")
			if play == "MOV":
				play = "MV"

			for k in range(154):
				f.write(str(l[k].count(play)) + ",")
			f.write("\n")
		f.write("\n")
	f.close()





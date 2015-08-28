from __future__ import division
from corpus import *
from parse import *
from neural_cluster import *
from collections import defaultdict
import pickle


def get_dislogmena():
	q = get_lemma_corpus()
	s = get_sonnet_lemmas()
	words = defaultdict()

	for elt1 in q.fileids():
		text = [word_minus_punct(word.lower()) for word in q.raw(elt1).split()]

		words = count_words(text, words, elt1.split("lem")[0])

	for elt2 in s.fileids():
		text = [word_minus_punct(word.lower()) for word in s.raw(elt2).split()]

		words = count_words(text, words, elt2.split("lem")[0])

	return {key:value for key,value in words.items() if len(value) == 2 and len(set(value)) != 1}

def get_trislogmena():
	q = get_lemma_corpus()
	s = get_sonnet_lemmas()
	words = defaultdict()

	for elt1 in q.fileids():
		text = [word_minus_punct(word.lower()) for word in q.raw(elt1).split()]

		words = count_words(text, words, elt1.split("lem")[0])

	for elt2 in s.fileids():
		text = [word_minus_punct(word.lower()) for word in s.raw(elt2).split()]

		words = count_words(text, words, elt2.split("lem")[0])

	return {key:value for key,value in words.items() if len(value) == 3 and len(set(value)) != 1}

def get_quadlogmena():
	q = get_lemma_corpus()
	s = get_sonnet_lemmas()
	words = defaultdict()

	for elt1 in q.fileids():
		text = [word_minus_punct(word.lower()) for word in q.raw(elt1).split()]

		words = count_words(text, words, elt1.split("lem")[0])

	for elt2 in s.fileids():
		text = [word_minus_punct(word.lower()) for word in s.raw(elt2).split()]

		words = count_words(text, words, elt2.split("lem")[0])

	return {key:value for key,value in words.items() if len(value) == 4 and len(set(value)) != 1}

#return set of dislogmena, trislogmena, quadlogmena
def get_all_sarr_words():
	l = []
	k = [get_dislogmena(), get_trislogmena(), get_quadlogmena()]

	for d in k:
		l += [key for key, value in d.items()]
	pickle.dump(set(l), open("all_sarr_words.p", "w"))
	return set(l)


def print_sarrazin(d):
	for key in d:
		print key, " ".join(d[key])

def only_sonnets(d):
	return {key:value for key, value in d.items() if [s for s in value if not s.isdigit()] != value}

def load_all_dislogmena():
	return pickle.load(open("all_dislogmena.p", 'r'))
def load_son_dislogmena():
	return pickle.load(open("son_dislogmena.p", 'r'))

def load_all_trislogmena():
	return pickle.load(open("all_trislogmena.p", 'r'))
def load_son_trislogmena():
	return pickle.load(open("son_trislogmena.p", 'r'))

def count_words(text, words, fid):
	for word in text:
		word = word.lower()
		if (word not in words):
			words[word] = [fid]
		else:
			words[word].append(fid)
	return words

def write_dt_to_file():
	s = load_son_trislogmena()
	f = open("./spreadsheets/son_trislogmena.csv", "w")
	for key in s:
		f.write(key + "," + " ".join(sorted(s[key])) + "\n")
	f.close()

	s = load_son_dislogmena()
	f = open("./spreadsheets/son_dislogmena.csv", "w")
	for key in s:
		f.write(key + "," + " ".join(sorted(s[key])) + "\n")
	f.close()

def period_sarr_by_sonnet():
	p = load_son_dislogmena()
	p.update(load_son_trislogmena())
	s = [[] for x in range(154)]

	for period in PERIODS:
		ro = [0 for x in range(154)]
		for play in period:
			for key in p:
				l = p[key]
				if play in l:
					for item in l:
						try:
							q = int(item)
							ro[q-1] += 1
						except:
							pass
		for i in range(len(ro)):
			s[i].append(ro[i])
	return s

def sarrazin_in_text(txt):
	z = rare_words_by_period()
	txt = txt.split()
	r = [0 for x in range(4)]
	for i in range(len(z)):
		for word in z[i]:
			if word in txt:

				r[i] += 1.0
	#print
	return r

def sarrazin_in_text_holdout(txt, fid):
	d = build_sarr_by_divided_corpus()
	txt = txt.split()
	length = len(txt)
	r = [0 for x in range(4)]

	for word in txt:
		if word in d:
			works = d[word]
			#print word, d[word], "fid:", fid
			for item in works:
				if item != fid:
					r[int(item[0])] += 1.0

					#print "added", r
	#print
	return r

def sarrazin_in_text_holdout_sparse(txt, fid):
	swords = sorted([key for key in build_sarr_by_divided_corpus()])
	length = len(txt.split())
	cts = [0 for x in swords]
	print len(cts),
	for word in txt:
		if word in swords:
			cts[swords.index(word)] += 1.0
	#print
	return [x/length for x in cts]



def rare_words_by_period():
	p = load_all_dislogmena()
	p.update(load_all_trislogmena())
	z = [[] for x in range(4)]

	for key in p:
		plays = p[key]
		for play  in plays:
			if not play.isdigit():
				z[period_by_play(play)].append(key)


	return z



def period_by_play(play):
	for i, x in enumerate(PERIODS):
		if play in x:
			return i
	print "problem"
	print play
	exit()

def build_sarr_by_divided_corpus():
	p = load_all_dislogmena()
	p.update(load_all_trislogmena())
	d = defaultdict()

	z = pickle.load(open("./divided_corpus.p", "r"))
	for key in p:
		d[key] = []

	for i in range(len(z)):
		for k in range(len(z[i])):
			words = z[i][k].split()
			for w in words:
				if w in d:
					d[w].append(str(i) + "." + str(k))

	return d





#broken
def build_zone_spreadsheet():
	s = [set(x.split()) for x in get_sonnet_lemmas()]
	z = [set(x.raw().split()) for x in get_lemma_corpus()]
	w = set([key for key in load_son_dislogmena()] + [key for key in load_son_trislogmena()])
	f = open("./spreadsheets/sarr.csv", "w")
	for i in range(154):
		zop = [0, 0, 0, 0]
		for word in list(w & s[i]):
			for i in range(len(z)):
				if word in z[i]:
					zop[i] += 1
		f.write(",".join([str(x) for x in zop]) + "\n")

if __name__ == '__main__':
	d = divide_corpus()
	r = sarrazin_in_text_holdout(d[3][41], '3.41')
	q = sarrazin_in_text(d[3][41])
	print r
	print q


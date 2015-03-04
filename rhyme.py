from corpus import *
from parse import *
from collections import defaultdict
import json
import pickle

rhymes = defaultdict()

def rhymes_in_sonnet(sonnet, no):
	sonnet = sonnet.lower()
	lines = sonnet.split("\n")
	while (lines[0] == ""):
		lines.pop(0)
	for i in range(3):
		for k in range(2):
			pair = frozenset([word_minus_punct(lines[(i * 4) + k].split()[-1]), word_minus_punct(lines[(i * 4) + k + 2].split()[-1])])

			if pair in rhymes:
				rhymes[pair].append(no)
			else:
				rhymes[pair] = [no]
	pair = frozenset([word_minus_punct(lines[-1].split()[-1]), word_minus_punct(lines[-2].split()[-1])])


	if pair in rhymes:
		rhymes[pair].append(no)
	else:
		rhymes[pair] = [no]


def rhymes_in_corpus(d, text, no):
	text = text.lower()
	lines = text.split("\n")
	out = open("out.txt", 'w')

	for i in range(len(lines) - 2):
		if len(lines[i].split()) == 0:
			continue
		if lines[i].split()[-1] == "--":
				words1 = word_minus_punct(lines[i].split()[-2])
		else:
				words1 = word_minus_punct(lines[i].split()[-1])

		if len(lines[i + 1].split()) == 0:
			word2 = "asjdkifbircis"
		else:
			if lines[i + 1].split()[-1] == "--":
				words2 = word_minus_punct(lines[i + 1].split()[-2])
			else:
				words2 = word_minus_punct(lines[i + 1].split()[-1])

		if len(lines[i + 2].split()) == 0:
			words3 = "ituvnfcds"
		else:
			if lines[i + 2].split()[-1] == "--":
				words3 = word_minus_punct(lines[i + 2].split()[-2])
			else:
				words3 = word_minus_punct(lines[i + 2].split()[-1])

		pairs = [frozenset([words1, words2]), frozenset([words1, words3])]
		out.write("["+ words1 + " " + words2 + "] [" +  words1 + " " + words3 + "]\n")
		for elt in pairs:
			if elt in d:
				d[elt].append(no)
	out.close()
	return d




def add(word1, word2, no):
	pair = frozenset([word1, word2])
	if pair in rhymes:
		rhymes[pair].append(no)
	else:
		rhymes[pair] = [no]

def load_sonnet_dict():
	return pickle.load(open("son_rhymes.p", 'r'))

def load_all_rhyme():
	return pickle.load(open("all_rhymes.p", 'r'))

def build_sonnet_dict():
	s = get_nopunct_sonnet_corpus()
	f = open("sonnet_rhymes.txt", 'w')
	for i in range(1, 155):
		if i in [126, 99]:
			continue
		txt = s.raw(str(i) + ".txt")
		rhymes_in_sonnet(txt, str(i))

	#sonnet 99 rhymes
	add("chide", "pride", "99")
	add("pride", "dy'd", "99")
	add("dy'd", "chide", "99")
	add("smells", "dwells", "99")
	add("hand", "stand", "99")
	add("hair", "despair", "99")
	add("both", "growth", "99")
	add("breath", "death", "99")
	add("see", "thee", "99")

	#sonnet 126 rhymes
	add("power", "hour", "126")
	add("show'st", "grow'st", "126")
	add("wrack", "back", "126")
	add("skill", "kill", "126")
	add("pleasure", "treasure", "126")
	add("be", "thee", "126")

	for key in rhymes:
		p = list(key)
		if len(p) == 1:
			p.append(p[0])
		f.write(p[0] + " " + p[1] + str(rhymes[key]) + "\n")
		#print rhymes[key], p[0], p[1]
	pickle.dump(rhymes, open("son_rhymes.p", 'w'))
	f.close()

def build_all_dict():
	q = get_redacted_corpus()
	d = load_sonnet_dict()

	for fid in q.fileids():
		d = rhymes_in_corpus(d, q.raw(fid), fid[:3])

	pickle.dump(d, open('all_rhymes.p', 'w'))
	write_dict_to_file(d, "all_rhymes.txt")


def print_dict(d):
	for key in d:
		p = list(key)
		if len(p) == 1:
			p.append(p[0])
		print  p[0], p[1], d[key]

def write_dict_to_file(d, fid):
	f = open(fid, 'w')
	for key in d:
		p = list(key)
		if len(p) == 1:
			p.append(p[0])
		f.write(p[0] + " " + p[1] + str(d[key]) + "\n")

if __name__ == '__main__':




	p = load_all_rhyme()
	f = open("rhyme_data2.csv", 'w')
	for key in p:
		if len(p[key]) == 1:
			continue
		w = list(key)
		if len(w) == 1:
			w.append(w[0])
		f.write(w[0] + " " + w[1])
		l = sorted(p[key])
		for elt in l:
			f.write("," + elt)
		f.write("\n")
	f.close()





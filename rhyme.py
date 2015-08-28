from corpus import *
from parse import *
from collections import defaultdict
import json
import pickle

rhymes = defaultdict()

def rhymes_in_sonnet(sonnet, no):
	son_rhymes =[]
	sonnet = sonnet.lower()
	lines = sonnet.split("\n")
	while (lines[0] == ""):
		lines.pop(0)
	for i in range(3):
		for k in range(2):
			pair = frozenset([word_minus_punct(lines[(i * 4) + k].split()[-1]), word_minus_punct(lines[(i * 4) + k + 2].split()[-1])])
			son_rhymes.append(pair)
			if pair in rhymes:
				rhymes[pair].append(no)
			else:
				rhymes[pair] = [no]
	pair = frozenset([word_minus_punct(lines[-1].split()[-1]), word_minus_punct(lines[-2].split()[-1])])
	son_rhymes.append(pair)

	if pair in rhymes:
		rhymes[pair].append(no)
	else:
		rhymes[pair] = [no]

	return son_rhymes


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
	return pickle.load(open("all_rhymes2.p", 'r'))

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
		f.write(p[0] + " " + p[1] + " ".join(d[key]) + "\n")


def rhymes_by_plays():
	q = get_redacted_corpus()
	d = load_all_rhyme()

	f = open("rhymeB.csv", "w")

	for elt in q.fileids():
	     name = elt[:3]
	     son = []
	     for key in d:
	     	value = d[key]
	     	if name in value:
	        	son += [int(x) for x in value if x.isdigit()]
	     son = sorted(son)
	     f.write(name + "," + " ".join([str(x) for x in son]) + "\n")

def period_rhymes_by_sonnet():
	s = [[] for x in range(154)]
	p = pickle.load(open("rhyme_by_play.p"))

	for period in PERIODS:
		ro = [0 for x in range(154)]	
		for play in period:
			if play == 'MV':
				play  = 'MOV'
			for son in p[play]:
				ro[int(son) - 1] += 1
		for i in range(len(s)):
			s[i].append(ro[i])
	return s		

def build_sonnet_rhyme_ref():
	s = get_nopunct_sonnet_corpus()
	f = open("sonnet_rhymes.txt", 'w')
	q = []
	for i in range(1, 155):
		if i in [126, 99]:
			continue
		txt = s.raw(str(i) + ".txt")
		z = rhymes_in_sonnet(txt, str(i))
		z.append(i)
		q.append(z)
	return q

def shared_rhyme_by_quatrain():
	q = build_sonnet_rhyme_ref()
	z = load_all_rhyme()

	f = open("shared_rhyme_by_quatrain.csv", "w")
	f.write(",,Period 1, Period 2, Period 3, Period 4\n")
	for i in range(len(q)):
		f.write("Sonnet " + str(q[i][-1]) + "\n")
		rhymes = q[i]
		for p in range(3):
			zones = [0, 0, 0, 0]
			strhyme = ","
			f.write(",Quatrain " + str(p + 1) + ",")
			for k in range(2):
				rhyme = rhymes.pop(0)
				strhyme += "/".join(rhyme) + " "
				print rhyme, p, k
				shared = z[rhyme]
				for item in shared:
					if item.isdigit()or item.upper() in ['PPR', "LUC", "VEN"]:
						continue
					idx = PERDICT[item.upper()]
					zones[idx] += 1
			f.write(",".join([str(x) for x in zones]) + strhyme + "\n")

		f.write(",Couplet,")
		zones = [0, 0, 0, 0]
		strhyme = ","
		rhyme = rhymes.pop(0)
		strhyme += "/".join(rhyme) + " "
		shared = z[rhyme]
		for item in shared:
			if item.isdigit() or item.upper() in ['PPR', "LUC", "VEN"]:
				continue
			idx = PERDICT[item.upper()]
			zones[idx] += 1
		f.write(",".join([str(x) for x in zones]) + strhyme + "\n")






	f.close()

if __name__ == '__main__':
	shared_rhyme_by_quatrain()
	"""

	p = pickle.load(open("sorted_son_rhyme.p", "r"))
	f = open("rhyme_playsQ.csv", 'w')
	d = {}
	for i in range(len(p)):
		plays = p[i]

		for play in plays:
			if play not in d:
				d[play] = [str(i + 1)]
			else:
				d[play].append(str(i + 1))

	for key in d:
		d[key].sort(key=int)
	d['STM'] = []
	pickle.dump(d, open("rhyme_by_play.p", "w"))

	f.write("," + ",".join([str(x) for x in range(1, 155)]) + "\n")
	for period in PERIODS:
		for play in period:
			f.write(play + ",")
			for i in range(154):
				f.write(str(d[play].count(str(i + 1))) + ",")
			f.write("\n")
		f.write("\n")
	f.close()
	"""

		







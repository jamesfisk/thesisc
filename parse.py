
from nltk.stem import WordNetLemmatizer
from corpus import *
import string
import nltk
import json
import pickle

SUBS = [['luc', 'LUC'], ['ven', 'VEN'], ['R2R', 'R2'],
		['R3R', 'R3'], ['H8R', 'H8'], ['TNR', 'TN'],
		['Edw', 'E3'], ['lc_', 'LC'], ['H5R', 'H5'],
		['JCR', 'JC'], ['JNR', 'JN'], ['LRR', 'LR'],
		['WTR', 'WT'], ['PPR', 'PP']]

p = set(string.punctuation) - set("-'")
def word_minus_punct (word):
	nw = ""
	for letter in word:
		if letter not in p:
			nw += letter
	return nw


def remove_function_words(text):
	text = text.split()
	ret_text = ""
	fwords = set(open("/Users/jamesfisk/Desktop/thesisc/functionwords.txt", 'r').read().split())
	for word in text:
		if word in fwords:
			continue
		ret_text += " " + word
	return ret_text


"""
most basic lemmatization. remove genitive "'s", remove plural "s", lemmatize verbs.
takes nltk pos tagged list, returns word list.
NO VERB
"""
def lemmatize(pos):
	wnl = WordNetLemmatizer()
	
	ret_text = []
	for elt in pos:
		word = elt[0]
		word = word.replace(u'\xe1', 'a')
		pos = elt[1]
		#print elt[1]
		"""
		if elt[1][0] == 'V':	#verb
			word = wnl.lemmatize(elt[0], 'v')
			print elt[0], word
		"""
		if word[-2:] == "'s" and word not in ["Let's", "let's", "'s"]:	#genetive
			word = word[:-2]
			pos = 'NNS'

		if pos in ['NNS', 'NNPS']:		#plural
			word = wnl.lemmatize(word, 'n')



		ret_text.append(word)
	return ret_text


def write_pos_to_file(filename, text):
	pos = nltk.pos_tag(text.split())
	with open(filename, 'w') as outfile:
		json.dump(pos, outfile)
	print "Done"

def load_pos_from_file(filename):
	with open(filename) as data_file:
		data = json.load(data_file)
	return data

def remove_punct(text):
	clean = ""
	write = 0
	for i  in range(len(text)):
		if text[i] in p:
			#apostrophe
			if text[i] == "'":
				if text[i + 1] == "s":
					#mak'st
					if text[i + 2] == "t":
						clean += "e"
						write = 1
					#summer's
					else:
						write = 2
				#e'er
				elif text[i + 1] == "e":
					clean += "v"
				#pow'r
				else:
					clean += "e"
					write = 1
			else:
				clean += " "
				write = 1
		else:
			if write <= 0:
				clean += text[i].lower()
		write -= 1
	return clean


def build_zone_lemmas():
	z, n = get_pos_zones()
	q = get_clean_zone_corpus()
	for i in range(len(z)):
		zone = z[i]
		for k in range(len(zone)):
			play = z[i][k]
			name = n[i][k].split("p")[0]

			clean = q[i].raw(q[i].fileids()[k]).lower().split()

			lem = lemmatize(play)
			ct = 0
			for p in range(len(lem)):
				if lem[p] != clean[p]:
					print name, clean[p], lem[p]
					ct += 1
			print ct, len(clean)
			lem = " ".join(lem).encode('utf-8')
			f = open("./res/lem/" + str(i + 1) + "/" + name + "lem.txt", "w")
			f.write(lem)
			f.close()


if __name__ == '__main__':
	s = get_sonnet_list()
	pos_path = "/Users/jamesfisk/Desktop/thesisc/res/sonpos2/"
	lem_path = "/Users/jamesfisk/Desktop/thesisc/res/sonlem/"

	for i in range(len(s)):
		son = s[i].lower().split()
		pos = nltk.pos_tag(son)
		pickle.dump(pos, open(pos_path + str(i + 1) + "pos.p", "w"))

		lem = lemmatize(pos)
		for k in range(len(son)):
			if lem[k] != son[k]:
				print i + 1, son[k], lem[k]
		print "\n"

		f = open(lem_path + str(i + 1) + "lem.txt", "w")
		f.write(" ".join(lem))
		f.close()


















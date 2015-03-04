
from nltk.stem import WordNetLemmatizer
from corpus import *
import string
import nltk
import json


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
"""
def lemmatize(pos):
	wnl = WordNetLemmatizer()
	
	ret_text = []
	for elt in pos:
		word = elt[0]
		#print elt[1]
		if elt[1][0] == 'V':	#verb
			word = wnl.lemmatize(elt[0], 'v')
			print elt[0], word
		elif elt[1] in ['NNS', 'NNPS']:		#plural
			word = wnl.lemmatize(elt[0], 'n')

		if word[-2:] == "'s" and word not in ["Let's", "let's", "'s"]:	#genetive
			word = word[:-2]

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


if __name__ == '__main__':
	s = get_nopunct_sonnet_corpus()
	write_pos_to_file("sonpos.json", s.raw())




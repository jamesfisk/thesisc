from nltk.stem import WordNetLemmatizer
import string
import nltk


p = set(string.punctuation)

def remove_function_words(text):
	text = text.split()
	ret_text = ""
	fwords = set(open("/Users/jamesfisk/Desktop/thesisc/functionwords.txt", 'r').read().split())
	for word in text:
		if word in fwords:
			continue
		ret_text += " " + word
	return ret_text

def lemmatize(text):
	wnl = WordNetLemmatizer()
	pos = nltk.pos_tag(text.split())
	ret_text = ""
	for elt in pos:
		if elt[1][0] == 'V':
			word = wnl.lemmatize(elt[0], 'v')
		else:
			word = wnl.lemmatize(elt[0])
		ret_text += " " + word
	return ret_text




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
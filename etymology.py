from oed import *
from lxml import html
from parse import *
from corpus import *
import requests
import io
import sys



oed_root = "http://www.oed.com/view"
lang = {"german" : 0,
		"latin" : 0,
		"greek" : 0,
		"norman" : 0}

def fetch_full_entry(identifier):
	url = oed_root + identifier
	page = requests.get(url)
	tree = html.fromstring(page.text)

	return tree
def get_tree_etymology(tree):
	buyers = tree.xpath('//div[@class="etymology preEntry"]/text()')
	return buyers

def get_word_etymology(query):
	print query
	try:
		res = search(query)
		choose = 1
		if (int(res[0]) > 1):
			for i in range(int(res[0])):
				print i + 1,
				print res[1][i]
			choose = eval(raw_input("Choose definition: "))
		tree = fetch_full_entry(res[1][choose - 1][1])
		print "etymology", query
		return get_tree_etymology(tree)
	except KeyboardInterrupt:
		raise
	except:
		print "Unexpected error: ", sys.exc_info()[0]

def update_freq(freq, entry):
	entry = remove_punct(entry)
	entry = entry.split()
	for elt in entry:
		if elt in freq:
			freq[elt] += 1
			break

	return freq


def sonnet_etymology (text):
	text = remove_punct(text)
	text = lemmatize(text)
	text = remove_function_words(text)
	text = text.split()
	freq = lang.copy()
	for word in text:
		try:
			entry =  " ".join(get_word_etymology(word))
		except:
			continue
		freq = update_freq(freq, entry)
		print entry + "\n" + str(freq) + "\n"
	return freq


if __name__ == '__main__':
	"""
	while True:
		word = raw_input("Enter a word: ")
		if word.strip() == '0':
			break
		print word
		print " ".join(get_word_etymology(word))
	"""
	sn = [40, 80, 120, 150]
	sonnets = get_sonnet_corpus()
	t_freq = []
	for i in range(len(sn)):
		print "\n\n\n\n\n\n SONNNET #" + str(sn[i]) + '\n\n\n'
		s = sonnets.raw(str(sn[i]) + '.txt')
		f = sonnet_etymology(s)
		t_freq.append((sn[i], f))
	print t_freq



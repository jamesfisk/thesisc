from corpus import *
from singleletter import *
from digrams import *
from word import *
from style import *
from ngram import *
from son_metrics import *
from rhyme import *
from citation import *
from sarrazin import *

from sklearn.preprocessing import scale



import pickle
import numpy as np


class DataPoint:
	def __init__(self, name):
		self.name = name
		self.letter_freq = []	#28 letters
		self.digrams = []		#96 common digrams
		self.word_freq = []		#96 common words
		self.word_len = []		#1-18 long words
		self.ngrams = []		#4 periods ngrams shared with ONLY 4/5 ngrams 

		self.mle = 0			#num mle
		self.fe = 0				#num fe
		self.ol = 0				#num ol
		self.le = 0				#num le
		self.we = 0				#num we
		self.col = 0			#num col
		self.arch = 0			#num arch


		self.rhyme = []			#4 periods num shared rhyme
		self.cit = []			#4 periods num citations shared

		self.sarr = []			#4 periods num rare words shared
		self.dist = []			#4 periods num dwords shared
		

	def metrics(self):
		return [self.mle, self.fe, self.ol, self.le, self.we, self.col, self.arch]
	
	def np_universal(self):
		return np.array(self.letter_freq + 
						  self.digrams + 
						  self.word_freq)

	def np_metrical(self):
		return np.array(self.metrics())

	def np_shakes(self):
		return np.array(self.ngrams + 
						self.rhyme +
						self.cit + 
						self.sarr + 
						self.dist)

	def np_metshakes(self):
		return np.concatenate([self.np_metrical(), self.np_shakes()])

	def np_all(self):
		return np.concatenate([self.np_universal(), self.np_metrical(), self.np_shakes()])




	def pickle_point(self, path):
		pickle.dump(self, open(path + self.name + ".p", "w"))




	def build_point(self, son):
		txt = open("./res/son/" + str(son) + ".txt", "r").read()
		self.letter_freq = get_letter_freq(txt, None)
		self.digrams = find_digrams(txt, top_96_corpus_digrams_keys())
		self.word_freq = find_words(txt, top_96_corpus_words_keys())
		self.word_len = word_length(txt, None)

		self.ngrams = self.bin_ngrams(son)

		self.set_metrics(son)

		self.rhyme = period_rhymes_by_sonnet()[son - 1]
		self.cit = period_citations_by_sonnet()[son - 1]

		self.sarr = period_sarr_by_sonnet()[son - 1]
		self.dist = period_dwords_by_sonnet()[son - 1]

	def build_not_sonnet_point(self, txt):
		self.letter_freq = get_letter_freq(txt, None)
		self.digrams = find_digrams(txt, top_96_corpus_digrams_keys())
		self.word_freq = find_words(txt, top_96_corpus_words_keys())
		self.word_len = word_length(txt, None)

		self.sarr = sarrazin_in_text(txt)



	def set_metrics(self, son):
		m = get_son_metrics(son)
		self.mle = m[8]
		self.fe = m[2]
		self.ol = m[0]
		self.le = m[6]
		self.we = m[7]
		self.col = m[4]
		self.arch = m[5]


	def bin_ngrams(self, son):
		l = get_son_ngram_thing()
		s = l[son - 1]
		bins = []
		for period in PERIODS:
			count = 0
			for play in period:
				count += s.count(play)
			bins.append(count)
		return bins

	def print_info (self):
		print "Sonnet", self.name
		print
		print "Letter Frequency"
		for i in range(11):
			if i % 5 == 0:
				print
			if i == 26:
				print "'",
			elif i == 27:
				print "-",
			else:
				print chr(i + 97), 
			print "%.5f" % self.letter_freq[i],

		print "..."
		digram = top_96_corpus_digrams_keys()
		print "96 Most Frquent Digrams"
		for i in range(11):
			if i % 5 == 0:
				print
			print digram[i],
			print "%.5f" % self.digrams[i],

		print "..."
		words = top_96_corpus_words_keys()
		print "96 Most Frquent Words\n"
		i = 0
		for row in zip(words, self.word_freq):
			i += 1
			if i % 5 == 0:
				print
			print "%-9s %.5f" % row,
			if i == 11:
				break
		print "...\n"
		print "Ngrams by Period"
		print self.ngrams
		print "\n"
		print "Metrics\n"

		for row in zip(["ML", "FE", "OL", "LE", "WE", "CO", "AR"], [float(x) for x in self.metrics()]):
			print "%s %d" % row,
		print 
		print "Shared Rhyme by Period"
		print self.rhyme
		print "Shared Citation by Period"
		print self.cit
		print "Shared Sarrazin Links by Period"
		print self.sarr
		print "Shared Distinctive Words by Period"
		print self.dist







def build_raw_dps():
	ds = []
	for i in range(1, 155):
		print i
		son = DataPoint(str(i))
		son.build_point(i)
		ds.append(son)
	pickle.dump(ds, open("./raw_sondatapoints.p", "w"))

def scale_dps():
	dps = pickle.load(open("./raw_sondatapoints.p", "r"))

	ndps = []
	for i in range(1, 155):
		son = DataPoint(str(i))
		ndps.append(son)

	
	for k in range(len(dps[0].letter_freq)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].letter_freq[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].letter_freq.append(att[i])


	for k in range(len(dps[0].digrams)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].digrams[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].digrams.append(att[i])

	for k in range(len(dps[0].word_freq)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].word_freq[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].word_freq.append(att[i])

	for k in range(len(dps[0].word_len)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].word_len[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].word_len.append(att[i])

	for k in range(len(dps[0].ngrams)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].ngrams[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].ngrams.append(att[i])

	for k in range(len(dps[0].rhyme)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].rhyme[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].rhyme.append(att[i])

	for k in range(len(dps[0].cit)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].cit[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].cit.append(att[i])

	for k in range(len(dps[0].sarr)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].sarr[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].sarr.append(att[i])

	for k in range(len(dps[0].dist)):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].dist[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].dist.append(att[i])

	for k in range(len(dps[0].metrics())):
		att = []
		for i in range(len(dps)):
			att.append(dps[i].word_freq[k])
		att = list(scale([float(x) for x in att]))
		for i in range(len(ndps)):
			ndps[i].word_freq.append(att[i])

	att = []
	for i in range(len(dps)):
		att.append(dps[i].mle)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].mle = att[i]

	att = []
	for i in range(len(dps)):
		att.append(dps[i].fe)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].fe = att[i]

	att = []
	for i in range(len(dps)):
		att.append(dps[i].ol)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].ol = att[i]

	att = []
	for i in range(len(dps)):
		att.append(dps[i].le)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].le = att[i]

	att = []
	for i in range(len(dps)):
		att.append(dps[i].we)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].we = att[i]

	att = []
	for i in range(len(dps)):
		att.append(dps[i].col)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].col = att[i]

	att = []
	for i in range(len(dps)):
		att.append(dps[i].arch)
	att = list(scale([float(x) for x in att]))
	for i in range(len(ndps)):
		ndps[i].arch = att[i]

	pickle.dump(ndps, open("./scaled_data_points.p", "w"))
	print "\n\n\n\n\n\n\n"
	ndps[1].print_info()
	dps[1].print_info()
	



	return ndps

def get_dps():
	return pickle.load(open("raw_sondatapoints.p", "r"))
def get_ndps():
	return pickle.load(open("scaled_data_points.p", "r"))

"""
'universal', 'metrical', 'shakes', 'metshakes' or 'all'
"""
def get_npdps(data_type):
	ndps = get_ndps()
	dps = get_dps()
	npdps = []
	if data_type == 'universal':
		for i in range(len(ndps)):
			npdps.append(ndps[i].np_universal())
	elif data_type == 'metrical':
		for i in range(len(ndps)):
			npdps.append(ndps[i].np_metrical())
	elif data_type == 'shakes':
		for i in range(len(ndps)):
			npdps.append(ndps[i].np_shakes())	
	elif data_type == 'sarr':
		for i in range(len(ndps)):
			npdps.append(ndps[i].sarr)
	elif data_type == 'dist':
		for i in range(len(ndps)):
			npdps.append(ndps[i].dist)
	elif data_type == 'ngrams':
		for i in range(len(ndps)):
			npdps.append(ndps[i].ngrams)
	elif data_type == 'metshakes':
		for i in range(len(ndps)):
			npdps.append(ndps[i].np_metshakes())
	elif data_type == 'all':
		for i in range(len(ndps)):
			npdps.append(ndps[i].np_all())
	else:
		print "Bad data type"
		exit()
	return np.array(npdps)



if __name__ == "__main__":
	dps = get_dps()
	s = 0
	for i in range(len(dps)):
		s += sum(dps[i].sarr)
		print dps[i].sarr
	print s
	






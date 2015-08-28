from __future__ import division
from datapoint import *
from neural import *
from corpus import *
from colloq import *

import pickle

#uses lemma corpus
def divide_lemma_corpus():
	z = get_lemma_zones()
	ret = [[], [], [], []]
	for i in range(len(z)):
		zone_text = z[i].raw().split()
		ct = 0
		num = 0
		txt = ""
		while ct < len(zone_text):
			txt += zone_text[ct] + " "
			if ct %4377== 0 and ct != 0:
				ret[i].append(txt)
				txt = ""
				num += 1
			ct += 1
	

	pickle.dump(ret, open("./divided_lemma_corpus.p", "w"))
	return ret

#uses redacted corpus. avoids some errors with clean text
def divide_redacted_corpus():
	z = get_redacted_zone_corpus()
	ret = [[], [], [], []]
	for i in range(len(z)):
		zone_text = z[i].raw().lower().split()
		ct = 0
		num = 0
		txt = ""
		while ct < len(zone_text):
			txt += zone_text[ct] + " "
			if ct %4377== 0 and ct != 0:
				ret[i].append(txt)
				txt = ""
				num += 1
			ct += 1
	

	pickle.dump(ret, open("./divided_redacted_corpus.p", "w"))
	return ret

def get_hieatt_zones():
	s = get_sonnet_list()
	ret = ["", "", "", ""]
	p = 0
	for i in range(1, 155):
		ret[p] += s[i - 1] + " "
		if i in [60, 103, 126]:
			p += 1
	return ret

def get_hieatt_zones_lemmas():
	s = get_sonnet_lemma_list()
	ret = ["", "", "", ""]
	p = 0
	for i in range(1, 155):
		ret[p] += s[i - 1] + " "
		if i in [60, 103, 126]:
			p += 1
	return ret

def run(indata, fnn):
         for i in range(len(indata)):
                 e = fnn.activate(indata[i])
                 print "zone", str(i + 1),e[0], e[1]
         print

def get_sarr_clusters():
	p = [3, 3, 0, 3, 0, 3, 1, 3, 2, 1, 3, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 1, 3, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 3, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 3, 0, 3, 2, 3, 1, 3, 3, 0, 0, 3, 3, 0, 3, 3, 0, 3, 1, 0, 3, 3, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 3, 1, 0, 3, 0, 3, 0, 0, 0, 1, 1, 2, 0, 1, 2, 0, 3, 3, 0, 3, 0, 2, 0, 1, 3, 3, 3, 2, 1, 2, 2, 3, 0, 1, 3, 0, 0, 2, 2, 2, 2, 0, 1, 0, 3, 0, 3, 3, 3, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 0, 3, 0, 0]

	s = get_sonnet_list()
	c = ["", "", "", ""]
	for i in range(len(s)):
		c[p[i]] += s[i] + " "
	return c



def corpus_dword_datapoints():
	z = get_lemma_zones()
	X = []
	y = []
	for i in range(len(z)):
		zone_text = z[i].raw().split()
		ct = 0
		num = 0
		txt = ""
		while ct < len(zone_text):
			txt += zone_text[ct] + " "
			if ct % 4377== 0 and ct != 0:
				
				X.append(dwords_in_text(txt))
				y.append(i)
				print num
				txt = ""
				num += 1


			ct += 1
	return X, y

def make_corpus_datapoints():
	z = get_lemma_zones()
	X = []
	y = []
	for i in range(len(z)):
		zone_text = z[i].raw().split()
		ct = 0
		num = 0
		txt = ""
		while ct < len(zone_text):
			txt += zone_text[ct] + " "
			if ct %4377== 0 and ct != 0:
				data = DataPoint(str(i) + "." + str(num))
				data.build_not_sonnet_point(txt)
				X.append(data.sarr)
				y.append(i)
				print X[-1], y[-1]
				txt = ""
				num += 1


			ct += 1
	return X, y

def make_sonnet_datapoints():
	s = get_lemma_sonnets()	

	for fid in s.fileids():
		text = s.raw(fid)
		data = DataPoint(fid)
		data.build_not_sonnet_point(txt)
		X.append(data.sarr)
		print X[-1]
	return X


def build_col_dataset():
	txt = divide_redacted_corpus()
	X = []
	y = []
	for i in range(len(txt)):
		for k in range(len(txt[i])):
			X.append(generate_d_stats(txt[i][k]))
			y.append(i)

	return [X, y]

def train_with_data(X, y):
	trainer, fnn, trndata, tstdata = make_nn(np.array(X), np.array(y))
	for k in range(300):
		print "Running on colloq"
		run_epoch(trainer, trndata, tstdata)
	return fnn


def run_classification():
	[X, y] = pickle.load(open("./sarr_alldata.p", "r"))
	for i in range(len(X)):
		print X[i], y[i]

	trainer, fnn, trndata, tstdata = make_nn(np.array(X), np.array(y))
	for k in range(200):
		print "Running on sarrazin holdout"
		run_epoch(trainer, trndata, tstdata)

	ht = get_hieatt_zones()
	zt = get_sarr_clusters()
	h = []
	z = []
	for i in range(len(ht)):
		h.append(sarrazin_in_text_holdout(ht[i], 'aaa'))
		z.append(sarrazin_in_text_holdout(zt[i], 'bbb'))
	#h = make_dataset(h)
	#z = make_dataset(z)

	print fnn.activate(np.array(h[0]))

	print "Test Hieatt"
	print "1-60", fnn.activate(np.array(h[0]))
	print "61-103", fnn.activate(np.array(h[1]))
	print "104-126", fnn.activate(np.array(h[2]))
	print "127-154", fnn.activate(np.array(h[3]))

	print"\n\n"

	print "Test Clusters"
	for k in range(4):
		print "Cluster", k+1, fnn.activate(np.array(z[k]))

	print "Test LLL Sonnets"
	ltxt = open("./lll_sonnets.txt", "r").read()
	lrz = sarrazin_in_text_holdout(ltxt, "lll") 
	print fnn.activate(np.array(lrz))

if __name__ == '__main__':
	p = pickle.load(open("fuckin.p", "r"))
	sc = pickle.load(open("sc.p", "r"))
	fnn = train_with_data(p[0], p[1])
	run(sc, fnn)
	"""
		p = [3, 3, 0, 3, 0, 3, 1, 3, 2, 1, 3, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 1, 3, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 3, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 3, 0, 3, 2, 3, 1, 3, 3, 0, 0, 3, 3, 0, 3, 3, 0, 3, 1, 0, 3, 3, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 3, 1, 0, 3, 0, 3, 0, 0, 0, 1, 1, 2, 0, 1, 2, 0, 3, 3, 0, 3, 0, 2, 0, 1, 3, 3, 3, 2, 1, 2, 2, 3, 0, 1, 3, 0, 0, 2, 2, 2, 2, 0, 1, 0, 3, 0, 3, 3, 3, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 0, 3, 0, 0]
		for k in range(4):
			print "Cluster", k+1
			for n in range(len(p)):
				if p[n] == k:
					print n+1,
			print
	"""









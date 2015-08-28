
from __future__ import division
from collections import defaultdict
from corpus import *
from numpy.random import normal
import numpy as np



"""
Title	OL	FE	Colloq	Arch	LE	WE	MLE
"""

def get_corpus_metrics():

	f = open("./spreadsheets/corpus_metrics_comp.csv", "r")
	line = "crap"
	d = defaultdict()
	while line:
		line = f.readline()
		pline = line.split(",")
		d[pline[0]] = [int(x) for x in pline[1:]]
		#print pline[0], [int(x) for x in pline[1:]]


	f.close()
	return d

def scale_metrics(d):
	q = get_clean_corpus()
	p = defaultdict()
	for key in d:
		fid = ""
		for elt in q.fileids():
			if elt.startswith(key):
				fid = elt
		if fid == "":
			print key, "faiure"
			exit()
		txt = q.raw(fid)
		l = len(txt.split())
		p[key] = [x/l for x in d[key]]
		#print key, p[key]
	return p


def compute_period_info():
	d = scale_metrics(get_corpus_metrics())

	r = [[], [], [], []]
	for k in range(7):
		for i in range(len(PERIODS)):
			pop = []
			for play in PERIODS[i]:
				try:
					pop.append(d[play][k])
				except (KeyError):
					pass
			mean = np.mean(pop)
			std = np.std(pop)
			r[i].append((mean, std))
	print r
	return r

def run_metrical_nn():
	r = compute_period_info()
	for k in range(60):
		for klass in range(4):
			datap = normal(r[klass])


if __name__ == '__main__':
	compute_period_info()




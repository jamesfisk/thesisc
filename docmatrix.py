from __future__ import division

from sarrazin import *
from cluster import *
from neural_cluster import *

from numpy import matrix
from scipy import linalg, mat, dot
import numpy as np
import time



#parse before input
def make_doc_matrix(docs):
	words = sorted(list(pickle.load(open("all_sarr_words.p")))) #rows
	m = []
	for word in words:
		col = []
		for doc in docs:
			doc = doc.split()
			col.append(doc.count(word))

		m.append(col)
	return m


def get_docs():
	return pickle.load(open("divided_lemma_corpus.p", "r"))

def make_corpus_sarr_docmatrix(): #WITH HIEATT ZONES
	docs = get_docs()
	zones = get_hieatt_zones_lemmas()
	docsj = []
	for elt in docs: #go through periods
			docsj += elt
	m = make_doc_matrix(docsj + zones)
	return m

#normalize matrix
def matB(m):
	rows, cols = len(m), len(m[0])
	for col in range(cols):
		length = 0

	        length = sum([m[row][col]**2 for row in range(rows)]) ** 0.5
	        for row in range(rows):
	            m[row][col] /= length
	return m


def get_svd(a):
	for k in range(len(a)):
		print " ".join([str(x) for x in a[k]])

	print
	b = matB(a)
	for i in range(len(b)):
		print " ".join([str(x) for x in b[i]])

	print 

	c = np.dot(matrix.transpose(np.array(b)),np.array(b))
	for i in range(len(c)):
		print " ".join([str(x) for x in c[i]])

	print 

	U, s, V = np.linalg.svd(b)
	return U, s, V

def two_pc_vectors(a):
	o = []
	t = []

	for k in range(len(a)):
		for j in range(2):
			if j == 0:
				o.append(a[k][j])
			else:
				t.append(a[k][j])

	return o, t

def cos_sim(a, b):
	return dot(a, b)/linalg.norm(a)/linalg.norm(b)


if __name__ == '__main__':

	start_time = time.time()

	get_all_sarr_words()
	a = pickle.load(open("sarr_docmatrix_corhieatt.p", "r"))#make_corpus_sarr_docmatrix()

	U, s, V = get_svd(a)
	pickle.dump([U, s, V], open("sarr_corpus_svd.p", "w"))

	#[U, s, V] = pickle.load(open("sarr_corpus_svd.p", "r"))
	ol, tl = two_pc_vectors(U)

	b = matB(a)
	b = matrix.transpose(np.array(b))


	for i in range(len(b)):

		x = cos_sim(ol, b[i,:])
		y = cos_sim(tl, b[i,:])
		print x, y			
		if i + 1 in BREAKS:
			print

	
	"""
	docmatrix = make_corpus_sarr_docmatrix()
	pickle.dump(docmatrix, open("sarr_docmatrix_corhieatt.p", "w"))

	docmatrix = pickle.load(open("sarr_docmatrix_corhieatt.p", "r"))
	do_PCA(matrix.transpose(np.array(docmatrix)), "sarr234PCA")
		"""

	print("--- %s seconds ---" % (time.time() - start_time))







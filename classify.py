from centroid import *
from datetime import datetime
from operator import mul
from singleletter import *
from digrams import *
from word import *
import math


def gaussian(mu, sigma, x):
	return (1/math.sqrt(2*math.pi*sigma))*math.e**(-(x-mu)**2/(2*sigma))



def classify (features, centroid, prior):
	scores = []
	for i in range(len(features)):

		if centroid.sv[i] == 0:
			print "0"
			continue
		score = gaussian(centroid.mean[i], centroid.sv[i], features[i])
		

		
		scores.append(score)
	reduced = reduce(mul, scores) * prior
	return reduced

def run_all_tests ():







if __name__ == "__main__":
	"""
	dummy = Centroid("abc", gaussian, 0)
	dummy.make_dummy_centroid()
	test = [6, 130, 8]
	print classify(test, dummy, .5)


	"""
	startTime = datetime.now()

	correct = [0, 0, 0, 0]
	for i in range(10):
		results = []
		validation = get_random_validation_corpus()
		test = get_test_corpus_minus_validation(validation)
		centroids = []

		for cp in test:
			words = top_96_words_keys(cp.raw())
			centroids.append(Centroid(cp, find_words, words))

		for c in centroids:
			c.make_centroid()

		for j in range(len(validation)):#cp in validation:
			fileid = validation[j].fileids()[0]
			print fileid, "from zone ", j + 1
			scores = []
			
			for cn in centroids:
				features = find_words(validation[j].raw(fileids=[fileid]), top_96_words_keys(cn.corpus.raw()))
				scores.append(classify(features, cn, .25))
			winner = scores.index(max(scores))
			if winner == j:
				correct[j] += 1
			print scores, scores.index(max(scores)) + 1
			#print "correct", correct
	print correct

	print(datetime.now()-startTime)


		




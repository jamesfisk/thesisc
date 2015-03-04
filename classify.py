from centroid import *
from datetime import datetime
from operator import mul
from singleletter import *
from digrams import *
from word import *
from style import *
import math


def gaussian(mu, sigma, x):
	return (1/math.sqrt(2*math.pi*sigma))*math.e**(-(x-mu)**2/(2*sigma))



def classify (features, centroid, prior):
	scores = []
	for i in range(len(features)):
		#centroid.sv[i] += 1.338388818711138e-12
		
		if centroid.sv[i] == 0:
			print "EHY!!!!"
			score = gaussian(centroid.mean[i], 1.338388818711138e-5, features[i])	#pseudocount. if we let this equal zero, will wipe out other data
		
		else:
			score = gaussian(centroid.mean[i], centroid.sv[i], features[i])

		#score = gaussian(centroid.mean[i], centroid.sv[i], features[i])
		
		scores.append(score)
	reduced = reduce(mul, scores) * prior
	return reduced

def run_cross_validation (func, aux):
	startTime = datetime.now()

	correct = [0, 0, 0, 0]
	for i in range(1000):
		results = []
		validation = get_clean_random_validation_corpus()
		#print [x.fileids() for x in validation]
		test = get_clean_test_corpus_minus_validation(validation)
		#print [x.fileids() for x in test]
		centroids = []

		for cp in test:
			centroids.append(Centroid(cp, func, aux))

		for c in centroids:
			c.make_centroid()
			"""
			print
			print "sv ", c.sv
			print "mean ", c.mean
		"""
		for j in range(len(validation)):#cp in validation:
			fileid = validation[j].fileids()[0]
			print fileid, "from zone ", j + 1
			scores = []
			
			for cn in centroids:
				features = func(validation[j].raw(), aux)
				scores.append(classify(features, cn, .25))
			winner = scores.index(max(scores))
			if winner == j:
				correct[j] += 1
			print scores, scores.index(max(scores)) + 1
		print "correct", correct, "out of", (i + 1)
		print
	print correct

	print(datetime.now()-startTime)



def run_all_tests ():
	return







if __name__ == "__main__":
	"""
	dummy = Centroid("abc", gaussian, 0)
	dummy.make_dummy_centroid()
	test = [6, 130, 8]
	print classify(test, dummy, .5)


	"""

	run_cross_validation(word_syllable, None)

		




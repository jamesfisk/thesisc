from __future__ import division
from corpus import *
from singleletter import *



class Centroid:

	def __init__(self, corpus, func, aux):
		self.corpus = corpus
		self.mean = []
		self.sv = []
		self.samples = []
		self.func = lambda a, b: func(a, b)
		self.aux = aux
	
	def make_centroid(self):
		self.populate_samples()
		self.compute_mean()
		self.compute_sv()

	def make_dummy_centroid(self):
		self.samples = [[6, 180, 12],
			   [5.92, 190, 11],
			   [5.58, 170, 12],
			   [5.92, 165, 10]]
		self.compute_mean()
		self.compute_sv()


	def populate_samples(self):
		files = self.corpus.fileids()
		num_samples = len(files)
		for i in range(num_samples):
			self.samples.append(self.func(self.corpus.raw(fileids=[files[i]]), self.aux))


	def compute_mean(self):
		self.mean = [0 for x in range(len(self.samples[0]))]
		for k in range(len(self.samples[0])):
			for j in range(len(self.samples)):
				self.mean[k] += self.samples[j][k]
		self.mean = [x / len(self.samples) for x in self.mean]

	def compute_sv (self):
		self.sv = [0 for x in range(len(self.mean))]
		for i in range(len(self.samples[0])):	#features
			s = 0
			for j in range(len(self.samples)):	#samples
				s += (self.samples[j][i] - self.mean[i]) ** 2
			self.sv[i] = s / (len(self.samples) - 1)
		






if __name__ == "__main__":
	test = get_test_corpus()
	zones = get_zone_corpus()
	cc1 = Centroid(test[0], get_letter_freq)
	print "test"
	"""
	cc1.samples = [[6, 180, 12],
				   [5.92, 190, 11],
				   [5.58, 170, 12],
				   [5.92, 165, 10]]
				   """
	cc1.populate_samples()
	cc1.compute_mean()
	cc1.compute_sv()
	print "mean", cc1.mean, "\nsv", cc1.sv
	
	

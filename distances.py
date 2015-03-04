from __future__ import division


def get_euclidean_distance(data1, data2):
	if len(data1) != len(data2):
		print "unequal data sets"
		return
	d = 0

	for i in range(len(data1)):
		d += ((data1[i] - data2[i]) ** 2)

	d = d ** .5
	return d

def get_cos_similarity(x, y):
	if len(x) != len(y):
		print "unequal data sets"
		return
	lenx, leny, dot = 0, 0, 0
	for i in range(len(x)):
		xi = x[i]
		yi = y[i]
		lenx += xi * xi
		leny += yi * yi
		dot += xi * yi
	lenx = lenx ** .5
	leny = leny ** .5
	return dot / (lenx * leny)

def print_zone_distances(zones):
	print "EuclideanDistance"
	for i in range(len(zones)):
		#print "Zone",
		for j in range(len(zones)):
			print get_euclidean_distance(zones[i], zones[j]),
		print

	print "CosineSimilarity"
	for i in range(len(zones)):
		#print "Zone", 
		for j in range(len(zones)):
			print get_cos_similarity(zones[i], zones[j]),
		print


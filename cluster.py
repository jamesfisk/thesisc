from datapoint import *

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.decomposition import PCA

COLORS = [ '\033[92m', '\033[91m', '\033[95m', '\033[94m']
ENDC = '\033[0m'
BREAKS = [53, 98, 136, 181]

def hieatt_zones():
	p = 0
	for i in range(1, 155):
		print COLORS[p] +  str(i),
		if i in [60, 103, 126]:
			p += 1
	print ENDC




def do_PCA(data, fid):
	pca = PCA(n_components=2)
	reduced_data = pca.fit_transform(data)

	f = open("./spreadsheets/" + fid + ".csv", "w")
	i = 1
	for item in reduced_data:
		f.write(str(item[0])+ "," + str(item[1]) + "\n")
		if i in BREAKS:
			f.write("\n")
		i += 1
	f.close()

	return reduced_data

def cluster_on_attribute(data):
	model = KMeans(init='k-means++', n_clusters=4, n_init=100)
	print model.fit(data)
	labels = model.labels_
	print labels
	print "Silhouette", metrics.silhouette_score(data, labels, metric='euclidean')
	print "Inertia", model.inertia_
	return labels

def run_clusters():
	tests = ['universal', 'metrical', 'shakes', 'sarr', 'dist', 'metshakes', 'all', ]

	for i in range(1, 3):
		num_clusters = 2 * i
		for k in range(len(tests)):
			print "Test", tests[k], "with", num_clusters, "clusters"
			
			model = KMeans(init='k-means++', n_clusters=num_clusters, n_init=100)
			data = do_PCA(get_npdps(tests[k]), "null")
			print model.fit(data)
			labels = model.labels_
			print labels
			print "Silhouette", metrics.silhouette_score(data, labels, metric='euclidean')
			print "Inertia", model.inertia_
			print
			
def print_color(labels):
			for j in range(len(labels)):
				print COLORS[labels[j]] + str(j + 1) + ENDC,
			print ENDC

def colored_clusters():
	tests = ['universal', 'metrical', 'shakes', 'sarr', 'dist', 'metshakes', 'all', ]

	for i in range(1, 3):
		num_clusters = 2 * i
		for k in range(len(tests)):
			print "Test", tests[k], "with", num_clusters, "clusters"
			
			model = KMeans(init='k-means++', n_clusters=num_clusters, n_init=100)
			data = do_PCA(get_npdps(tests[k]), "null")
			model.fit(data)
			labels = model.labels_
			print_color(labels)
			print "Silhouette %.4f" % metrics.silhouette_score(data, labels, metric='euclidean')
			print "Inertia %.4f" % model.inertia_, "\n\n"
			
if __name__ == '__main__':
	colored_clusters()

	"""
	data_red = []
	data = []
	ndps = get_ndps()
	dps = get_dps()
	for i in range(len(ndps)):
		data_red.append(np.array(ndps[i].letter_freq))
		data.append(np.array(dps[i].letter_freq))
	do_PCA(np.array(data_red), "letter_freq_reduced")
	do_PCA(np.array(data), "letter_freq_noscale")


	data = []
	pca1 = do_PCA(get_npdps('universal'), 'null')
	pca2 = do_PCA(get_npdps('metrical'), 'null')
	pca3 = do_PCA(get_npdps('shakes'), 'null')
	for i in range(154):
		data.append(np.concatenate([pca1[i], pca2[i], pca3[i]]))
	cluster_on_attribute(np.array(data))
	#data = np.concatenate([do_PCA(get_npdps('universal'), 'null'), do_PCA(get_npdps('metrical'), 'null'), do_PCA(get_npdps('shakes'), 'null')])
	#cluster_on_attribute(data)
	******************************************************************

	dps = get_dps()
	npdps = []
	for i in range(len(dps)):
		npdps.append(dps[i].sarr)
	red_data = do_PCA(np.array(npdps), "sarr_reduced_noscale")

	labels = cluster_on_attribute(red_data)
	clusters = [[], [], [], []]
	for i in range(len(labels)):
		idx = int(labels[i])
		clusters[idx].append(red_data[i])

	for c in clusters:
		for item in c:
			print item[0], item[1]
		print 
		print (50 * '*')
		print
		"""






	

	

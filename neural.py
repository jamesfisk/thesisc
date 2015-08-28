from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
from sklearn import datasets
import numpy as np


def split_data(alldata, x, y):

	tstdata_temp, trndata_temp = alldata.splitWithProportion(0.25)

	tstdata = ClassificationDataSet(x, 1, nb_classes=y)
	for n in xrange(0, tstdata_temp.getLength()):
	    tstdata.addSample( tstdata_temp.getSample(n)[0], tstdata_temp.getSample(n)[1] )

	trndata = ClassificationDataSet(x, 1, nb_classes=y)
	for n in xrange(0, trndata_temp.getLength()):
	    trndata.addSample( trndata_temp.getSample(n)[0], trndata_temp.getSample(n)[1] )

	trndata._convertToOneOfMany( )
	tstdata._convertToOneOfMany( )

	return trndata, tstdata

def make_dataset(indata):
	alldata = ClassificationDataSet(len(indata[0]), 1, 4)
	for n in xrange(len(indata)):
		alldata.addSample(np.array(indata[n]))
	return alldata

def run_epoch(trainer, trndata, tstdata):
    trainer.trainEpochs( 1 )
    trnresult = percentError( trainer.testOnClassData(),trndata['class'] )
    tstresult = percentError( trainer.testOnClassData(dataset=tstdata ), tstdata['class'] )

    print "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult, \
          "  test error: %5.2f%%" % tstresult
    print

def get_olive():
	olive = datasets.fetch_olivetti_faces()
	return olive.data, olive.target

def make_nn(indata, klass):
	num_classes = len(np.unique(klass))
	num_attributes = len(indata[0])
	alldata = ClassificationDataSet(num_attributes, 1, nb_classes=num_classes)

	for n in xrange(len(indata)):
		alldata.addSample(np.array(indata[n]), [klass[n]])

	trndata, tstdata = split_data(alldata, num_attributes, num_classes)

	fnn = buildNetwork( trndata.indim, 200, trndata.outdim, outclass=SoftmaxLayer )

	trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

	return trainer, fnn, trndata, tstdata
def get_dummy_data():
	means = [(-1,0),(2,4),(3,1)]
	cov = [diag([1,1]), diag([0.5,1.2]), diag([1.5,0.7])]
	X = []
	y = []

	for n in xrange(400):
	      for klass in range(3):
	                input = multivariate_normal(means[klass],cov[klass])
	                X.append(input)
	                y.append(klass)
	return X, y



def build_sample_nn():
	means = [(-1,0),(2,4),(3,1)]
	cov = [diag([1,1]), diag([0.5,1.2]), diag([1.5,0.7])]
	alldata = ClassificationDataSet(2, 1, nb_classes=3)
	for n in xrange(400):
	      for klass in range(3):
	                input = multivariate_normal(means[klass],cov[klass])
	                alldata.addSample(input, [klass])

	tstdata_temp, trndata_temp = alldata.splitWithProportion(0.25)

	tstdata = ClassificationDataSet(2, 1, nb_classes=3)
	for n in xrange(0, tstdata_temp.getLength()):
	    tstdata.addSample( tstdata_temp.getSample(n)[0], tstdata_temp.getSample(n)[1] )

	trndata = ClassificationDataSet(2, 1, nb_classes=3)
	for n in xrange(0, trndata_temp.getLength()):
	    trndata.addSample( trndata_temp.getSample(n)[0], trndata_temp.getSample(n)[1] )

	trndata._convertToOneOfMany( )
	tstdata._convertToOneOfMany( )

	fnn = buildNetwork( trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer )


	trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

	return trainer, fnn, tstdata

if __name__ == '__main__':
	X, y = get_dummy_data()
	trainer, fnn, trndata, tstdata = make_nn(X, y)
	for k in range(100):
		run_epoch(trainer, trndata, tstdata)
		print






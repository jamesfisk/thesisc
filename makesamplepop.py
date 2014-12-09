from corpus import *
import os
import math


def make_sample_pop(text, folder):
	path =  "/Users/jamesfisk/Desktop/thesisc/" + folder + "/"

	text = open(text, 'r').read().split()
	for j in range(int(math.ceil(len(text) / 4378))):
		outfile = open(path + "/" + str(j + 1) + ".txt", 'w')
		for n in range(4378):
			outfile.write(text[(j * 4378) + n] + " ")
		outfile.close()






	
	  


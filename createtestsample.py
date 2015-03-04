import io
import os
import random


def main():
	path =  "/Users/jamesfisk/Desktop/thesisc/cleanzones/"
	tpath = "/Users/jamesfisk/Desktop/thesisc/cleansamples/"

	for k in range(1,5):	#loop through ZONES
		path = path + str(k) + "/"
		files = os.listdir(path)
		print files
		samplecount = 1
		writtenwords = 1

		for myfile in files:	#loops through FILES in a ZONE
			print myfile
			infile = open(path + myfile, 'r')
			txt = infile.read().split()
			infile.close()
			if writtenwords == 1:
				outfile = open(tpath + str(k) + "/"  + str(samplecount) + ".txt", 'w')

			for i in range(len(txt)):	#loop through WORDS in a FILE in a ZONE
				outfile.write(txt[i][:-1] + " ")

				writtenwords += 1
				if writtenwords % 4378 == 0:		#should divide text into 4378 word-long files
					outfile.close()
					samplecount += 1
					writtenwords = 1
					outfile = open(tpath + str(k) + "/"  + str(samplecount) + ".txt", 'w')
					print "break", i, samplecount

			outfile.write(" | ")
		outfile.close()

		print

		path =  "/Users/jamesfisk/Desktop/thesisc/cleanzones/"


		"""
		myfile = random.choice(files)


		while (myfile[-4:] != ".txt" and myfile[-4:] != ".TXT"):
			myfile = random.choice(files)
		

		infile = open(path + myfile, 'r')
		txt = infile.read().split()
		infile.close()

		outfile = open(tpath + str(k) + ".txt", 'w')
		print myfile
		for j in range(4378):
			outfile.write(txt[j + 500] + " ")

		outfile.close()
		path =  "/Users/jamesfisk/Desktop/thesisc/div/"
		"""

main()
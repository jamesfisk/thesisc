import io
import os
import random


def main():
	path =  "/Users/jamesfisk/Desktop/thesisc/div/"
	tpath = "/Users/jamesfisk/Desktop/thesisc/div/test/"

	for k in range(1,5):
		path = path + str(k) + "/"
		files = os.listdir(path)
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

main()
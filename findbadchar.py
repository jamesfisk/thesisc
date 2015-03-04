import io
import os

def main():

	path =  "/Users/jamesfisk/Desktop/thesisc/res/redacted/"
	files = os.listdir(path)
	#files.remove("EdwardIII_clean.txt")
	for f in files:
		if not f.endswith(".txt"):
			continue
		print f

		infile = open(path + f, 'r')
		txt = list(infile.read())
		for elt in txt:
			print f,  elt.encode('ascii', 'strict')
		infile.close()



main()
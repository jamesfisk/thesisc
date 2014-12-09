import io
import os

def main():

	path =  "/Users/jamesfisk/Desktop/thesisc/div/1/3H6RIV_clean.txt"
	infile = open(path, 'r')
	txt = list(infile.read())
	for elt in txt:
		print elt.encode('ascii', 'strict')



main()
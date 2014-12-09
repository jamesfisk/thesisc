#from textclean.textclean import textclean
import os


def main():

	path =  "/Users/jamesfisk/Desktop/thesisc/div/"
  	#print files
  	lnpath =  "/Users/jamesfisk/Desktop/thesisc/linenumbers/"


  	for k in range(1,5):
  	  path = path + str(k) + "/"
  	  files = os.listdir(path)

	  for i in range(len(files)):
	    if (files[i][-4:] != ".txt" and files[i][-4:] != ".TXT"):
	      		continue

	    
	    infile = open(path + files[i], 'r')
	    txt = list(infile.read())
	    infile.close()

	    outfile = open(path + files[i], 'w')
	    print files[i]
	    for elt in txt:


	    	outfile.write(elt.encode('ascii', 'strict'))

	    outfile.close()
	  path =  "/Users/jamesfisk/Desktop/thesisc/div/"
	  


main()
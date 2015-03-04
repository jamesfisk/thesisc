#from textclean.textclean import textclean
from parse import *
import os
import string




def more_upper (word):
	upper = 0
	lower = 0
	for letter in word:
		if letter.isupper():
			upper += 1
		else:
			lower += 1
	if upper > lower:
		return True 
	return False

if __name__ == '__main__':

	path =  "/Users/jamesfisk/Desktop/thesisc/res/redacted/"
	path2 = "/Users/jamesfisk/Desktop/thesisc/res/redactedB/"
  	#print files
  	lnpath =  "/Users/jamesfisk/Desktop/thesisc/res/copies/redacted copy/"
  	lnpath2 =  "/Users/jamesfisk/Desktop/thesisc/res/linenumbers_final/nopunct/"


	files = os.listdir(path)
	files.remove("EdwardIII__red.txt")
	outfilep = open("removed_words.txt", 'w')

	#remove scene nums
	
	for k in range(len(files)):
            if (files[k][-4:] != ".txt" and files[k][-4:] != ".TXT"):
	        continue
	    infile = open(path2 + files[k], 'r')
	    text = infile.read()
	    infile.close()

	    outfile = open(path2 + files[k], 'w')

	    for char in text:
	    	if char in ['[', ']', '{', '}', '#']:
	    		continue
	    	outfile.write(char)

	    """
	    line = infile.readline()
	    while (line):
	    	line = infile.readline()
	    	#print line
	    	if len(line.split()) == 0:
	    		continue
	    	elif line.split()[0].startswith("|A"):
	    		print line
	    		continue
	    	else:
	    		outfile.write(line)"""
	    	
	    
	    outfile.close()
	    


	"""
  	for i in range(len(files)):
	    if (files[i][-4:] != ".txt" and files[i][-4:] != ".TXT"):
	      		continue
	    infile = open(path2 + files[i], 'r')

	    text = infile.read().split()
	    infile.close()


	    #text = text.replace('\n', '\r')
	    #text = text.split('\r')

	    #print text[:5]
	    outfile = open(path2 + files[i], 'w')

	    for word in text:
	    	if word.startswith("|L"):
	    		outfile.write("\n")
	    		continue

    		if (word.isupper() or more_upper(word)) and word_minus_punct(word) not in ["I", "O", "A", "Y", "T"]:							  
    			if not word.startswith("|"):
	    			#print word
	    			outfilep.write(word + "\n")
    			continue

    		elif word.startswith("|") or word.isdigit():
    			#print word
    			outfilep.write(word + "\n")
    			continue

    		outfile.write(word + " ")
    	

        
	    #DONT DO THIS BIT UNTIL CLEANED TEXT
	    for letter in text:
	    	if letter in ['[', ']', '{', '}', '#']:
	    		continue
	    	outfile.write(letter)


	    for line in text:
	    	words = line.split()
	    	s = set([word_minus_punct(word) for word in words])
	    	if list(s) in [['\n'], ['I'], ['Enter'], ['Exit']]:
	    		continue

	    	for word in words:

	    		if (word.isupper() or more_upper(word)) and word_minus_punct(word) not in ["I", "O", "A", "Y", "T"]:							  
	    			if not word.startswith("|"):
		    			#print word
		    			outfilep.write(word + "\n")
	    			continue
	    		elif word.startswith("|") or word.isdigit():
	    			#print word
	    			outfilep.write(word + "\n")
	    			continue

	    		outfile.write(word + " ")

	    	outfile.write('\r')
	    
        outfile.close()
	    
	outfilep.close()"""

	    
	   

	  

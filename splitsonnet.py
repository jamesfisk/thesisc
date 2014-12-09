import os
import io

def main():
	path = "/Users/jamesfisk/Desktop/thesisc"
	infile = open(path + "/son_clean.txt", 'r')
	line = infile.readline().split()



	for i in range(len(line)):
		if (line[i][:2] == "|A"):
			outfile = open(path + "/son/" + line[i + 1] + ".txt", 'w')
			continue
		if (line[i][:2] == "|L"):
			outfile.write("\n")
		elif line[i].isdigit():
			continue
		else:
			outfile.write(line[i] + " ")
	outfile.close()
	infile.close()

	"""
	while (line):
		print "inf"
		while (len(line) == 0):
			print "infd"
			line = infile.readline().split()

		#strip out line no
		if len(line) > 1:
			line = line[1:]
		print line
		sonnet_no = line[0]
		outfile = open(path + "/son/" + sonnet_no + ".txt", 'w')
		line = infile.readline().split()
		if (len(line) == 0):
			print "infh"
			line = infile.readline().split()
		print line

		#write to one sonnet file
		while(line[0][:2] == "|L"):
			print line
			if (len(line) > 1):
				line = line[1:]
			outfile.write(" ".join(line))
			line = infile.readline().split()
		outfile.close()
		line = infile.readline().split()
	infile.close()
"""




main()
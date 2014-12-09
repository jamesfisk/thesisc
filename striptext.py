"""
This script takes a path to a directory. For each text file "filename.txt" in that directory, it will
remove all the xml tags and write it to "filename_clean.txt"
"""


import os
import io

def main():
  while True:
    path = "/Users/jamesfisk/Desktop/thesisc/clean/"#raw_input("Enter path name (e.g. /Users/usrnm/Documents/MyFiles): ").strip()
    if (os.path.exists(path)):
      break
    print "Not a valid path name."
  files = os.listdir(path)
  #print files
  for i in range(len(files)):
    if (files[i][-4:] != ".txt" and files[i][-4:] != ".TXT"):
      continue

    infile = open(path + files[i], 'r')
    line = infile.read()
    infile.close()
    outfile = open(path + files[i], 'w')
    bracket = False
    pipe = False
    line = list(line)
    #print line
    for char in line:
      #print char
      if char == '[':
        bracket = True
      if char == '|':
        pipe = True
      if bracket == False and pipe == False:
        #print char, bracket, pipe
        outfile.write(char)
      else:
        #print char, bracket, pipe
        outfile.write(" ")
      if char == ']':
        bracket = False
      if char == " ":
        pipe = False

    outfile.close()



main()

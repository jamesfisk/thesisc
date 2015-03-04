import io
import os
import fnmatch
import shutil


"""
recursively grab all files in path with extension "extension" 
and place them in directory dir.
"""
def grab_files (path, dest, extension):

	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(filenames, extension):
			print filename
			shutil.copy2(root + "/" + filename, dest)
	print "success"

def main():
	path = "/Users/jamesfisk/Desktop/thesisc/cleanzones/"
	dest = "/Users/jamesfisk/Desktop/thesisc/cleantxt/"
	grab_files(path, dest, '*.txt')

main()


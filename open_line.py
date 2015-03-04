from corpus import *
from syllable import *
import string

allchars = set()
iambic = [8, 9, 10, 11, 12, 13, 14]
def ispunct(char):
	p = set(string.punctuation) - set("'")
	return char in p

def iswhitespace(char):
	return char in set(string.whitespace)


def count_open_lines(text):
	ol = 0
	total = 0
	lines = text.split("\n")
	for line in lines:
		if sylco_line(line) not in iambic:
			print line
			continue
		line = list(line)
		if len(line) == 0:
			continue
		while iswhitespace(line[-1]) or line[-1] in['"', ")", "]"]:
			line.pop()
			if len(line) == 0:
				break
		if len(line) == 0:
			continue

		if not ispunct(line[-1]):
			ol += 1
		else:
			if line[-1] in [">", '`']:
				print "".join(line)
			allchars.add(line[-1])
		total += 1
	return [ol, total]


if __name__ == '__main__':
	c = get_redacted_corpus()
	f = open("corpus_lines.csv", "w")
	f.write("Title,Open Lines, Total Lines\n")
	for fid in c.fileids():
		q = count_open_lines(c.raw(fid))
		f.write(fid[:3] + "," + str(q[0]) + "," + str(q[1]) + "\n")
		#print "sonnet", i + 1, "\n", count_open_lines(s.raw(str(i + 1) + ".txt"))
		#print
	f.close()
	print allchars
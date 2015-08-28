from corpus import *
from parse import *



colloq = [[["'t"],["'tis", "'twas", "'twere"]],
		  [["i'th'"], []],
		  [["o'th", "a'th'"], []],
		  [["th'"], []],
		  [["'em", "'um"], []],
		  [["'ll"], ["i'll"]],
		  [["'rt"], []],
		  [["'re"], []],
		  [["'d", "'ld"], []],
		  [["'lt"], []],
		  [["'st", "'ve"], []],
		  [["i'm"], []],
		  [["'as"], []],
		  [["this'"], []],
		  [["'a'", "ha'"], []],
		  [["a' "], ["'a'"]],
		  [["o'"], []],
		  [[" 's "], []],
		  #this one is too hard to separate genitive from conjunctions
		  #[["'s "], [" 's ", "here's ", "there's ", "where's ", "what's ", "that's ", "how's ", "he's ", "she's ", "who's "]],
		  [["has "], []],
		  [["does"], []]]
arch = [[["eth "], []],
		[["ion "], []],
		[["ed "], []]]
most = [[[" most "], []]]

"""
pt = list of patterns we are looking for
ex = list of exclusions
"""
def count_in_txt(s, pt, ex):

	count = 0
	for p in pt:
		count += s.count(p)
	for e in ex:
		count -= s.count(e)
	return count

def generate_d_stats(txt):
	outdata = []
	txt = txt.lower()
	outdata.append(count_in_txt(txt,["'d", "'ld"], []))
	outdata.append(count_in_txt(txt,["ed "], []))
	return outdata



def generate_colloq_arch(txt):
	outdata = []
	txt = txt.lower()
	count = 0

	for i in range(len(colloq)):
		count += count_in_txt(txt,colloq[i][0], colloq[i][1])
		outdata.append(count)
		count = 0

	for i in range(len(arch)):
		count += count_in_txt(txt,arch[i][0], arch[i][1])
		outdata.append(count)
		count = 0
		"""
	for i in range(len(most)):
		count += count_in_txt(txt,most[i][0], most[i][1])
		outdata.append(count)
		count = 0
		"""
	return outdata

def print_col_data(indata):
	idx = 0
	for i in range(len(colloq)):
		print " ".join(colloq[i][0]), indata[idx], "\t"
		idx += 1
	for k in range(len(arch)):
		print " ".join(arch[k][0]), indata[idx], "\t"
		idx += 1
	print "most", indata[idx]
	print "did it  work", indata[-1]
	print indata


def print_col(l):
	for elt in l:
		if elt[1] != 0:
			print elt

if __name__ == '__main__':
	q = get_sonnet_corpus()
	o = generate_colloq_arch(q.raw("1.txt"))
	print_col_data(o)
"""
def count_ap_t(text):
	words = [word_minus_punct(word.lower()) for word in text.split()]
	count = 0
	for word in words:
		if "'t" == word[-2:] and word not in ["'tis", "'twas", "'twere"]:
			count += 1

	return count

def count_ap_l(text):
	words = [word_minus_punct(word.lower()) for word in text.split()]
	count = 0
	for word in words:
		if "'ll" == word[-3:] and word not in ["i'll"]:
			count += 1

	return count


if __name__ == '__main__':
	w = []
	f = open("./spreadsheets/most.csv", "w")

	for elt in most:
		f.write("," + "/".join(elt[0]))
		l = count_in_sonnets(elt[0],elt[1])

		w.append(l)
		print elt[0]
		print_col(l)
	f.write("\n")

	for i in range(154):
		f.write(str(i + 1) + ",")
		for k in range(len(w)):
			f.write(str(w[k][i][1]) + ",")
		f.write("\n")



"""



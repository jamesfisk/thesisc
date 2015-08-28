from corpus import *


def alpha_only(word):
	s = ""
	for char in word:
		if char.isalpha() or char in set("-'"):
			s += char
		elif char in set(",;!?.|\"\t\n\x0b\x0c\r "):
			s += " "

	return s

if __name__ == '__main__':

	c = get_clean_corpus()
	hc = alpha_only(c.raw('WT clean csv.txt')).split()

	

	x = get_xml_corpus()
	hx = alpha_only(x.raw('WTRIV.TXT')).split()
	print len(hx)
	t = []

	for elt in hc:
		try:
			hx.remove(elt)
		except (ValueError):
			t.append(elt)

	print len(hx)
	print "IN"
	for elt in hx:
		if elt not in  ["L", "--"]:
			print elt,
	print
	print
	print "OUT"
	for elt in t:
		print elt,



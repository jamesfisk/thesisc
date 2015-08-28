from corpus import *
from parse import *
import pickle

SUPP = ["Edward", "Lucrece", "Venus", "MOV", "Temp", "Lear", "Phoenix", "pilgrim", "complaint", "John", "ROMEO"]


def make_csv(l, fid):
	f = open(fid, 'w')

	for i in range(len(l)):
		f.write(",".join(l[i]) + "\n")
	f.close()

def build_evans():
	path = "./res/ref/"
	l= []
	for i in range(1, 155):
		f = open(path + str(i) + ".txt", "r")
		txt = f.read().split("\n")
		f.close()
		s = []
		for line in txt:
			for word in line.split():
				word = word_minus_punct(word.upper())

				for play in ALLPLAYS + SUPP:
					if word == play.upper():
						s.append(word)

					"""
					if word.startswith(play.upper()):
						print "Word:", word, "\nLine:", line
						cit = raw_input("Cit:")
						if cit == 0:
							continue
						elif cit == 1:
							s.append(word)
						else:
							s.append(cit)
							"""
		l.append(s)
	make_csv(l, "evans.csv")
	pickle.dump(l, open("cit.p", "w"))

def build_composite():
	f1 = open("./spreadsheets/BoothePlayCount.csv", "r")
	f2 = open("./spreadsheets/WellsPlayCount.csv", "r")
	f3 = open("./spreadsheets/evansB.csv", "r")

	booth = f1.read().split("\n")
	wells = f2.read().split("\n")
	evans = f3.read().split("\n")

	f1.close()
	f2.close()
	f3.close()

	bb = [wells, booth, evans]
	l = []


	for i in range(3):
		s = []
		for k in range(155):
			try:
				s.append((bb[i][k].replace(",", " ")).split())
			except IndexError, e:
				pass
		l.append(s)
	pickle.dump(l, open("smallfry.p", "w"))

def play_by_play_graph():
	periods = [PERIOD1, PERIOD2, PERIOD3, PERIOD4]

	d = pickle.load(open("smallfry.p", "r"))

	f = open("./spreadsheets/bigmama.csv", "w")
	f.write("," + ",".join([str(x) for x in range(1, 155)]) + "\n")

	for period in periods:
		for play in period:
			f.write(play + ",")
			for i in range(154):
				count = 0
				for k in range(3):
					for elt in d[k][i]:
						if elt == play:
							count += 1
				f.write(str(count) + ",")
			f.write("\n")
		f.write("\n\n")

	f.close()

def period_citations_by_sonnet():
	f = open("./spreadsheets/bigmama2.csv", "r")
	f.readline()
	s = [[] for x in range(154)]
	for i in range(4):
		l = f.readline().split(",")[1:-1]
		for k in range(len(l)):
			s[k].append(int(l[k]))
	return s


if __name__ == '__main__':
	build_composite()
	play_by_play_graph()
	periods = [PERIOD1, PERIOD2, PERIOD3, PERIOD4]

	d = pickle.load(open("smallfry.p", "r"))

	f = open("./spreadsheets/bigmama2.csv", "w")
	f.write("," + ",".join([str(x) for x in range(1, 155)]) + "\n")
	ct = 1
	for period in periods:
		f.write("Period " + str(ct) + ",")
		ct += 1

		for i in range(154):
			count = 0
			for play in period:

				for k in range(3):
					for elt in d[k][i]:
						if elt == play:
							count += 1
			f.write(str(count) + ",")
		f.write("\n")

	f.close()






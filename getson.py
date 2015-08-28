from corpus import *


def son_num():
	s = get_sonnet_corpus()

	while True:
		num = int(raw_input("Sonnet: "))
		if num == 0:
			exit()
		if num in [x for x in range(1, 155)]:
			print
			print s.raw(str(num) + ".txt")
			print

def word_search():
	s = get_sonnet_list()

	while True:
		word = raw_input("Word: ")
		if word == "0":
			return
		for i in range(len(s)):
			for line in s[i].split("\n"):
				if word in line.lower():
					print i+1, line

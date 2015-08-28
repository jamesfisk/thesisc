



def get_son_metrics(num):
	"""
	UOL,U,FE,Most,Colloq,Arch,LE,WE,MLE
	0   1 2  3    4      5    6  7  8
	"""
	f = open("./spreadsheets/son_counts_comp.csv", "r")
	line = f.readline()
	sons = []
	while line:
		line = f.readline().split(",")[1:]
		if line != []:
			sons.append([int(x) for x in line])
	f.close()
	return sons[num - 1]

if __name__ == '__main__':
	s = get_son_metrics()
	print s[-1], len(s)
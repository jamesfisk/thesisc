from nltk.corpus import inaugural
import nltk


def main():

	cfd = nltk.ConditionalFreqDist(
			 (target, file[:4]) 
			 for fileid in inaugural.fileids()
             for w in inaugural.words(fileid)
             for target in ['democracy', 'republic']
             if w.lower().startswith(target))
	cfd.plot()

main()
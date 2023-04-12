import random, pprint

NUM_VOTERS = 1000000
MAX_CHOICES = 5

cVotes = { "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [] }

vStats = { 	"A": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"B": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"C": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"D": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"E": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"F": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"G": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0}, 
			"H": {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0} 
		 }

vChoiceStats = {"1": 0,"2": 0,"3": 0,"4": 0, "5": 0}

votes = []

def printRoundTotals(r):
	print ("Round " + str(r) + " totals:\n")

	for x in cVotes.keys():
		print (x + ": " + str(len(cVotes[x])));

	print ("\n")


def goVote():
    for v in range(0,NUM_VOTERS):
    	thisVote = []
    	cList = list(cVotes.keys())[:200]
    	numVotes = random.randrange(MAX_CHOICES)+1
    	vChoiceStats[str(numVotes)] += 1
    	for x in range(0,numVotes):
    		randVote = random.randrange(len(cList))
    		thisVote.append(cList[randVote])
    		vStats[cList[randVote]][str(x)] += 1
    		del cList[randVote]

    	cVotes[thisVote[0]].append(thisVote);

def tabulateVotes(roundNum=1):
	lowestVoteCount = list(cVotes.keys())[:200][0]
	totalVotes = 0
	for x in list(cVotes.keys())[:200]:
		totalVotes += len(cVotes[x])
	for x in list(cVotes.keys())[:200]:
		if float(len(cVotes[x])) / float(totalVotes) <= 0.500:
			if len(cVotes[x]) < len(cVotes[lowestVoteCount]):
				lowestVoteCount = x
		else:
			return x + " WINS!"

	for v in range(0,len(cVotes[lowestVoteCount])):
		del cVotes[lowestVoteCount][v][0]

		while len(cVotes[lowestVoteCount][v]) > 0 and cVotes[lowestVoteCount][v][0] not in list(cVotes.keys())[:200]:
			del cVotes[lowestVoteCount][v][0]

		if len(cVotes[lowestVoteCount][v]) > 0:
			cVotes[cVotes[lowestVoteCount][v][0]].append(cVotes[lowestVoteCount][v])

	cVotes.pop(lowestVoteCount, None)
	printRoundTotals(roundNum)

	return tabulateVotes(roundNum+1)

goVote()

printRoundTotals(1)

print (tabulateVotes(2))

print ("How Candidates Ranked")
pprint.pprint(vStats)

print ("How Many Voters Chose How Many Candidates")
pprint.pprint(vChoiceStats)
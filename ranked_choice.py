import random, pprint

NUM_VOTERS = 1000000
MAX_CHOICES = 5

cVotes = { "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0 }

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

def goVote():
    while len(votes) < NUM_VOTERS:
    	thisVote = []
    	cList = cVotes.keys()
    	numVotes = random.randrange(MAX_CHOICES)+1
    	vChoiceStats[str(numVotes)] += 1
    	for x in range(0,numVotes):
    		randVote = random.randrange(len(cList))
    		thisVote.append(cList[randVote])
    		vStats[cList[randVote]][str(x)] += 1
    		del cList[randVote]

    	votes.append(thisVote);

    	if thisVote[0] not in cVotes.keys():
    		cVotes[thisVote[0]] = 1
    	else:
    		cVotes[thisVote[0]] += 1

def tabulateVotes(roundNum=1):
	lowestVoteCount = cVotes.keys()[0]
	totalVotes = 0
	for x in cVotes.keys():
		totalVotes += cVotes[x]
	for x in cVotes.keys():
		if float(cVotes[x]) / float(totalVotes) <= 0.500:
			if cVotes[x] < cVotes[lowestVoteCount]:
				lowestVoteCount = x
		else:
			return x + " WINS!"

	for v in range(0,len(votes)):
		if len(votes[v]) > 0:
			if votes[v][0] == lowestVoteCount:
				del votes[v][0]
				while len(votes[v]) > 0 and votes[v][0] not in cVotes.keys():
					del votes[v][0]
				if len(votes[v]) > 0:
					cVotes[votes[v][0]] += 1
	cVotes.pop(lowestVoteCount, None)
	print "Round " + str(roundNum+1) + " totals: \n" + str(cVotes)

	return tabulateVotes(roundNum+1)

goVote()

print "Round 1 totals:\n" + str(cVotes)

print tabulateVotes()

print "How Candidates Ranked"
pprint.pprint(vStats)

print "How Many Voters Chose How Many Candidates"
pprint.pprint(vChoiceStats)
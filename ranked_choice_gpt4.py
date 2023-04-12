import random
from collections import Counter
import pprint

NUM_VOTERS = 1000000
MAX_CHOICES = 5

cVotes = { "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [] }
vStats = {key: Counter() for key in cVotes.keys()}
vChoiceStats = Counter()

def printRoundTotals(r):
    print(f"Round {r} totals:\n")
    for x in cVotes.keys():
        print(f"{x}: {len(cVotes[x])}")
    print("\n")

def goVote():
    for _ in range(NUM_VOTERS):
        cList = list(cVotes.keys())[:200]
        numVotes = random.randrange(MAX_CHOICES) + 1
        vChoiceStats[numVotes] += 1
        thisVote = random.sample(cList, numVotes)
        for idx, candidate in enumerate(thisVote):
            vStats[candidate][idx] += 1
        cVotes[thisVote[0]].append(thisVote)

def tabulateVotes():
    roundNum = 1
    while True:
        printRoundTotals(roundNum)

        lowestVoteCount = min(cVotes, key=lambda x: len(cVotes[x]))
        totalVotes = sum(len(votes) for votes in cVotes.values())
        
        for x in cVotes.keys():
            if len(cVotes[x]) / totalVotes > 0.5:
                return f"{x} WINS!"

        for v in cVotes[lowestVoteCount]:
            del v[0]
            while len(v) > 0 and v[0] not in cVotes:
                del v[0]
            
            if len(v) > 0:
                cVotes[v[0]].append(v)
        
        cVotes.pop(lowestVoteCount)
        roundNum += 1

goVote()
printRoundTotals(1)
print(tabulateVotes())

print("How Candidates Ranked")
pprint.pprint(vStats)

print("How Many Voters Chose How Many Candidates")
pprint.pprint(dict(vChoiceStats))

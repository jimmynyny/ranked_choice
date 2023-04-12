import csv
from collections import Counter
import pprint
import sys

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            yield row

def process_votes(votes_data):
    cVotes = {}
    vStats = {}
    vChoiceStats = Counter()

    for row in votes_data:
        for candidate in row:
            if candidate not in cVotes:
                cVotes[candidate] = []
                vStats[candidate] = Counter()

        numVotes = len(row)
        vChoiceStats[numVotes] += 1
        for idx, candidate in enumerate(row):
            vStats[candidate][idx] += 1
        cVotes[row[0]].append(row)

    return cVotes, vStats, vChoiceStats

def printRoundTotals(r, cVotes):
    print(f"Round {r} totals:\n")
    for x in cVotes.keys():
        print(f"{x}: {len(cVotes[x])}")
    print("\n")

def tabulateVotes(cVotes, vStats, vChoiceStats):
    roundNum = 1
    while True:
        printRoundTotals(roundNum, cVotes)

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

if len(sys.argv) != 2:
    print("Usage: python tabulate_votes.py <input_csv>")
    sys.exit(1)

input_csv = sys.argv[1]
votes_data = read_csv(input_csv)
cVotes, vStats, vChoiceStats = process_votes(votes_data)
printRoundTotals(1, cVotes)
print(tabulateVotes(cVotes, vStats, vChoiceStats))

print("How Candidates Ranked")
pprint.pprint(vStats)

print("How Many Voters Chose How Many Candidates")
pprint.pprint(dict(vChoiceStats))

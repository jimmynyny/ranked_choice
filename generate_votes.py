import csv
import random
import sys

def generate_votes_csv(num_rows, candidates, file_name):
    votes_data = []

    for _ in range(num_rows):
        num_choices = random.randint(1, len(candidates))
        choices = random.sample(candidates, num_choices)
        votes_data.append(choices)

    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(votes_data)

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python generate_votes.py <number_of_rows> <candidates> [output_file]")
    sys.exit(1)

num_rows = int(sys.argv[1])
candidates = sys.argv[2].split(',')
file_name = sys.argv[3] if len(sys.argv) == 4 else "example_votes.csv"
generate_votes_csv(num_rows, candidates, file_name)

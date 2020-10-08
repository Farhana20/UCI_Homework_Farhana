import os
import csv

vote_path = os.path.join("Resources", "election_data.csv")

#variables
total_votes = []
candidates_dup = []
candidates = []
totalvoters = 0
count = 0
percent = 0
cand = []
countcand = []
percentcand = []


with open(vote_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)


    for row in csvreader:
        total_votes.append(row[0])
        candidates_dup.append(row[2])
    for i in range(len(total_votes)):
        if 'candidates_dup[i]' not in candidates:
            candidates.append(candidates_dup[i])

print(f'{len(total_votes)}')
print(f'{candidates}')

         
        #print(i,row[2])
        #count += 1
        #percent =(count/ totalvoters)* 100

        #countcand.append(count)
        #percentcand.append(percent)

#zip(cand, percentcand, countcand)

#print(totalvoters)
#print(cand)
#print(countcand)




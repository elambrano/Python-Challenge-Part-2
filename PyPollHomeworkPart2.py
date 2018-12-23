fn = 'Resources/election_data.csv'
f = open (fn)
contents = f.read()
f.close()

lines = contents.split('\n')
print('Length =', len(lines))
for line in lines[0:10]:
    print(line)
    
lines = lines[1:]
# drop last line if it's empty
if lines[-1]=="":
    lines.pop()


#Question 1 (total Votes)
total_votes = len(lines)
print(total_votes)

#Question 2
election_dictionary={}
for line in lines:
    items = line.split(',')
    candidate = items [2]
    if candidate in election_dictionary:
        election_dictionary [candidate] +=1
    else:
        election_dictionary [candidate] = 1

candidates_with_votes = list (election_dictionary.keys())
print(candidates_with_votes)

#Question 3&4 percentage & number of votes
election_results = []
for candidate,count in election_dictionary.items():
    percentage_votes = count/total_votes*100
    candidate_data = (count,percentage_votes,candidate)
    election_results.append(candidate_data)
sorted_results = sorted(election_results,reverse = True)
print(sorted_results)

#Question 5
winner = sorted_results [0][2]
print("Election Results")
print("-" * 20)
print("Total Votes:",total_votes)
print("-" * 20)
for cr in sorted_results:
    print('%s: %.3f%% (%d)' % (cr[2], cr[1], cr[0]) )
print("-" * 20)
print("Winner:",winner)
print("-" * 20)






















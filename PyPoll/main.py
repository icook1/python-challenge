#Import OS and CSV
import os
import csv
#Previous trouble with PC correctly identifying the directory. Identify current working directory and utilize absolute path to ensure correct file consistenly.
print("Current Working Directory:", os.getcwd())
os.chdir("C:\\Users\\ormis\\Desktop\\python-challenge\\PyPoll\\Resources")
election_csv = os.path.join("..", "Resources", "election_data.csv")
absolute_csvpath = os.path.abspath(election_csv)
print("Absolute Path:", absolute_csvpath)
#Establish baseline variables
total_votes = 0 
candidates_list = []
candidate_votes_dict = {}
winner = ""
winning_votes = 0

#Open the CSV in reader mode with a comma delimiter.
with open(election_csv, encoding="utf-8") as csv_file:
    election_csv = csv.reader(csv_file, delimiter=",")
#Identify and move on from the CSV header if one is in the file.
    csv_header = next(csv_file)
#Loop through the CSV file counting the total number of votes for each candidate and establishing a list of candidates.    
    for row in election_csv:
        total_votes = total_votes + 1
        candidate = row[2]
        

        if candidate not in candidates_list:
            candidates_list.append(candidate) 
            candidate_votes_dict[candidate] = 0
       
       
#dictionary for candidate votes needed with names of candidates
        candidate_votes_dict[candidate] = candidate_votes_dict[candidate] + 1
with open("C:\\Users\\ormis\\Desktop\\python-challenge\\PyPoll\\Analysis\\PyPoll Text Analysis.txt","w") as txt_file:
#Print results of the total votes to the text file utilized for the final analysis.
    election_results = (
        f"Election Results\n"
        f"-----------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------\n")
    print(election_results)

    txt_file.write(election_results)
#Loop through the CSV to determine the individual votes for each established candidate and their percentage of the total vote count.
    for candidate in candidate_votes_dict:
        votes = candidate_votes_dict.get(candidate)
        percent_of_vote = float(votes) / float(total_votes) * 100

        if (votes > winning_votes):
            winning_votes = votes
            winner = candidate
        
        results = f"{candidate}: {percent_of_vote:.3f}% ({votes})\n"
        print(results)

        txt_file.write(results)
#Determine and print the Candidate name with the most votes who is the winner.
    winner_results = (
        f"----------------\n"
        f"Winner: {winner}"
        f"----------------\n"
    )
    print(winner_results)
#Write the winning candidiate to the text file with previous results.
    txt_file.write(winner_results)



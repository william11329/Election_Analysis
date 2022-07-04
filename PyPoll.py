# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#declare new list for candidates (added before open)
candidate_options = []

#declaring an empty dictionary for vote tallying
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    file_reader = csv.reader(election_data, delimiter=",")

# read the header row.
    headers = next(file_reader)

 # Print each row in the CSV file.
    for row in file_reader:
        #2. add to the total vote count.
        total_votes += 1
  
  #3 print total votes
   # print(total_votes)
 # Print the candidate name from each row.
        candidate_name = row[2]      

# If the candidate does not match any existing candidate... adding IF statement to narrow list
        if candidate_name not in candidate_options:

# Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

#this will begin to track a candidates vote count
            candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
#print(candidate_options)

#print the candidate vote dictionary
        #print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.") 
 # Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        headers = next(file_reader)
        print(headers)

        

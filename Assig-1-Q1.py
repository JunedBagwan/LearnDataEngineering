
# Write a Python program that reads the CSV file and outputs the following information:
# The total number of interactions in the file.
# The total number of unique users in the file.
# The most visited URL in the file.
# The average time spent on each URL.



import pandas as pd

file_path = input("Enter the file path : ")

#storing a input file into the dataframe
df = pd.read_csv(file_path)

#E:\Study Folder\Growth School\Module 1 - Assignment\user_visited.csv

#Total Interactions
total_interactions = len(df.index)

#Total Unique Users
total_uniqueusers = df["user_id"].nunique()

#Most visited url
mostvisitedurl = df["url"].value_counts().sort_values(ascending=False).index[0]

Question = ["Total Interatioctions", "Total Unique Users","Most Visited URL"]
OutPut =[total_interactions,total_uniqueusers,mostvisitedurl]

var = {'Question': Question, 'Output': OutPut}

opDF= pd.DataFrame(var)

opDF.to_csv('Output-Q1.csv',index=False)

print(opDF)







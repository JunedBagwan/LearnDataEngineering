import pandas as pd
import datetime as dt

file_path = input("Enter file path: ")

#E:\Study Folder\Growth School\Module 1 - Assignment\customer_input.csv
df = pd.read_csv(file_path)

#Group data by Date
# 1. Covert column 'timestamp' datatype
df['timestamp']=pd.to_datetime(df.timestamp)

#2. Covert timestamp to 'YYYY-MM-DD' Format
df['timestamp']=df['timestamp'].dt.date

df.groupby(['timestamp','customer_id'])[['product_price','quantity']].sum()

#3.Total Spent
df['total_spent'] = df['product_price']*df['quantity']

#print(df[['timestamp','total_spent','product_price','quantity']])

outputdf= pd.DataFrame({"date":df['timestamp'],"customer_id":df['customer_id'],"total_spent":df['total_spent']})

outputdf.to_csv("Output-Q2.csv",index=False)

print(outputdf)


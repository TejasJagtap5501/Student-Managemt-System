# Pandas: This is use for data analysis 
# command: pip install pandas

import pandas as pd

# data = [10, 20, 30]

# arr = pd.Series(data, index=["a", "b", "c"])

# print(arr)

# /*********************************************
# create 2d array 

# Series and dataframe 
# names = pd.Series(["Tejas", "Sarthak", "Rudhre"])
# marks = pd.Series([55, 89, 67])

# print(names)
# print(marks)

# /**********************************************************************

# import pandas as pd

# data = {
#     "Subject": ["Maths", "Science", "English", "Computer"],
#     "Marks": [80, 75, 85, 90]
# }

# df = pd.DataFrame(data)
# # df.to_csv("__csv",index=False)
# print(df)
# total = df["Marks"].sum()
# max=df["Marks"].max()

# average = df["Marks"].mean()

# print("Total Marks:", total)
# print("Average Marks:", average)
# print("Maximum marks is:",max)

# /*****************************************************

import pandas as pd

data = {
    "Subject": ["Maths", "Science", "English", "Computer"],
    "Marks": [80, 75, 85, 90]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)

# Read from CSV
df2 = pd.read_csv("data.csv")

print(df)
print(df2)

# /*****************************************

write: to_csv ( use )
Read : to_csv

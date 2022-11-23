#Title: damir_usersp1.py
#Date: November 22, 2022
#Author: Jamal Eddine Damir
#Description: Code that demonstrates how to select data from MongoDB using Python
#Sources:
# W3Schools.com

# Importing MongoClient
from pymongo import MongoClient

# Connecting to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.5vradwb.mongodb.net/web335DBretryWrites=true&w=majority")

# Assigning web335DB to db variable
db = client["web335DB"]

# Assigning users' collection to users_col variable
users_col = db["users"]

# Displaying all the documents in the users' collection
for user in users_col.find():
   print(user)

# Displaying data for user with specific employeeId
print(users_col.find_one({"employeeId": "1011"}))

# Displaying data for user with specific lastName
print(users_col.find_one({"lastName": "Mozart"}))





""" 
Title: damir_usersp2.py
Date: November 29, 2022
Author: Jamal Eddine Damir
Description: Code that demonstrates how to modify MongoDB documents using Python
Sources:
 W3Schools.com 
"""

# Importing MongoClient
from pymongo import MongoClient
import datetime

# Connecting to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.5vradwb.mongodb.net/web335DBretryWrites=true&w=majority")

# Assigning web335DB to db variable
db = client["web335DB"]

# Assigning users' collection to users_col variable
users_col = db["users"]

# Creating a new user document
users_col.insert_one({
    "firstName" : "Jack",
    "lastName" : "Sparrow",
    "employeeId" : "1014",
    "email" : "jack@sparrow.com",
    "dateCreated" : datetime.datetime.now()
    })

# Displaying newly created user
print(users_col.find_one({"lastName": "Sparrow"}))

# Updating new user's email address
users_col.update_one({"lastName" : "Sparrow"},
    {"$set" : {"email" : "pirate@jacksparrow.com"}})

# Displaying the updated document
print(users_col.find_one({"lastName": "Sparrow"}))

# Deleting newly created user
users_col.delete_one({ "lastName" : "Sparrow" })

# Proving that document was deleted (returns "None")
print(users_col.find_one({"lastName": "Sparrow"}))


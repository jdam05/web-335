/**
 * Title: damir-assignment4.2.js
 * Date: November 15, 2022
 * Author: Jamal Eddine Damir
 * Description: This file contains MongoDB Queries used to get
 *              data from the users collection
 * Sources:
 * Source code from class GitHub Repository
 * Instructor provided assignment specific instructions
 */

// loading users.js file to database
load("users.js");

// Finding all the documents in the users collection
db.users.find({});

// Finding user by email address
db.users.find({ email: "jbach@me.com" });

// Finding user by last name
db.users.find({ lastName: "Mozart" });

// Find user by first name
db.users.find({ firstName: "Richard" });

// Finding user by employee ID
db.users.find({ employeeId: "1010" });

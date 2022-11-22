/**
 * Title: damir-Assignment5.2.js
 * Date: November 19, 2022
 * Author: Jamal Eddine Damir
 * Description: This file contains MongoDB Queries that perform
 *              multiple operations on the users collection data.
 *
 * Sources:
 * Source code from class GitHub Repository
 * Instructor provided assignment specific instructions
 */

// Adding a new user to the users collection
db.users.insertOne({
	firstName: "Jamal",
	lastName: "Damir",
	employeeId: "1013",
	email: "jdamir@my365.bellevue.edu",
	dateCreated: new Date(),
});

// Updating email address by user last name
db.users.updateOne(
	{ lastName: "Mozart" },
	{
		$set: { email: "mozart@me.com" },
	}
);

// Displaying Mozart user document to prove email address change
db.users.aggregate([{ $match: { lastName: "Mozart" } }]);

// Listing all the documents and displaying specific fields
db.users.aggregate([
	{ $project: { _id: 0, firstName: 1, lastName: 1, email: 1 } },
]);

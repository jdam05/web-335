/*
 * Title: damir-Assignment6.2.js
 * Date: November 22, 2022
 * Author: Jamal Eddine Damir
 * Description: This file contains MongoDB Queries that perform
 *              multiple operations on the houses and student collections data.
 *
 * Sources:
 * Source code from class GitHub Repository
 * Instructor provided assignment specific instructions
 */

// Showing a list of all the documents in the houses collection
db.houses.find({});

// Showing a list of all the documents in the students collection
db.students.find({});

// Adding a student document to the students collection
db.students.insertOne({
	firstName: "Jamal",
	lastName: "Damir",
	studentId: "s1019",
	houseId: "h1011",
});

// Showing that document was added to the collection
db.students.findOne({ lastName: "Damir" });

// Deleting added document form student collection
db.students.deleteOne({ lastName: "Damir" });

// Showing students by house
db.students.aggregate([
	{
		$lookup: {
			from: "houses",
			localField: "houseId",
			foreignField: "houseId",
			as: "houseInfo",
		},
	},
]);

// Showing students at house Gryffindor (houseId: "h1007")
db.students.aggregate([
	{
		$lookup: {
			from: "houses",
			localField: "houseId",
			foreignField: "houseId",
			as: "houseInfo",
		},
	},
	{
		$match: {
			houseId: "h1007",
		},
	},
]);

// Showing students with "Eagle" Mascot
db.students.aggregate([
	{
		$lookup: {
			from: "houses",
			localField: "houseId",
			foreignField: "houseId",
			as: "houseInfo",
		},
	},
	{
		$match: {
			"houseInfo.mascot": "Eagle",
		},
	},
]);

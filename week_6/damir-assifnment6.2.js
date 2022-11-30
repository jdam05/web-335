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
db.houses.aggregate([
	{
		$lookup: {
			from: "students",
			localField: "houseId",
			foreignField: "houseId",
			as: "student_doc",
		},
	},
]);

// Showing students at house Gryffindor (houseId: "h1007")
db.houses.aggregate([
	{
		$lookup: {
			from: "students",
			localField: "houseId",
			foreignField: "houseId",
			as: "student_doc",
		},
	},
	{ $match: { founder: "Godric Gryffindor" } },
]);

// Showing students with "Eagle" Mascot
db.houses.aggregate([
	{
		$lookup: {
			from: "students",
			localField: "houseId",
			foreignField: "houseId",
			as: "student_doc",
		},
	},
	{
		$match: {
			mascot: "Eagle",
		},
	},
]);

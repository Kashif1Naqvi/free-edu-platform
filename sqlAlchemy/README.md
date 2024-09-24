The purpose of this repository for learning and improve skills

`Assignment 1: Basic CRUD Operations`
Create:

Insert 3 users into the User table, with varying attributes such as name, age, and is_deleted status.
Each user should have 2-3 addresses in different cities.
Read:

Retrieve all users who are older than 25 years and display their names and ages.
Retrieve all addresses where the state is "California".
Update:

Update the age of one user by increasing it by 5 years.
Change the city of one of the addresses from "Los Angeles" to "San Diego".
Delete:

Soft delete a user by setting their is_deleted to True.
Hard delete an address that belongs to a specific user.


`Assignment 2: Relationships and Joins`
One-to-Many Relationship:

Fetch all users and for each user, print their name and the cities they have addresses in.
Joins:

Perform an SQL join using SQLAlchemy to fetch users and their respective cities from the Address table.
Fetch users who have an address in the city "New York" using a join.
Count:

Write a query that counts the number of addresses each user has.
Display the result as User: <name>, Number of addresses: <count>.

`Assignment 3: Complex Queries`
Filter with Conditions:

Fetch all users who have more than 2 addresses and are not marked as is_deleted.
Group By and Aggregate:

Write a query to find out how many users are in each state based on the address table (group by state).
The output should be State: <state>, Users: <count>.
Subquery:

Write a query that fetches users who have an address in a city where more than 2 users live.

`Assignment 4: Optimizing Queries`
Eager Loading:

Use the joinedload option to optimize a query that fetches users and their addresses, reducing the number of queries made to the database.
Batch Updates:

Update the state field of all users living in California to "CA" using a bulk update query.

`Assignment 5: Advanced Queries and Pagination`
Pagination:

Implement pagination for fetching users, showing only 5 users per page.
Write a query to fetch the 2nd page of results.
Searching:

Implement a search functionality where you can filter users by name and state. The query should allow partial matches (use SQL’s LIKE feature with SQLAlchemy).

`Bonus Assignment: Soft Deletes`
Soft Delete Handling:
Modify your existing queries to automatically exclude users who are soft deleted (is_deleted = True).
Use a custom Query class or a default filter to exclude deleted users globally without modifying each query.

--Note
`How to Approach the Assignments:`
Use the session.add() and session.commit() for inserting records.
Use session.query() to fetch data and filter it based on conditions.
Make use of the join() function for joins.
Use the func module for aggregate queries like COUNT and SUM.
For pagination, use offset and limit to fetch specific pages.
You can use joinedload for eager loading when optimizing the queries that involve relationships.

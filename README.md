# Overview

While majoring in software engineering, I have made a goal to learn and try something new that I have never done before every two weeks. This way I can discover different kinds of software and hopefully find something that I really enjoy. 

For this repository I wrote a program that uses an SQL relational database to store different kinds of crocheting stiches. When you start the program it will ask you if you'd like to run it with user or administrator privileges. Depending on which one you choose, you will be able to modify, delete, or query the database. 

My purpose for writing this software was to become familiar with SQL databases and the different ways to implement them. Particularly how to use an SQL database with Python, which is suprisingly easy and straight forward.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

SQL stands for Structured Query Language and is used for relational databases.

Relational databases are a collection of data items that have predefined relationships between them. Everything within a table is related to that table, and all tables are related to one another in some way. 

For the database I created, it has one table called 'stiches'. Within the table you can store the 'name' of the stich as well as the url of a 'photo'. For a later challenge I would like to make the 'photo' a BLOB so that you can actually store a photo in the database, as well as add some more tables to the database.

# Development Environment

For this program I used Python and the SQLite library. The SQLite library is supported by python and very easy to use and understand. Once you have imported the library you can start writing code. There are no extra steps to get the libary working. SQLite works by storing the database right on to your computer. There is no separate server process requiered to store and run the database. 

# Useful Websites

* [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-python/)
* [SQLite BLOB Information](https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/)

# Future Work

* Implement the use of BLOB or some other form to store a picture
* Make the database display pretty
* Add website links to provide more information about the different stiches
* Make it so you have to provide a password to use administrator privileges

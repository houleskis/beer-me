import sqlite3

#testing database
db = 'lcbo_db_test.db'

#Establish connection with the db. If the db does not exist, it will be create in this directory
con = sqlite3.connect(db)


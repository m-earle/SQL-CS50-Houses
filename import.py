# TODO
from cs50 import SQL
from sys import argv, exit
import csv

##create a sqllite database
##later in program can use db to execute queries
##e.g., db.execute("QUERY")

db = SQL("sqlite:///students.db")

##check number of commandline arguments
##one argument that should be a csv file

def main():
    if len(argv) != 2:
        print("missing command line argument")
        exit(1)

##create table called "students" and sepcify the columns we want
##all of which will be tet except birth

    #db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

##open CSV file given by command-line argument

    with open(argv[1], "r")as titles:
        reader = csv.DictReader(titles)

        ##for row in reader:
            ##print (row)

        for row in reader:
            x = row["name"].split()
            if len(x) == 2:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                            x[0], None, x[1], row["house"], row["birth"])
            else:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                            x[0], x[1], x[2], row["house"], row["birth"])
main()
# TODO

from sys import argv, exit
from cs50 import SQL

##check for command line arguments

def main():
    if len(argv) != 2:
        print("missing command line argument")
        exit(1)

##query the database for all students in the house

    db = SQL("sqlite:///students.db")

    ## question acts as placeholder, value indicated at end of statement

    row = (db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1]))
    for i in range(len(row)):
        first = row[i]["first"] ##this gives lavender
        middle = row[i]["middle"] ##this gives none
        last = row[i]["last"] ##this prints out brown (first row last name)
        birth = row[i]["birth"] ##this gives birth year

        if row[i]["middle"] == None: ##if there's no middle name
            print(f"{first} {last}, born {birth}")
        else:
            print(f"{first} {middle} {last}, born {birth}")

main()

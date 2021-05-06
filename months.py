#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program tells the month of the year
#   inputted by the user


def main():
    # this function determines the month

    # input
    print("What month of the year is it?")
    month = int(input("Enter a number from 1-12: "))

    # process and output
    if month == 1:
        print("January!")
    elif month == 2:
        print("February!")
    elif month == 3:
        print("March!")
    elif month == 4:
        print("April!")
    elif month == 5:
        print("May!")
    elif month == 6:
        print("June!")
    elif month == 7:
        print("July!")
    elif month == 8:
        print("August!")
    elif month == 9:
        print("September!")
    elif month == 10:
        print("October!")
    elif month == 11:
        print("November!")
    elif month == 12:
        print("December!")

if __name__ == "__main__":
    main()

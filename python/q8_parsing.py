#!/usr/bin/env python

# The football.csv file contains the results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79
# goals against opponents, and had 36 goals scored against them). Write a
# program to read the file, then print the name of the team with the smallest
# difference in 'for' and 'against' goals.

# The below skeleton is optional.  You can use it or you can write the script
# with an approach of your choice.


import csv


def read_data():
    """
    Returns a generator yielding a dictionary for each row in football.csv.
    """
    with open('football.csv') as csv_file:
        for row in csv.DictReader(csv_file):
            yield row


def get_teams(data):
    """
    Returns a tuple containing the the smallest difference between goals scored
    and goals allowed, and the list of all teams having this goal difference,
    respectively.
    """
    min_scoring_diff = 1000

    for row in data:
        scoring_diff = int(row['Goals']) - int(row['Goals Allowed'])

        if scoring_diff < min_scoring_diff:
            min_scoring_diff = scoring_diff
            teams = []

        if scoring_diff == min_scoring_diff:
            teams.append(row['Team'])

    return min_scoring_diff, teams

if __name__ == "__main__":
    print(get_teams(read_data()))

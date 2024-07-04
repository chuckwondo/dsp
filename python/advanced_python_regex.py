#!/usr/bin/env python

import csv
from collections import Counter


def read_faculty():
    with open('faculty.csv') as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        my_faculty = [professor for professor in reader]

    return my_faculty


def count_degrees(my_faculty):
    # A professor may hold multiple degrees (space-separated), so the
    # following produces a list of lists of degrees.
    degree_lists = [professor['degree'].split() for professor in my_faculty]

    # Flatten the list of lists of degrees, removing dots ('.') from the degree
    # values to create canonical values so that, for example, 'Ph.D.' and 'PhD'
    # can be counted as the same type of degree.
    degrees = [d.replace('.', '') for degrees in degree_lists for d in degrees]

    # Return a dictionary of {degree: frequency}
    return Counter(degrees).items()


def count_titles(my_faculty):
    my_titles = [professor['title'].replace(' is ', ' of ')
                 for professor in my_faculty]

    # Return a dictionary of {title: frequency}
    return Counter(my_titles).items()


def select_email_addresses(my_faculty):
    return [professor['email'] for professor in my_faculty]


def count_email_domains(my_emails):
    # Return a dictionary of {domain: frequency}
    return Counter([email.split('@')[1] for email in my_emails]).items()


if __name__ == "__main__":
    faculty = read_faculty()
    counts = sorted(count_degrees(faculty))
    titles = sorted(count_titles(faculty))
    emails = sorted(select_email_addresses(faculty))
    domains = sorted(count_email_domains(emails))

    print("There are %i distinct degrees: %s" % (len(counts), counts))
    print("There are %i distinct titles: %s" % (len(titles), titles))
    print("Email address:")
    print('\n'.join(emails))
    print("There are %i unique email domains: %s" % (len(domains), domains))

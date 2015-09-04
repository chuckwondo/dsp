import advanced_python_regex as apr
from collections import defaultdict

faculty = apr.read_faculty()

# Q6

faculty_dict = defaultdict(list)

for prof in faculty:
    surname = prof['name'].split()[-1]
    faculty_dict[surname].append([prof['degree'], prof['title'], prof['email']])

print(faculty_dict.items()[:3])

# Q7

prof_dict = {}

for prof in faculty:
    names = prof['name'].split()
    fname, surname = names[0], names[-1]
    prof_dict[(fname, surname)] = [prof['degree'], prof['title'], prof['email']]

print(prof_dict.items()[:3])

# Q8

print(sorted(prof_dict.items(), key=lambda t: t[0][1])[:3])

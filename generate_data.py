#!/usr/bin/python3.5

import json
import random
import string

#
# script to generate random data for review_dahsboard
#

release = "Trunk"
number_of_builds = 20
number_of_bugs = 40
data = {}

########################
def RandomSentence(words):
    sentence = ""

    for _ in range(words):
        word = ''.join([random.choice(string.ascii_letters) for _ in range(random.randint(1, 11))])
        sentence = sentence + word + ' '

    return(sentence)

###
def generate_parfait(rel, builds):

    print("Generating parfait table data")

    data['parfait'] = []
    for i in range(1, builds+1):
        data['parfait'].append({
            'build_id': i,
            'release': release,
            'verified': random.randint(800, 850),
            'unverified': random.randint(2000, 2200),
            'open_bugs': random.randint(50, 100),
            'new_bugs': random.randint(0, 20),
            'fixed_bugs': random.randint(0, 20)
        })

###
def generate_qualys(rel, builds):

    print("Generating qualys table data")

    data['qualys'] = []
    for i in range(1, builds+1):
        data['qualys'].append({
            'build_id': i,
            'release': release,
            'new_bugs': random.randint(0, 10),
            'comments': RandomSentence(random.randint(1, 10))
        })

####
def generate_bugs(bugs):

    print("Generating bugs table data")
    programmers = ['Jakub', 'Petr', 'Ales', 'Honza']
    data['bugs'] = []
    for i in range(1, bugs+1):
        data['bugs'].append({
            'build_id': 1000000 + i,
            'severity': random.randint(1, 5),
            'status': random.randint(11, 88),
            'subject': RandomSentence(random.randint(1, 10)),
            'asignee': programmers[random.randrange(len(programmers))],
            'tags': RandomSentence(random.randint(0, 3))
        })

####
def generate_open_bugs_trend(rel, builds):

    print("Generating open_bugs_trend table data")

    data['open_bugs_trend'] = []
    for i in range(1, builds+1):
        data['open_bugs_trend'].append({
            'build_id': i,
            'release': release,
            'open_bugs': random.randint(60, 90)
        })

###############################################################################

#
# main
######
if __name__ == '__main__':

    generate_parfait(release, number_of_builds)
    generate_qualys(release, number_of_builds)
    generate_bugs(number_of_bugs)
    generate_open_bugs_trend(release, number_of_builds)

    with open('reviewboard_data.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)

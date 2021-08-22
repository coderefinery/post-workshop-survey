#!/usr/bin/env python3
import sys
import csv

csvfile = sys.argv[1]
processed_datafile = csvfile.replace('.csv','_processed.csv')

questions = [
    "Which workshop did you attend?",
    "What is your current position?",
    "Other",
    "Version control",
    "Automated testing",
    "Travis CI",
    "Code coverage analysis",
    "Jupyter Notebooks",
    "CMake",
    "Integrated development environments",
    "Code review",
    "Read the Docs or GitHub/GitLab/BitBucket Pages",
    "Reusable",
    "Reproducible",
    "Modular",
    "Documented",
    "Has it become easier for you to collaborate on software development with your colleagues and collaborators?",
    "Have you introduced one or more of your colleagues to new tools or practices as a result of the workshop?"
    ]

# if 2017 survey then split "Read the Docs or GitHub/GitLab/BitBucket Pages"
# into "Read the docs" and "GitHub/GitLab/BitBucket Pages"

freeform_q1 = "What else has changed in how you write code for your research after attending a CodeRefinery workshop?"
freeform_q2 = "Do you have any recommendations on how we should change the CodeRefinery curriculum?"
freeform_q3 = "If you want to receive a hand-written thank you postcard from a random location, please enter your name and postal address below."

what_else_changed = []
recommendations = []
addresses = []

with open(csvfile) as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row[freeform_q1] == '':
            what_else_changed.append(row[freeform_q1])
        if not row[freeform_q2] == '':
            recommendations.append(row[freeform_q2])
        if not row[freeform_q3] == '':
            addresses.append(row[freeform_q3])

with open('postcard_addresses.txt','w') as f:
    for i in addresses:
        f.write(i+'\n--------------------------------\n')

with open('what_else_changed.txt','w') as f:
    for i in what_else_changed:
        f.write(i+'\n--------------------------------\n')

with open('other_recommendations.txt','w') as f:
    for i in recommendations:
        f.write(i+'\n--------------------------------\n')

# now the tools usage and yes/no questions
with open(csvfile) as f:
    reader = csv.DictReader(f)
    with open(processed_datafile,'w') as fout:
        writer = csv.DictWriter(fout, fieldnames=questions)
        writer.writeheader()
        for row in reader:
            for q in questions:
                if q in row.keys():
                    row_out = {key:row[key] for key in questions}
            writer.writerow(row_out)

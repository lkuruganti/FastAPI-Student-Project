import pandas as pd 
import random
"""
PGROUP = ['BPC', 'MPC']
GRADE = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12']
GROUP = ['Biology', 'Math', 'Physics', 'English', 'History', 'Hindi', 'Marathi']
LOCATION = ['Chennai', 'Banglore', 'Delhi', 'Pune', 'Mumbai', 'Jalgaon']
SUBJECT = ['Biology1', 'Math2', 'Physics1', 'English2', 'History1', 'Hindi2', 'Marathi3']


random.shuffle(PGROUP)
p_group = PGROUP[0]
print("fffffffffffffffff", p_group)

df = pd.read_csv('student.csv')

new_df = df.fillna({
    'Grade': random.choice(GRADE),
    'Pgroup': random.choice(PGROUP),
    'Group': random.choice(GROUP),
    'Subject': random.choice(SUBJECT),
    'Total students': 35,
    'Buffer': 987654321,
    'Virtual class/Physical': 'TRUE', 
    'Student': 'S4',
    'Marks': 80,
    'Location': loc,
})

print(new_df)
"""

data = []

chart_analysis = []

student_list = ["S1", "S2", "S3"]

data.append(student_list)

loc_data = {}

loc_data["hello"] = "world"
loc_data["bye"] = "goodbye"

chart_analysis.append(loc_data)


data.append(chart_analysis)

print(data[0])

print(data)








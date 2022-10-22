import csv
from os import path


had = [["first_name", "second_name", "Grade", "Faculty"],
        ['Harry', 'Potter', '1', 'Gryffindor'],
        ['Ronald', 'Weasley', '1', 'Gryffindor'],
        ['Hermione', 'Granger', '1', 'Gryffindor'],
        ['Draco', 'Malfoy', '1', 'Slytherin']]
with open('students.csv', 'a') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(had)

def get_s():
    students = []
    header = {'name': '', 'surname': '', 'grade': '', 'faculty': ''}
    for f in header:
        answer = input(f"Enter student's {f}: ")
        students.append(answer)
    with open('students.csv', 'a') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(students)
    return students


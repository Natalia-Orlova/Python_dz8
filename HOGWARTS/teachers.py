import csv


had = [["first_name", "second_name", "subject"],
        ['Severus', 'Snape', 'Potions'],
        ['Minerva', 'McGonagall', 'Transfiguration'],
        ['Sybill', 'Trelawney', 'Divination']]
with open('teachers.csv', 'a') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(had)

def get_t():
    teachers = []
    header = {'name': '', 'surname': '', 'subject': ''}
    for f in header:
        answer = input(f"Enter student's {f}: ")
        teachers.append(answer)
    with open('students.csv', 'a') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(teachers)
    return teachers
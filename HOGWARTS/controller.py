import sys
import csv
import menu as m
import logger as log 
import teachers as te
import students as st

def Hogwarts():
    while True:
        m.main()
        c = input("Enter choice: ")
        if c == '0':
            break
        if c == '1':
            log.logger("Information about faculties")
            m.faculties()
            c = input("Enter choice: ")
            
            if c == '1':
                log.logger("Information about Gryffindor")
                g = open('Gryffindor.txt', 'r', encoding='utf-8')
                print(*g)
                continue

            elif c == '2':
                log.logger("Information about Hufflepuff")
                h = open('Hufflepuff.txt', 'r', encoding='utf-8')
                print(*h)
                continue

            elif c == '3':
                log.logger("Information about Ravenclaw")
                r = open('Ravenclaw.txt', 'r', encoding='utf-8')
                print(*r)
                continue

            elif c == '4':
                log.logger("Information about Slytherin")
                s = open('Slytherin.txt', 'r', encoding='utf-8')
                print(*s)
                continue

            else:
                log.logger("Invalid value entered")
                print ("Invalid value")
                continue

        elif c == '2':
            
            m.teachers()
            c = input("Enter choice: ")
            
            if c == '1':
                log.logger("Information about teachers")
                with open('teachers.csv', 'r') as File:
                    reader = csv.reader(File)
                    for row in reader:
                        print (row)
                continue

            elif c == '2':
                log.logger("Addition a new teacher")
                te.get_t()

            elif c == '0':
                continue

            else:
                log.logger("Invalid value entered")
                print ("Invalid value")
                continue

        elif c == '3':
            m.students()
            c = input("Enter choice: ")

            if c == '1':
                log.logger("Information about students")
                with open('students.csv', 'r') as File:
                        reader = csv.reader(File)
                        for row in reader:
                            print (row)
                continue
            
            elif c =='2':
                log.logger("Addition a new student")
                st.get_s()

            elif c == '0':
                continue

            else:
                log.logger("Invalid value entered")
                print ("Invalid value")
                continue
        
        else:
                log.logger("Invalid value entered")
                print ("Invalid value")
                continue
        return
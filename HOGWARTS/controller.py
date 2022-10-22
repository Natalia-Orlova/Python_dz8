import csv
import menu as m


while True:
    m.main()
    c = input("Enter choice: ")
    
    if c == '0':
        break
    
    if c == '1':
        m.faculties()
        c = input("Enter choice: ")
        if c == '1':
            print("Information about Gryffindor")
        if c == '2':
            print("Information about Hufflepuff")
        if c == '3':
            print("Information about Ravenclaw")
        if c == '4':
            print("Information about Slytherin")

    if c == '2':
        print("Our Teachers")
    if c == '3':

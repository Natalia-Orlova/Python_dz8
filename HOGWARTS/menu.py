def main ():
    print('~' * 70)
    hello = 'Welcome to Hogwarts School of Wizardcraft and Wizardy!'
    print ("\033[1m\033[31m\033[43m{}\033[0m".format(hello.center(len(hello)+15)))
    print('~' * 70)
    print('1. Faculties \n2. Teachers\n3. Students\n0. EXIT\n')


def faculties():
    print("1. \033[31m{}\033[0m".format('Gryffindor'))
    print("2. \033[33m{}\033[0m".format('Hufflepuff'))
    print("3. \033[34m{}\033[0m".format('Ravenclaw'))
    print("4. \033[32m{}\033[0m".format('Slytherin'))
    print("0. PREVIOUS MENU\n")
    

def teachers():
    print("1. Open information\n2. Add new teacher")
    print("0. PREVIOUS MENU\n")


def students():
    print("1. Open information\n2. Add new student")
    print("0. PREVIOUS MENU\n")






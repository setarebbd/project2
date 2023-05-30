import os
PATH = "C:/Users/maryam/Desktop/DATABASE.txt"


def validation():
    if not os.path.exists(PATH):
        f = open(PATH, "w+")
        f.write('')


def add(name, number):
    validation()
    f = open(PATH, "a+")
    new_phone = name+':'+number+'\n'
    f.write(new_phone)
    f.close()


def search(name):
    validation()
    f = open(PATH, "r")
    for line in f.readlines():
        if name == line.split(":")[0]:
            print(name+':'+line.split(":")[1])


def delete(name):
    validation()
    f = open(PATH, "r")
    new_database = ""
    for line in f.readlines():
        if not name == line.split(":")[0]:
            new_database += line
    f.close()
    f = open(PATH, 'w')
    f.write(new_database)


def show_all():
    validation()
    f = open(PATH, "r")
    database = ''
    database = f.read()
    f.close()
    print(database)


choice = 1
while choice != 0:
    print('1=add user\n2=search\n3= delete\n4=show all\n0=exit')
    choice = int(input('enter your choice: '))
    os.system('cls')
    if choice == 1:
        name = input('enter name: ')
        number = input('enter number: ')
        add(name, number)
    elif choice == 2:
        name = input('enter name: ')
        search(name)
    elif choice == 3:
        name = input('enter name: ')
        delete(name)
    elif choice == 4:
        show_all()

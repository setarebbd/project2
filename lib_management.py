import pickle
import os
PATH = "C:/Users/maryam/Desktop/"


def check_validation():
    if not os.path.exists(PATH+'user.dat'):
        f = open(PATH+'user.dat', 'wb')
        users_dict = {}
        pickle.dump(users_dict, f)
        f.close()
    if not os.path.exists(PATH+'book.dat'):
        f = open(PATH+'book.dat', 'wb')
        books_dict = {}
        pickle.dump(books_dict, f)
        f.close()
    if not os.path.exists(PATH+'borrow.dat'):
        f = open(PATH+'borrow.dat', 'wb')
        borrows_dict = {}
        pickle.dump(borrows_dict, f)
        f.close()


def add_user(name, family, father_name, nationality_code, birthday):
    check_validation()
    f = open(PATH+'user.dat', 'rb')
    users_dict = pickle.load(f)
    f.close()
    user_id = len(users_dict)
    users_dict[user_id] = [name, family,
                           father_name, nationality_code, birthday]
    f = open(PATH+'user.dat', 'wb')
    pickle.dump(users_dict, f)
    f.close()
    print('welcome! your user id is : ',  user_id)


def add_book(title, author, subject, year):
    check_validation()
    f = open(PATH+'book.dat', 'rb')
    books_dict = pickle.load(f)
    f.close()
    book_id = len(books_dict)
    books_dict[title] = [author, subject, year]
    f = open(PATH+'book.dat', 'wb')
    pickle.dump(books_dict, f)
    f.close()


def search(title):
    check_validation()
    f = open(PATH+'book.dat', 'rb')
    books_dict = pickle.load(f)
    f.close()
    print(books_dict[title])


def borrow(user_id, title):
    check_validation()
    f = open(PATH+'borrow.dat', 'rb')
    borrows_dict = pickle.load(f)
    f.close()
    borrow_id = len(borrows_dict)
    borrows_dict[user_id] = [title]
    f = open(PATH+'borrow.dat', 'wb')
    pickle.dump(borrows_dict, f)
    f.close()


def show_all():
    check_validation()
    f = open(PATH+'user.dat', 'rb')
    users_dict = pickle.load(f)
    f.close()
    f = open(PATH+'book.dat', 'rb')
    books_dict = pickle.load(f)
    f.close()
    f = open(PATH+'borrow.dat', 'rb')
    borrows_dict = pickle.load(f)
    f.close()
    print(users_dict)
    print('----')
    print(books_dict)
    print('----')
    print(borrows_dict)


choice = 1
while choice != 0:
    print('1=add user\n2=add book\n3=search\n4=borrow\n5=show all\n0=exit')
    choice = int(input("entar your choice: "))

    if choice == 1:
        name = input('enter name: ')
        family = input('enter family: ')
        father_name = input('enter father name: ')
        nationality_code = input('enter nationality code: ')
        birthday = input('enter birthday: ')
        add_user(name, family, father_name, nationality_code, birthday)

    elif choice == 2:
        title = input('enter title: ')
        author = input('enter author: ')
        subject = input('enter subject:')
        year = input('enter year: ')
        add_book(title, author, subject, year)

    elif choice == 3:
        title = input('enter title: ')
        search(title)

    elif choice == 4:
        user_id = input('user id: ')
        title = input('enter title: ')
        borrow(user_id, title)

    elif choice == 5:
        show_all()

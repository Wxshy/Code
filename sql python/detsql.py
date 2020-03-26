import sqlite3

conn = sqlite3.connect('Detentions.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Students(Student_ID REAL not null primary key, LastName text, FirstName text)')
    c.execute('CREATE TABLE IF NOT EXISTS Teachers(Teacher_ID REAL NOT NULL PRIMARY KEY, name TEXT, subject TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Detention(Detention_ID REAL NOT NULL, Student_ID REAL NOT NULL, Teacher_ID REAL NOT NULL, Timee text, Datee text, Room text, foreign key(Student_ID) references Students(Student_ID), foreign key(Teacher_ID) references Teachers(Teacher_ID))')

def data_entry():
    while True:
        try:
            print('What table would you like to insert data into?')
            choice = int(input('1. Students \n2. Teachers \n3. Detention \n>>> '))
            break
        except ValueError:
            print('Please enter either 1, 2 or 3')
        except choice > 3:
            print('Please enter either 1, 2 or 3')

    if choice == 1:
        sid = int(input('Student_ID: '))
        fname = input('FirstName: ')
        lname = input('LastName: ')
        c.execute("INSERT INTO Students(Student_ID, LastName, FirstName) VALUES (?,?,?) ", (sid, lname, fname))
        
    elif choice == 2:
        tid = int(input('Teacher_ID: '))
        name = input('Name: ')
        subject = input('Subject: ')
        c.execute('INSERT INTO Teachers(Teacher_ID, name, subject) VALUES (?,?,?)', (tid, name, subject))
    elif choice == 3:
        did = int(input('Detention_ID: '))
        sid = int(input('Student_ID: '))
        tid = int(input('Teacher_ID: '))    
        time = input('Time (HH:MM:SS): ')
        date = input('Date (DD-MM-YYYY): ')
        room = input('Room: ')

    conn.commit()
    c.close()
    conn.close()


def readDb():
    while True:
        try:
            print('What table would you like to read from?')
            choice = int(input('1. Students \n2. Teachers \n3. Detention \n>>> '))
        except ValueError:
            print('Please enter either 1, 2 or 3')
        except choice > 3:
            print('Please enter either 1, 2 or 3')

        if choice == 1:
            c.execute('SELECT * FROM Students')
            for row in c.fetchall():
                print(row)
            break
        elif choice == 2:
            c.execute('SELECT * FROM Teachers')
            for row in c.fetchall():
                print(row)
            break
        elif choice == 3:
            c.execute('SELECT * FROM Detention')
            for row in c.fetchall():
                print(row)
            break
    
    

while True:
    try:
        print('---MENU---')
        choice = int(input('1. Input \n2. Read \n3. Quit \n>>> '))
        break
    except ValueError:
        print('Please enter either 1, 2 or 3')
    except choice > 3:
        print('Please enter either 1, 2 or 3')

if choice == 1:
    data_entry()
    break
elif choice == 2:
    readDb()
    break
elif choice == 3:
    quit()

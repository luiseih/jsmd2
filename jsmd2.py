#!/usr/bin/python3

# TODO:
#
# Default app to see documents stored in
# database.
#
# Create independent file modules for
# working with business, job, application,
# resumes, cover letters (maybe?).

import os
import time
import sqlite3
import configparser
from pathlib import Path

def main():
    # define clear screen function
    def clear():
        # for windows
        if os.name == 'nt':
            os.system('cls')
        # for mac and linux
        else:
            os.system('clear')
        return

    def configuration_check():
        config = configparser.ConfigParser()
        if os.path.isfile('jsmd2.conf'):
            config.read('jsmd2.conf')
            database_location = config['DEFAULT']['DatabaseLocation']
            database_name = config['DEFAULT']['DatabaseName']
        else:
            database_location, database_name = Menu.configuration()
            config['DEFAULT'] = {'DatabaseLocation': database_location,
                                 'DatabaseName': database_name}
            with open('jsmd2.conf', 'w') as configfile:
                config.write(configfile)
        conn, c = Database.connect(database_location, database_name)
        Database.init(conn, c)
        return conn, c

    class Database:
        def connect(database_location, database_name):
            os.chdir(database_location)
            conn = sqlite3.connect(database_name)
            c = conn.cursor()
            return conn, c

        def init(conn, c):
            c.executescript("""
            DROP TABLE IF EXISTS company;
            DROP TABLE IF EXISTS job;
            DROP TABLE IF EXISTS application;
            DROP TABLE IF EXISTS cover_letter;
            DROP TABLE IF EXISTS resume;
            DROP TABLE IF EXISTS status;

            CREATE TABLE company(
            id INTEGER PRIMARY KEY NOT NULL,
            updated_on TEXT NOT NULL,
            name TEXT NOT NULL,
            address1 TEXT,
            address2 TEXT,
            city TEXT,
            state TEXT DEFAULT 'VIC' NOT NULL,
            postal_code INTEGER,
            country TEXT DEFAULT 'AUSTRALIA' NOT NULL);

            CREATE TABLE job(
            id INTEGER PRIMARY KEY NOT NULL,
            updated_on TEXT NOT NULL,
            from_company INTEGER NOT NULL,
            name TEXT NOT NULL,
            requirements BLOB NOT NULL,
            FOREIGN KEY(from_company) REFERENCES company(id));

            CREATE TABLE application(
            id INTEGER PRIMARY KEY NOT NULL,
            updated_on TEXT NOT NULL,
            job INTEGER NOT NULL,
            sent INTEGER NOT NULL,
            cover_letter INTEGER NOT NULL,
            resume INTEGER NOT NULL,
            status INTEGER NOT NULL,
            notes TEXT NOT NULL,
            FOREIGN KEY(job) REFERENCES job(id),
            FOREIGN KEY(cover_letter) REFERENCES cover_letter(id),
            FOREIGN KEY(resume) REFERENCES resume(id),
            FOREIGN KEY(status) REFERENCES status(id));

            CREATE TABLE cover_letter(
            id INTEGER PRIMARY KEY NOT NULL,
            updated_on TEXT NOT NULL,
            name TEXT NOT NULL,
            document BLOB NOT NULL);

            CREATE TABLE resume(
            id INTEGER PRIMARY KEY NOT NULL,
            updated_on TEXT NOT NULL,
            name TEXT NOT NULL,
            document BLOB NOT NULL);

            CREATE TABLE status(
            id INTEGER PRIMARY KEY NOT NULL,
            status TEXT NOT NULL);
            """)
            return

        def read():
            pass
        def write():
            pass


    class Application:
        def read():
            pass

        def write():
            pass

    class Company:
        def read():
            pass

        def write():
            pass

    class Cover_letter:
        def read():
            pass
        def write():
            pass


    class Job:
        def read():
            pass
        def write():
            pass

    class Menu:
        def header():
            clear()
            print()
            print("*"*12,"JSMD2","*"*12)
            print()
            return

        def configuration():
            Menu.header()
            print ("Database Configuration")
            print()
            print ("*"*30)
            database_location = input("Enter sqlite3 database location (ENTER for current folder): ")
            if database_location == "":
                database_location = os.getcwd()
            database_name = input("Enter sqlite3 database name (ENTER for 'jsmd2.db'): ")
            if database_name == "":
                database_name = "jsmd2.db"
            return database_location, database_name
    
        def main():
            Menu.header()
            print("Main Menu")
            print()
            print ("*"*30)
            print("1. Work with companies.")
            print("2. Work with job positions.")
            print("3. Work with job applications.")
            print("4. Work with resumes.")
            print("5. Work with cover letters.")
            print("6. Status options.")
            print("7. Exit.")
            print()
            choice = input("What would you like to do? ")
            if choice == "1":
                Menu.companies()
            elif choice == "2":
                Menu.jobs()
            elif choice == "3":
                Menu.applications()
            elif choice == "4":
                Menu.resumes()
            elif choice == "5":
                Menu.cover_letters()
            elif choice == "6":
                Menu.status()
            elif choice == "7":
                Menu.goodbye()
            else:
                Menu.invalid_input()
                Menu.main()
            return

        def companies():
            Menu.header()
            print("Companies")
            print()
            print ("*"*30)
            print("1. Add a new company.")
            print("2. Modify a company.")
            print("3. Delete a company.")
            print("4. List companies.")
            print("5. Search companies.")
            print("6. Go to main menu.")
            print("7. Exit.")
            print()
            choice = input("What would you like to do? ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                Menu.main()
            elif choice == "7":
                Menu.goodbye()
            else:
                Menu.invalid_output()
                Menu.companies()
            return

        def jobs():
            pass

        def applications():
            pass

        def resumes():
            pass

        def cover_letters():
            pass

        def status():
            Menu.header()
            print("Status options")
            print()
            print("*"*30)
            print()
            print("Current available options are:")
            Status.read()
            print()
            print("*"*30)
            print("1. Add a new option.")
            print("2. Modify a previous option.")
            print("3. Delete an option.")
            print("4. Go to main menu.")
            print("5. Exit.")
            print()
            choice = input("What would you like to do? ")
            if choice == "1":
                status = input("Type the new status: "),
                Status.write(status)
                Menu.status()
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                Menu.main()
            elif choice == "5":
                Menu.goodbye()
            else:
                Menu.invalid_input()
                Menu.status()
            return

        def invalid_input():
            print()
            print("That is not a valid option. Please try again.")
            time.sleep(2)
            return

        def goodbye():
            conn.close()
            print()
            print("Fingers crossed. Good luck!")
            print()
            return

    class Resume:
        def read():
            pass
        def write():
            pass

    class Status:
        def read():
            for row in conn.execute('SELECT * FROM status'):
                print(row)
            return

        def write(status):
            conn.execute('INSERT INTO status(status) VALUES(?)', status)
            conn.commit()
            return


    conn, c = Configuration.check()
    print("SQLite version",sqlite3.sqlite_version)
    time.sleep(2)
    Menu.main()

if __name__ == '__main__':
    main()

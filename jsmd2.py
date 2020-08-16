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
            database_location, database_name = menu_configuration()
            config['DEFAULT'] = {'DatabaseLocation': database_location,
                                 'DatabaseName': database_name}
            with open('jsmd2.conf', 'w') as configfile:
                config.write(configfile)
            os.chdir(database_location)
            conn = sqlite3.connect(database_name)
            create_database(conn)
        return database_location, database_name

    def create_database(conn):
        conn.executescript("""
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

    def application_read():
        pass

    def application_write():
        pass

    def company_read():
        pass
    
    def company_write():
        pass

    def cover_letter_read():
        pass

    def cover_letter_write():
        pass

    def job_read():
        pass
    
    def job_write():
        pass

### Menu Section ###
    def menu_header():
        clear()
        print()
        print("*"*12,"JSMD2","*"*12)
        print()
        return

    def menu_configuration():
        menu_header()
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
    
    def menu_main():
        menu_header()
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
            menu_companies()
        elif choice == "2":
            menu_jobs()
        elif choice == "3":
            menu_applications()
        elif choice == "4":
            menu_resumes()
        elif choice == "5":
            menu_cover_letters()
        elif choice == "6":
            menu_status()
        elif choice == "7":
            menu_goodbye()
        else:
            menu_invalid_input()
            menu_main()
        return

    def menu_companies():
        Menu_header()
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
            menu_main()
        elif choice == "7":
            menu_goodbye()
        else:
            menu_invalid_output()
            menu_companies()
        return

    def menu_jobs():
        pass

    def menu_applications():
        pass

    def menu_resumes():
        pass

    def menu_cover_letters():
        pass

    def menu_status():
        menu_header()
        print("Status options")
        print()
        print("*"*30)
        print()
        print("Current available options are:")
        status_read()
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
            status_write(status)
            menu_status()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            menu_main()
        elif choice == "5":
            menu_goodbye()
        else:
            menu_invalid_input()
            menu_status()
        return

    def menu_invalid_input():
        print()
        print("That is not a valid option. Please try again.")
        time.sleep(2)
        return

    def menu_goodbye():
        print()
        print("Fingers crossed. Good luck!")
        print()
        return

    class Resume:
        def read():
            pass
        def write():
            pass

    def status_read():
        for row in conn.execute('SELECT * FROM status;'):
            print(row)
        return

    def status_write(status):
        conn.execute('INSERT INTO status(status) VALUES(?);', status)
        conn.commit()
        return

    location, db = configuration_check()
    os.chdir(location)
    conn = sqlite3.connect(db)
    print("SQLite version",sqlite3.sqlite_version)
    time.sleep(1)
    menu_main()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

#  vim: set ts=8 sw=4 tw=110 et :

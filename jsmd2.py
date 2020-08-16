#!/usr/bin/python3

'''
JSMD2 is an application to manage job applications.
It acts as a front end for SQLite3.
'''

__author__ = "Luis E. I. Herrera"
__copyright__ = "MIT License 2020"

# TODO:
#
# Create menus for working with job,
# application, resumes, and cover letters.
#
# Default app to see documents stored in
# database.
#
# This is getting really long.
# Create independent file modules for
# working with business, job, application,
# resumes, cover letters (maybe?).

import os
import time
import sqlite3
import datetime
import configparser


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

        if os.path.isfile(database_name):
            connection = sqlite3.connect(database_name)
        else:
            connection = sqlite3.connect(database_name)
            create_database(connection)
        return connection

    def create_database(connection):
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

    # Menu Section
    def menu_header():
        clear()
        print()
        print("*" * 12, "JSMD2", "*" * 12)
        print()
        return

    def menu_configuration():
        menu_header()
        print("Database Configuration")
        print()
        print("*" * 30)
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
        print("*" * 30)
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
        menu_header()
        print("Companies")
        print()
        print("*" * 30)
        print()
        print("Current companies are:")
        company_read()
        print()
        print("*" * 30)
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
            name = input("What is the company name? ")
            address1 = input("What is the company address1? ")
            address2 = input("What is the company address2? ")
            city = input("What is the company city? ")
            state = input("What is the company state? ")
            if state == "":
                state = "VIC"
            postal_code = input("What is the company post code? ")
            country = input("What is the company country? ")
            if country == "":
                country = "AUSTRALIA"
            company_add(name, address1, address2, city, state, postal_code, country)
            menu_companies()
        elif choice == "2":
            modify_company = input("What company would you like to modify? ")
            cur = conn.cursor()
            cur.execute('SELECT * FROM company WHERE rowid=?', (modify_company,))
            old_company = cur.fetchone()
            print("What is the company name (", old_company[2], ")? ")
            name = input()
            if name == "":
                name = old_company[2]
            print("What is the company address1 (", old_company[3], ")? ")
            address1 = input()
            if address1 == "":
                address1 = old_company[3]
            print("What is the company address2 (", old_company[4], ")? ")
            address2 = input()
            if address2 == "":
                address2 = old_company[4]
            print("What is the company city (", old_company[5], ")? ")
            city = input()
            if city == "":
                city = old_company[5]
            print("What is the company state (", old_company[6], ")? ")
            state = input()
            if state == "":
                state = old_company[6]
            print("What is the company post code (", old_company[7], ")? ")
            postal_code = input()
            if postal_code == "":
                postal_code = old_company[7]
            print("What is the company country (", old_company[8], ")? ")
            country = input()
            if country == "":
                country = old_company[8]
            company_modify(modify_company, name, address1, address2, city, state, postal_code, country)
            menu_companies()
        elif choice == "3":
            delete_company = input("Company to delete? ")
            company_delete(delete_company)
            menu_companies()
        elif choice == "4":
            how_many = input("Last how many entries? ")
            company_last_entries(how_many)
            menu_companies()
        elif choice == "5":
            search_company = input("Company to search for? ")
            company_search(search_company)
            menu_companies()
        elif choice == "6":
            menu_main()
        elif choice == "7":
            menu_goodbye()
        else:
            menu_invalid_input()
            menu_companies()
        return

    # Company menu header
    def company_read():
        for row in conn.execute('SELECT * FROM company;'):
            print(row)
        return

    # Company menu option 1
    def company_add(name, address1, address2, city, state, postal_code, country):
        updated_on = datetime.datetime.now().isoformat()
        conn.execute('INSERT INTO company \
                (updated_on,name,address1,address2,city,state,postal_code,country) \
                VALUES(?,?,?,?,?,?,?,?);',
                     (updated_on, name, address1, address2, city, state, postal_code, country))
        conn.commit()
        return

    # Company menu option 2
    def company_modify(modify_company, name, address1, address2, city, state, postal_code, country):
        updated_on = datetime.datetime.now().isoformat()
        conn.execute('UPDATE company SET \
        updated_on=?,name=?,address1=?,address2=?,city=?,state=?,postal_code=?,country=? WHERE \
        rowid=?;', (updated_on, name, address1, address2, city, state, postal_code, country, modify_company))
        conn.commit()
        return

    # Company menu option 3
    def company_delete(delete_company):
        conn.execute('DELETE FROM company WHERE rowid=?;', delete_company)
        conn.commit()
        return

    # Company menu option 4
    def company_last_entries(how_many):
        for row in conn.execute('SELECT * FROM company ORDER BY rowid DESC LIMIT ?;', how_many):
            print(row)
        input("Press ENTER to continue...")
        return

    # Company menu option 5
    def company_search(search_company):
        for row in conn.execute("SELECT * FROM company WHERE name LIKE ?;", ('%' + search_company + '%',)):
            print(row)
        input("Press ENTER to continue...")
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
        print("*" * 30)
        print()
        print("Current available options are:")
        status_read()
        print()
        print("*" * 30)
        print("1. Add a new option.")
        print("2. Modify a previous option.")
        print("3. Delete an option.")
        print("4. Go to main menu.")
        print("5. Exit.")
        print()
        choice = input("What would you like to do? ")
        if choice == "1":
            status = input("Type the new status: "),
            status_write_new(status)
            menu_status()
        elif choice == "2":
            old_status = input("Which option would you like to change? ")
            new_status = input("What should the new option be? ")
            status_replace(old_status, new_status)
            menu_status()
        elif choice == "3":
            remove_status = input("Which option would you like to remove? ")
            status_remove(remove_status)
            menu_status()
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
        def read(self):
            pass

        def write(self):
            pass

    # Status menu header
    def status_read():
        for row in conn.execute('SELECT * FROM status;'):
            print(row)
        return

    # Status menu option 1
    def status_write_new(status):
        conn.execute('INSERT INTO status(status) VALUES(?);', status)
        conn.commit()
        return

    # Status menu option 2
    def status_replace(old_status, new_status):
        conn.execute('UPDATE status SET status=? WHERE rowid=?;', (new_status, old_status))
        conn.commit()
        return

    # Status menu option 3
    def status_remove(remove_status):
        conn.execute('DELETE FROM status WHERE rowid=?;', remove_status)
        conn.commit()
        return

    conn = configuration_check()
    print("SQLite version", sqlite3.sqlite_version)
    time.sleep(1)
    menu_main()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

#  vim: set ts=8 sw=4 tw=110 et :

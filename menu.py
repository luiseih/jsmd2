#!/usr/bin/env python3

import os
import time
import status
import company
import job
import application
import cover_letter
import resume


def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux
    else:
        os.system('clear')
    return


def header():
    clear()
    print()
    print("*" * 12, "JSMD2", "*" * 12)
    print()
    return


def configuration():
    header()
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


def main(db):
    header()
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
        companies(db)
    elif choice == "2":
        jobs(db)
    elif choice == "3":
        applications(db)
    elif choice == "4":
        resumes(db)
    elif choice == "5":
        cover_letters(db)
    elif choice == "6":
        statuses(db)
    elif choice == "7":
        goodbye(db)
    else:
        invalid_input()
        main(db)


def companies(db):
    header()
    print("Companies")
    print()
    print("*" * 30)
    print()
    print("Current companies are:")
    company.read()
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
        company.add(name, address1, address2, city, state, postal_code, country)
        companies(db)
    elif choice == "2":
        modify_company = input("What company would you like to modify? ")
        cur = db.cursor()
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
        company.modify(modify_company, name, address1, address2, city, state, postal_code, country)
        companies(db)
    elif choice == "3":
        delete_company = input("Company to delete? ")
        company.delete(delete_company)
        companies(db)
    elif choice == "4":
        how_many = input("Last how many entries? ")
        company.last_entries(how_many)
        companies(db)
    elif choice == "5":
        search_company = input("Company to search for? ")
        company.search(search_company)
        companies(db)
    elif choice == "6":
        main(db)
    elif choice == "7":
        goodbye(db)
    else:
        invalid_input()
        companies(db)
    return


def statuses(db):
    header()
    print("Status options")
    print()
    print("*" * 30)
    print()
    print("Current available options are:")
    status.read(db)
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
        status_new = input("Type the new status: "),
        status.write_new(db, status_new)
        statuses(db)
    elif choice == "2":
        old_status = input("Which option would you like to change? ")
        new_status = input("What should the new option be? ")
        status.replace(db, old_status, new_status)
        statuses(db)
    elif choice == "3":
        remove_status = input("Which option would you like to remove? ")
        status.remove(db, remove_status)
        statuses(db)
    elif choice == "4":
        main(db)
    elif choice == "5":
        goodbye(db)
    else:
        invalid_input()
        statuses(db)


def invalid_input():
    print()
    print("That is not a valid option. Please try again.")
    time.sleep(2)


def goodbye(db):
    db.dbconnect.close()
    print()
    print("Fingers crossed. Good luck!")
    print()


def jobs(db):
    pass


def applications(db):
    pass


def resumes(db):
    pass


def cover_letters(db):
    pass
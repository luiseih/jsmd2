#!/usr/bin/env python3

import os
import time
import status
import company
import datetime
import database
import job
import PySimpleGUI as sg
import application
import cover_letter
import resume

sg.theme('Dark Blue 3')  # please make your windows colorful


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



def configuration(current_dir):
    layout = [[sg.Text('Select folder for database')],
              [sg.Input(current_dir), sg.FolderBrowse()],
              [sg.Text('Select database name')],
              [sg.Input("jsmd2.db")],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Database Location', layout)
    event, values = window.read()
    window.close()
    database_location = values[0]
    database_name = values[1]
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
    company.read(db)
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
        updated_on = datetime.datetime.now().isoformat()
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
        company.add(db, updated_on, name, address1, address2, city, state,
                    postal_code, country)
        companies(db)
    elif choice == "2":
        modify_company = input("What company would you like to modify? ")
        old_company = company.get_one(db, modify_company)
        print("What is the new company name (", old_company[2], ")? \
        (ENTER to leave unchanged)")
        name = input("> ")
        if name == "":
            name = old_company[2]
        print("What is the new company address1 (", old_company[3], ")? \
               (ENTER to leave unchanged)")
        address1 = input("> ")
        if address1 == "":
            address1 = old_company[3]
        print("What is the new company address2 (", old_company[4], ")? \
               (ENTER to leave unchanged)")
        address2 = input("> ")
        if address2 == "":
            address2 = old_company[4]
        print("What is the new company city (", old_company[5], ")? \
               (ENTER to leave unchanged)")
        city = input("> ")
        if city == "":
            city = old_company[5]
        print("What is the new company state (", old_company[6], ")? \
               (ENTER to leave unchanged)")
        state = input("> ")
        if state == "":
            state = old_company[6]
        print("What is the new company post code (", old_company[7], ")? \
               (ENTER to leave unchanged)")
        postal_code = input()
        if postal_code == "":
            postal_code = old_company[7]
        print("What is the new company country (", old_company[8], ")? \
               (ENTER to leave unchanged)")
        country = input()
        if country == "":
            country = old_company[8]
        company.modify(db, modify_company, name, address1, address2, city,
                       state, postal_code, country)
        companies(db)
    elif choice == "3":
        delete_company = input("Company to delete? ")
        company.delete(db, delete_company)
        companies(db)
    elif choice == "4":
        how_many = input("Last how many entries? ")
        company.last_entries(db, how_many)
        input("Press ENTER to continue...")
        companies(db)
    elif choice == "5":
        search_company = input("Company to search for? ")
        company.search(db, search_company)
        input("Press ENTER to continue...")
        companies(db)
    elif choice == "6":
        main(db)
    elif choice == "7":
        goodbye(db)
    else:
        invalid_input()
        companies(db)


def jobs(db):
    header()
    print("Jobs")
    print()
    print("*" * 30)
    print()
    print("Current jobs are:")
    job.read(db)
    print()
    print("*" * 30)
    print("1. Add a new job.")
    print("2. Modify a job.")
    print("3. Delete a job.")
    print("4. List jobs.")
    print("5. Search jobs.")
    print("6. Go to main menu.")
    print("7. Exit.")
    print()
    job_choice = input("What would you like to do? ")
    if job_choice == "1":
        updated_on = datetime.datetime.now().isoformat()
        job_name = input("What is the job position? ")
        print("The last 5 companies entered are:")
        company.last_entries(db, 5)
        job_company_link = input("To what company would you like to link it?")
        job_requirements = input("Would you like to add a requirements document?")
        if job_requirements.lower() == "y" or job_requirements.lower() == "yes":
            job_requirements = input("Type the document name and location: ")
            job_requirements_blob = database.convert_to_binary_data(job_requirements)
        else:
            job_requirements_blob = ""
        job.add(db, updated_on, job_company_link, job_name,
                job_requirements_blob)
        companies(db)
    elif job_choice == "2":
        updated_on = datetime.datetime.now().isoformat()
        modify_job = input("What job position would you like to change? ")
        old_job = job.get_one(db, modify_job)
        print("What is the new job name (", old_job[4], ")? \
        (ENTER to leave unchanged)")
        new_job_name = input("> ")
        if new_job_name == "":
            new_job_name = old_job[4]
        print("The last 5 companies entered are:")
        company.last_entries(db, 5)
        input()

        job.modify(db, modify_job, new_job_name)
        jobs(db)
    elif job_choice == "3":
        delete_job = input("Company to delete? ")
        job.delete(db, delete_job)
        jobs(db)
    elif job_choice == "4":
        how_many = input("Last how many entries? ")
        job.last_entries(db, how_many)
        jobs(db)
    elif job_choice == "5":
        search_job = input("Company to search for? ")
        job.search(db, search_job)
        jobs(db)
    elif job_choice == "6":
        main(db)
    elif job_choice == "7":
        goodbye(db)
    else:
        invalid_input()
        jobs(db)


def applications(db):
    pass


def resumes(db):
    pass


def cover_letters(db):
    pass


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
    db.database_connect.close()
    print()
    print("Fingers crossed. Good luck!")
    print()

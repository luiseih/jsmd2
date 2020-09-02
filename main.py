#!/usr/bin/env python3

"""
JSMD2 is an application to manage job applications.
It acts as a front end for SQLite3.
"""

__author__ = "Luis E. I. Herrera"
__copyright__ = "MIT License 2020"

# TODO:
#
# Create menus for working with job,
# application, resumes, and cover letters.
#
# Default app to see documents stored in
# database.


import cli
import sqlite3
import time
import database


def select_interface():
    interface = ""

    while interface != "1" and interface !="2":
        print("1. CLI")
        print("2. GUI")
        interface = input("? ")

    return interface

def main():
    interface = select_interface()
    db = database.Database()
    db.configuration_check(interface)
    cli.main(db)


if __name__ == '__main__':
    main()

#  vim: set ts=8 sw=4 tw=110 et :

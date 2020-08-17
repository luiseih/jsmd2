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
#
# This is getting really long.
# Create independent file modules for
# working with business, job, application,
# resumes, cover letters (maybe?).

import menu
import sqlite3
import time
import database


def main():
    db = database.Database()
    db.configuration_check()
    print("SQLite version", sqlite3.sqlite_version)
    time.sleep(1)
    menu.main(db)


if __name__ == '__main__':
    main()

#  vim: set ts=8 sw=4 tw=110 et :

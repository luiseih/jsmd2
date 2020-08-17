#!/usr/bin/env python3

import sqlite3
import configparser
import os
import menu


class Database:
    def __init__(self):
        self.database_location = ""
        self.database_name = ""
        self.dbconnect = ""

    def configuration_check(self):
        config = configparser.ConfigParser()
        if os.path.isfile('jsmd2.conf'):
            config.read('jsmd2.conf')
            self.database_location = config['DEFAULT']['DatabaseLocation']
            self.database_name = config['DEFAULT']['DatabaseName']
        else:
            self.database_location, self.database_name = menu.configuration()
            config['DEFAULT'] = {'DatabaseLocation': self.database_location,
                                 'DatabaseName': self.database_name}
            with open('jsmd2.conf', 'w') as configfile:
                config.write(configfile)
        os.chdir(self.database_location)
        if os.path.isfile(self.database_name):
            self.set_connection(self.database_name)
        else:
            self.set_connection(self.database_name)
            self.create_database()

    def set_connection(self, database_name):
        self.dbconnect = sqlite3.connect(database_name)

    def create_database(self):
        self.dbconnect.executescript("""
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

#!/usr/bin/env python3

import sqlite3
import configparser
import os
import sys
import cli
import gui


class Database:
    def __init__(self):
        self.database_location = None
        self.database_name = None
        self.database_connect = None

    def configuration_check(self, interface):
        current_dir = os.getcwd()
        config = configparser.ConfigParser()
        os.chdir(os.path.expanduser('~/.config/'))
        if os.path.isfile('jsmd2.conf'):
            config.read('jsmd2.conf')
            self.database_location = config['DEFAULT']['DatabaseLocation']
            self.database_name = config['DEFAULT']['DatabaseName']
        else:
            if interface == "1":
                configuration = cli.configuration(current_dir)
            else:
                configuration = gui.configuration(current_dir)

            try:
                self.database_location, self.database_name = configuration
                config['DEFAULT'] = {'DatabaseLocation': self.database_location,
                                     'DatabaseName': self.database_name}
                with open('jsmd2.conf', 'w') as configfile:
                    config.write(configfile)
            except TypeError:
                sys.exit()
        os.chdir(self.database_location)
        if os.path.isfile(self.database_name):
            pass
        else:
            sqlite3.connect(self.database_name)
            self.create_database()

    def create_database(self):
        sqlite3.connect(self.database_name).executescript("""
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

    def read(self, table):
        data = []
        command = "SELECT * FROM "+table
        for row in sqlite3.connect(self.database_name).execute(command):
            data.append(row)
        return data

    def add(self, table, fields, values):
        conn = sqlite3.connect(self.database_name)
        command = "INSERT INTO "+table+"("+', '.join(fields)+") VALUES (\""+', '.join(values)+"\")"
        conn.execute(command)
        conn.commit()

    def modify(self, table, field, new_status, old_rowid):
        conn = sqlite3.connect(self.database_name)
        command = "UPDATE "+table+" SET "+field+"='"+new_status+"' WHERE rowid="+old_rowid
        conn.execute(command)
        conn.commit()

    def delete(self, table, old_rowid):
        conn = sqlite3.connect(self.database_name)
        command = "DELETE FROM "+table+" WHERE rowid="+old_rowid
        conn.execute(command)
        conn.commit()

    def close(self):
        sqlite3.connect(self.database_name).close()


def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def write_to_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

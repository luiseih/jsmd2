#!/usr/bin/python3

from pathlib import Path
import os
import configparser
import sqlite3

# Check for configuration file and,
# if it doesn't exist, create it.
# Ask user for config file location,
# sqlite3 database file name and location,
# Names for tables (offer defaults).
# Default app to see documents stored in
# database.

# Check for sqlite3 database and,
# if it doesn't exist, create it.
# Use location and names previously
# provided by user. Check config file.

# Create main menu. Ask user what
# he wants to do.

# Create independent file modules for
# working with business, job, application,
# resumes, cover letters (maybe?).


def main():

    home = str(Path.home())
    full_path = os.path.join(home, ".config")
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    else:
        os.chdir(full_path)

    if not os.path.isfile('jsmd2.conf'):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'ServerAliveInternal': '45',
                             'Compression': 'yes',
                             'CompressionLevel': '9'}
        config['bitbucket.org'] = {}
        config['bitbucket.org']['User'] = 'hg'
        config['topsecret.server.com'] = {}
        topsecret = config['topsecret.server.com']
        topsecret['Port'] = '50022'                # mutates the parser
        topsecret['ForwardX11'] = 'no'             # same here
        config['DEFAULT']['ForwardX11'] = 'yes'
        with open('jsmd2.conf', 'w') as configfile:
            config.write(configfile)

    

if __name__ == '__main__':
    main()



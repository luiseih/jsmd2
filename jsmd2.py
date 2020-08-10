#!/usr/bin/python3

from pathlib import Path
import os
import configparser


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



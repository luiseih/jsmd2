#!/usr/bin/python3

import os.path
import configparser

if not os.path.isfile('.jsmd2/jsmd2.conf'):
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
    with open('.jsmd2/jsmd2.conf', 'w') as configfile:
        config.write(configfile)


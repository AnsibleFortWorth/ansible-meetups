#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sqlite3
import argparse

# read the command line args
parser = argparse.ArgumentParser()
parser.add_argument('--list', action = 'store_true')
parser.add_argument('--host', action = 'store')
args = parser.parse_args()

# basic structure the ansible ``script`` plugin expects
inventory = {
    'sqlitegroup': {
        'hosts': [],
        'vars': {}
    },
    '_meta': {
        'hostvars': {}
    }
}


# Connecting to the sqlite database and reading in the information
# (oversimplified query, but it'll do)
conn = sqlite3.connect('sqlite3_inventory.db')
curs = conn.cursor()
curs.execute('SELECT * FROM hosts')
all_records = curs.fetchall()
curs.close()

# NOTE: If you had even a slightly more sophisitcated database schema this could
#       be far more verbose, but this will work for our example
for record in all_records:
    inventory['sqlitegroup']['hosts'].append(record[1])
    inventory['sqlitegroup']['vars']['ansible_connection'] = record[2]
    inventory['_meta']['hostvars'][record[1]] = { "ansible_connection": record[2] }

if args.list:
    print(json.dumps(inventory))
elif args.host:
    if '.' in args.host:
        host = args.host.split('.')[0]
    else:
        host = args.host
    json.dumps(inventory['_meta']['hostvars'][host])






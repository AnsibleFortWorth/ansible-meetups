# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    inventory: sqlite3
    short_description: Parses our example sqlite3 database
    description:
        - Parses our example sqlite3 database
'''

import os
import sqlite3

from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native

class InventoryModule(BaseInventoryPlugin):

    NAME = 'sqlite3_inventory_plugin'

    def parse(self, inventory, loader, host_list, cache=True):
        ''' parses the sqlite3 file '''

        super(InventoryModule, self).parse(inventory, loader, host_list)

        try:

            # Connecting to the sqlite database and reading in the information
            # (oversimplified query, but it'll do)
            conn = sqlite3.connect('./sqlite3_inventory.db')
            curs = conn.cursor()
            curs.execute('SELECT * FROM hosts')
            all_records = curs.fetchall()
            curs.close()

            # NOTE: If you had even a slightly more sophisitcated database schema this could
            #       be far more verbose, but this will work for our example
            self.inventory.add_group('sqlitegroup')
            for record in all_records:
                self.inventory.add_host(record[0], group='sqlitegroup')
                self.inventory.set_variable(record[0], 'ansible_connection', record[2])

        except Exception as e:
            raise AnsibleParserError("Invalid sqlite3 database, could not parse: %s" % to_native(e))

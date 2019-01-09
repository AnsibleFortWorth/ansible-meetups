#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2013, Adam Miller <maxamillion@fedoraproject.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = r'''
---
module: hello_new_style
short_description: Say hello!
description:
  - This module allows for addition or deletion of services and ports either tcp or udp in either running or permanent firewalld rules.
version_added: "2.8"
options:
  name:
    description:
      - Name of a person or entity to say hello to
author: "Adam Miller (@maxamillion)"
'''

EXAMPLES = r'''
- hello_new_style:
    name: "Ansible Fort Worth Meetup"
'''

from ansible.module_utils.basic import AnsibleModule


def main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str'),
        ),
        supports_check_mode=False
    )


if __name__ == '__main__':
    main()

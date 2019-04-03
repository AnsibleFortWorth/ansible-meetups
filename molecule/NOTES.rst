Notes For Working With Molecule
===============================

Watch Elana Hashman's AnsibleFest 2017 talk, it's **absolutely** **amazing**.
We'll be borrowing much of her content for today's talk and demo.

    * https://www.ansible.com/infrastructure-testing-with-molecule
    * https://hashman.ca/ansiblefest-2017/


Starting Molecule with a pre-existing role

::

    molecule init scenario --role-name apache_install --driver-name vagrant


Starting Molecule to create a new role

::

    molecule init role -r role_name

Molecule Documentation of note
-----------------------------

* https://molecule.readthedocs.io/en/latest/index.html
* https://molecule.readthedocs.io/en/latest/getting-started.html
* https://testinfra.readthedocs.io/en/latest/

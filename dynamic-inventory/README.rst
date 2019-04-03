Notes For Working With and Writing Ansible Dynamic Inventories
==============================================================

These are notes about working with Ansible Dynamic Inventories as well as
writing our own.

In this directory you will find various examples that are used to demonstrate
the use and authorship of dynamic inventories.

Why dynamic inventories?
------------------------

Static inventory files are simple and easy to use and may fit your use case just
fine but if your infrastructure is very large or fluctuates often because of the
use of ephemeral technologies like Infrastructure as a Service, then maintaining
static inventory files can become combersome.

Quite Note
----------

A note about Ansible dynamic inventories, there are technically two types:


* Inventory Plugin: Native Ansible plugin written in python, utilizing the
  Ansible Plugin API

   * All inventory interaction is actually done with a plugin now, including
     static files. Whan you pass a ``.yaml``, ``.ini``, or ``.toml`` file to
     Ansible appropriate plugin is called.
   * Inventory Plugins allow dynamic inventory developers more flexibility to
     acccess Ansible internals, libraries of helper functions, built in caching
     mechanism, dynamic variable and group composition, among other things.

* Inventory Scripts: Any executable so long as it returns correct JSON when
  called with ``--list`` (also optionally ``--host`` to return a single host's
  variables)

   * Inventory Scripts are technically still avaiable today due to an Inventory
     Plugin called ``script``
   * All available inventory scripts are available here:
     https://github.com/ansible/ansible/tree/devel/contrib/inventory

Mixing Inventories
------------------

You can mix inventories, static, dyanmic scripts, and dynamic plugins. If the
location given to ``-i`` in Ansible is a directory (or as so configured in
``ansible.cfg``), Ansible can use multiple inventory sources at the same time.
When doing so, it is possible to mix both dynamic and statically managed inventory
sources in the same ansible run. Instant hybrid cloud!

Note also to configure and setup your inventory plugins under the
``[inventory]`` header in your Ansible config file (default location is
``/etc/ansible/ansible.cfg``


Ansible Documentation of note
-----------------------------

* https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html
* https://docs.ansible.com/ansible/latest/plugins/inventory.html#inventory-plugins
* https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html


Notes For Writing Custom Modules
================================

When writing custom modules there are modules of three types:

* New-Style: All current Ansible Core modules written in Python or PowerShell
* Non-Native WANT_JSON and Binary: Accept JSON as input just as new-style do
* Old-Style: Modules accept a file path containing key=value pairs as input


All modules are expected to print JSON to stdout when they exit to report status

Ansible Documentation of note
-----------------------------

* https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html
* https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html
* https://docs.ansible.com/ansible/latest/dev_guide/overview_architecture.html


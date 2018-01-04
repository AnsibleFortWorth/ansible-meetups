# playbooks-advanced

This is series of playbook examples that are derived from the [Official Ansible
Documentation](https://docs.ansible.com/ansible/latest/index.html) and are
considered to be "advanced" in nature. They are by no means meant to be
all-encompassing but are meant to introduce users to new functionality.

## Running the Examples

All playbooks contained here should be executed from the directory where
`inventory.txt` is found.

### Example

```
$ ansible-playbook loops/loops.yaml -i inventory.txt
```
#!/bin/bash

source $1

if [[ -f $some_file ]]; then
    printf '{ "msg": "Nothing to do", "changed": false }'
else
    mkdir -p $(dirname ${some_file})
    touch $some_file
    printf '{ "msg": "Created %s", "changed": true }' "$some_file"
fi






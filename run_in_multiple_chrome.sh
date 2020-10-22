#!/bin/bash
default_browser_instances=4

if [ "$#" -eq  "0" ]
   then
     echo "Using default instances to run test cases"
     pytest -n $default_browser_instances
 else
     echo "Initialising $1 chrome instances"
     pytest -n $1
 fi

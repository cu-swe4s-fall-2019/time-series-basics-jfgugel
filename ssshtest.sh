#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

# assert that stdout is not empty
run __init__ python3 data_import.py
assert_stdout


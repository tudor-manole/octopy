#!/usr/bin/env python

# TM

from faker import Faker
import random

fake = Faker()

required_lines = int(input("Input number of desired lines: "))

with open('fakedataset.csv', 'w', encoding = 'utf-8') as f:
    for i in range(required_lines):
        # format is: IP,DEST_PORT,DATE_TIME
        f.write(str(fake.ipv4()) + "," + str(random.randint(1,65535)) + "," + str(fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)) + "\n")

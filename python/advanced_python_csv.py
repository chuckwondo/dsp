#!/usr/bin/env python

import advanced_python_regex as apr

emails = sorted(apr.select_email_addresses(apr.read_faculty()))

with open('emails.csv', 'w') as f:
    for email in emails:
        f.write(email + '\n')

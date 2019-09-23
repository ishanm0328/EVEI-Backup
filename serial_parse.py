#!/usr/bin/env python3

import re

###
# Concat two lines from serial input and pass to this
# Returns a hash of the parsed data
#
def serial_parse(serial_string):

    pattern = ('^RM([0-9]+)'        # Match RM0, RM100, etc
               '[\s]*'              # Match any number of spaces after that
               'A([0-9]\.[0-9])'    # Match A0.0, A1.3, etc
               'B([0-9]\.[0-9])'    # Match B0.0, B1.3, etc
               'D\nE([0-9]+)'       # Match DE0, DE100, etc - for some reason, the D is on line 1 and the E is on line 2
               '[\s]*'              # Match any number of spaces after
               '([+-][0-9]{1,2})'   # Match +3, -12, etc
               '[\s]?'              # There might be a space, if the number before was only 1 digit
               '([+-][0-9]{1,2})'   # Match +3, -12, etc
               '[\s]?'              # There might be a space here too
               '([+-][0-9]{1,2})$') # Match +3, -12, etc

    matches = re.search(pattern, serial_string)

    if matches == None:
        raise ValueError

    data = {}
    data['rpm'] = int(matches.group(1))
    data['analog_a'] = float(matches.group(2))
    data['analog_b'] = float(matches.group(3))
    data['lap_count'] = int(matches.group(4))
    data['gyro_x'] = int(matches.group(5)) # TODO: x/y might be wrong
    data['gyro_y'] = int(matches.group(6))
    data['gyro_z'] = int(matches.group(7))
    return data

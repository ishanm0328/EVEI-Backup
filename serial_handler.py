#!/usr/bin/env python3

import re
import serial

###
# Concat two lines from serial input and pass to this
# Returns a hash of the parsed data
#
def parse(serial_string):

    pattern = ('^RM([0-9]+)'        # Match RM0, RM100, etc
               '[\s]*'              # Match any number of spaces after that
               'A([0-9]\.[0-9])'    # Match A0.0, A1.3, etc
               'B([0-9]\.[0-9])'    # Match B0.0, B1.3, etc
               '([D ])\n'           # Match D or a blank
               'E([0-9]+)'          # Match E0, E100, etc
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
    data['lap_count'] = bool(matches.group(4).strip())
    data['energy'] = int(matches.group(5))
    data['gyro_x'] = int(matches.group(6)) # TODO: x/y might be wrong
    data['gyro_y'] = int(matches.group(7))
    data['gyro_z'] = int(matches.group(8))
    return data

###
# Create a serial connection on the given port
#
def connect(port):
    return serial.Serial(port=port,
                         baudrate=9600,
                         parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE,
                         bytesize=serial.EIGHTBITS,
                         timeout=0)

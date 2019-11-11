#!/usr/bin/env python3

import re
import serial
from serial.tools.list_ports import comports

from random import randint

class SerialHandler():
    def __init__(self, data, config):
        self.data = data
        self.config = config
        self.serialport = None

    def connect(self):
        self.serialport = serial.Serial(
            port=self.config['serial']['port'],
            baudrate=self.config['serial']['baud'],
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0
        )

    def disconnect():
        self.serialport.close()

    # TODO: just read 34 bytes with a short timeout?
    def update(self):
        if self.serialport.in_waiting >= 34:
            line = self.serialport.readline()
            line = line + self.serialport.readline()
            self.data.append(parse(line))
            return True
        else:
            return False

    # TODO: store timestamp in data too
    def parse(serial_string):
        pattern = ('^RM([0-9]+)'        # Match RM0, RM100, etc
                   '[\s]*'              # Match any number of spaces after that
                   'A([0-9]\.[0-9])'    # Match A0.0, A1.3, etc
                   'B([0-9]\.[0-9])'    # Match B0.0, B1.3, etc
                   '([D ])\n'           # Match D or a blank
                   'E([0-9]+)'          # Match E0, E100, etc
                   '[\s]*'              # Match any number of spaces after
                   '([+-][0-9]{1,2})'   # Match +3, -12, etc
                   '[\s]?'              # Maybe a space, if the number was only 1 digit
                   '([+-][0-9]{1,2})'   # Match +3, -12, etc
                   '[\s]?'              # There might be a space here too
                   '([+-][0-9]{1,2})$') # Match +3, -12, etc

        matches = re.search(pattern, serial_string)

        if matches == None:
            raise ValueError # TODO: just ignore bad data?

        data = {}
        data['RPM'] = int(matches.group(1))
        data['Position'] = float(matches.group(2))
        data['analog_b'] = float(matches.group(3))
        data['lap_count'] = bool(matches.group(4).strip())
        data['Energy'] = int(matches.group(5))
        data['Acceleration'] = int(matches.group(6)) # TODO: x/y might be wrong
        data['gyro_y'] = int(matches.group(7))
        data['gyro_z'] = int(matches.group(8))
        return data

    def list_ports():
        ports = comports()
        names = []
        for port in ports:
            names.append(port.device)
        return names

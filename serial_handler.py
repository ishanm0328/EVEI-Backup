#!/usr/bin/env python3

import re
import serial
from serial.tools.list_ports import comports

from random import randint

from pprint import pprint

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

    def sublist_indexes(self, array, subarray):
        indexes = []
        for i in range(len(array)):
            if array[i] == subarray[0] and array[i:i+len(subarray)] == subarray:
                indexes.append(i)
        return indexes

    def replace_sublist(self, array, find, replace):
        indexes = self.sublist_indexes(array, find)
        for index in indexes:
            array = array[0:index] + replace + array[index+len(find):]
        return array

    def ctrl_decode(self, line):
        array = list(line)
        array = self.replace_sublist(array, [0, 57], [])
        array = self.replace_sublist(array, [254, 81], [])
        array = self.replace_sublist(array, [254, 69, 0], [])
        array = self.replace_sublist(array, [254, 69, 7], [32, 32, 32])
        array = self.replace_sublist(array, [254, 69, 64], [10])
        array = self.replace_sublist(array, [254, 69, 71], [32])
        array = self.replace_sublist(array, [254, 69, 74], [32])
        array = self.replace_sublist(array, [254, 69, 77], [32])
        print(array)
        string = bytes(array).decode('ascii')
        pprint(string)
        return string

    # TODO: just read 34 bytes with a short timeout?
    def update(self):
        if self.serialport.in_waiting >= 34:
            line = self.serialport.readline()
            line = line + self.serialport.readline()
            #line = line.decode('utf-8')
            #line = str(line, 'ascii')
            line = self.ctrl_decode(line)
            self.data.append(self.parse(line))
            return True
        else:
            return False

    # TODO: store timestamp in data too
    def parse(self, serial_string):
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
                   '([+-][0-9]{1,2})'   # Match, +3, -12, etc
                   '[\s]?$')            # Maybe match a final space

        matches = re.search(pattern, serial_string)

        if matches == None:
            raise ValueError # TODO: just ignore bad data?

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

    def list_ports():
        ports = comports()
        names = []
        for port in ports:
            names.append(port.device)
        return names

#!/usr/bin/env python3

import re

# read two strings from serial, concat them
testString = "RM0    A1.3B2.4D\nE0     +1 -2 +11\n"

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

matches = re.search(pattern, testString)

print(matches.group(1,2,3,4,5,6,7))

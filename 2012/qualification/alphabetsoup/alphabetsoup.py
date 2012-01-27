#!/usr/bin/env python

import sys
import os
from math import *
from decimal import *

DEBUG = 0
filename = None
input = []

# make sure argument was provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print "No filename provided"

# make sure filename does point to a valid file
if filename and os.path.isfile(filename):
    f = open(filename, 'r')
    try:
        t = f.readline().strip(' \t\n')
        t = int(t)
        # make sure t is within range
        if 1 <= t and t <= 20:
            for i in range(0, t):
                line = f.readline().strip('\n')
                input.append(line)
        else:
            print "T out of range: %s" % t
    except ValueError:
            print "ValueError: T not an integer: %s" % t
    except Exception, e:
            print "Exception: %s" % e
    f.close()
else:
    print "File %s doesn't exist" % filename

# alphabet soup begins
for (t, line) in enumerate(input):
    if DEBUG:
        print "Line %s: %s" % (t, line)

    letters = { 'H': 0, 'A': 0, 'C': 0, 'K': 0, 'E': 0, 'R': 0, 'U': 0, 'P': 0 }
    # count how many times each letter we care about appear in the line
    for c in line:
        if c in letters.keys():
            letters[c] = letters[c] + 1
    if DEBUG:
        print "  letters = %s" % letters

    # special case: c has to appear twice as much as the other letters
    # normalize c to the lower integer
    letters['C'] = floor(Decimal(letters['C'] / 2.0))
    if DEBUG:
        print "  new 'c' count: %s" % letters['C']
        

    # calculate the lower occurence of the letters we care about
    # this is the number of times we can repeat "HACKERCUP"
    low = min(letters.values())
    n = int(low)

    print "Case #%s: %s" % (t + 1, n)

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
                parts = line.split(' ', 2)
                W = int(parts[0])
                H = int(parts[1])
                S = parts[2]
                input.append((W, H, S))
        else:
            print "T out of range: %s" % t
    except ValueError, e:
            print "ValueError: T, W or H not an integer: %s" % e
    except Exception, e:
            print "Exception: %s" % e
    f.close()
else:
    print "File %s doesn't exist" % filename

# billboards begins
def biggest_font_size(W, H, S):
    for s in range(min(W, H), 0, -1):
        # character per line, current line number and remaining string
        cpl = int(floor(Decimal(W / s)))
        ln = 1
        rs = S
        while (len(rs) > 0):
            if DEBUG:
                print "Size: %s Char per line: %s Line: %s Remaining length: %s Remaining string: '%s'" % (s, cpl, ln, len(rs), rs)

            # does the remaining string fit in the width of the billboard?
            if len(rs) <= cpl:
                return s
            # would one more line fit in the height of the billboard?
            elif (ln + 1) * s > H:
                break
            else:
                # next char
                nc = rs[cpl]
                if nc == ' ':
                    ln = ln + 1
                    # cut at char-per-line and loose the leading space
                    rs = rs[cpl:].lstrip(' ')
                    if DEBUG:
                        print "Split on space, continue on next line with remaining string: '%s'" % rs
                    continue
                else:
                    # previous space
                    ps = rs.rfind(' ', 0, cpl)
                    if ps != -1:
                        ln = ln + 1
                        # cut at previous-space and loose the leading space
                        rs = rs[ps:].lstrip(' ')
                        if DEBUG:
                            print "Found previous space at %s, next char was '%s', continue on next line with remaining string: '%s'" % (ps, nc, rs)
                        continue
                    else:
                        # remaining strip was only 1 word
                        if DEBUG:
                            print "Remaining strip is a full word and can't be split, next char was '%s'" % nc
                        break

    # the entire string doesn't fit even at font size 1
    return 0

for (t, (W, H, S)) in enumerate(input):
    if DEBUG:
        print "Billboard #%s: %s %s %s" % (t + 1, W, H, S)

    s = biggest_font_size(W, H, S)
    print "Case #%s: %s" % (t + 1, s)


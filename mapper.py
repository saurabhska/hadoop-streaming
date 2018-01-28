#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    if not line:
        continue
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split("|")[1:]
    # process each word
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
      tokens = word.split()
      header = tokens[0]
      for v in tokens[1:]:
        v = '_'.join([header, v.split('_',1)[0]])
              print '%s\t%s' % (v, 1)

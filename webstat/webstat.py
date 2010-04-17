#!/usr/bin/env python

"""Webstat program."""

import sys
import urllib
import time
import hashlib

def webstat(address):
    """Get some basic information about a webpage.

    Returns a dictionary containing the following items: download
    time (sec), SHA1 checksum, webpage size in bytes and number of lines.
    """
    start_time = time.time()
    connection = urllib.urlopen(address)
    webpage = connection.read()
    download_time = time.time() - start_time
    sha1 = hashlib.sha1()
    sha1.update(webpage)
    page_size = len(webpage)
    return { "time"  : download_time,
             "sha1"  : sha1.hexdigest() if page_size > 0 else None,
             "size"  : page_size,
             "lines" : 0 if page_size == 0 else webpage.count('\n') + 1 }

def main():
    try:
        address = sys.argv[1]
        stats = webstat(address)
    except IOError, e:
        print >> sys.stderr, "Error:", e
    except IndexError:
        print >> sys.stderr, "Usage: python webstat.py <address>"
    else:
        print "SHA1: %s" % stats["sha1"]
        speed = stats["size"] / stats["time"] / 1024
        values = (speed, stats["size"], stats["lines"])
        print "%.2f kB/s, %d bytes, %d lines" % values

if __name__ == "__main__":
    main()

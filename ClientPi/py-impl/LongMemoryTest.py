#!/usr/bin/env python

# not used in this project.

import sys

sys.path.append('../gen-py')

from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory

from thrift import Thrift

try:
    ConnectLongMemory().getPersonConfig("AnyRandomString")

except Thrift.TException as tx:
    print("%s" % (tx.message))

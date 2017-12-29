#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')
from LongMemory.ttypes import *
import sys

sys.path.append('../gen-py')

from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory

from thrift import Thrift


def test1():
    try:
        input = LongMemoryLoginInputObject()
        input.username = 'AnyRandomString'
        input.password = None
        input.code = '12345'
        output = ConnectLongMemory().login(input)
        print(output)
    except Thrift.TException as tx:
        print("%s" % (tx.message))

def test2():
    try:
        input = LongMemoryLoginInputObject()
        input.username = 'sesy'
        input.password = None
        input.code = '12345'
        output = ConnectLongMemory().login(input)
        print(output)
    except Thrift.TException as tx:
        print("%s" % (tx.message))

def test3():
    try:
        input = LongMemoryLoginInputObject()
        input.username = 'sesy'
        input.password = None
        input.code = '456'
        output = ConnectLongMemory().login(input)
        print(output)

    except Thrift.TException as tx:
        print("%s" % (tx.message))

test1()
test2()
test3()
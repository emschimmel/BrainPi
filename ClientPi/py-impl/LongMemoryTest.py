#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')
from LongMemory.ttypes import *
import sys

sys.path.append('../gen-py')

from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory

from thrift import Thrift

try:
    input = Person()
    input.uniquename = 'AnyRandomString'

    details = user_detail()
    details.firstname = 'Celyne'
    details.lastname = 'van der Pol'
    details.gender = 'undefined'
    details.dob = '5-1-2017'
    input.details = details
    input.username = 'cbaby'
    input.password = None
    input.code = '12345'
    input.enabled = False

    ConnectLongMemory().storeNewPerson(input)
    ConnectLongMemory().getPersonConfig('AnyRandomString')

except Thrift.TException as tx:
    print("%s" % (tx.message))

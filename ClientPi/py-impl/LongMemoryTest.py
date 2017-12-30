#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')
from AutorisationStruct.ttypes import Person
from AutorisationStruct.ttypes import user_detail
from AutorisationStruct.ttypes import Autorisation
from GenericStruct.ttypes import ActionEnum
import pickle

sys.path.append('../gen-py')

from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory

from thrift import Thrift


def test1():
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

def test2():
    try:
        input = Person()
        input.uniquename = '== Hans =='

        details = user_detail()
        details.firstname = 'Hans'
        details.lastname = 'van der Pol'
        details.gender = 'Men'
        details.dob = '6-3-1966'
        input.details = details
        input.username = 'sesy'
        input.password = None
        input.code = '456'
        input.enabled = True

        autorisation = Autorisation()
        autorisation.write_enabled = True
        autorisation.enabled = True
        autorisation.module_config = pickle.dumps("unique name", protocol=None, fix_imports=False)

        actions = dict()
        actions[ActionEnum.LOGIN] = autorisation
        input.autorisations = actions
        ConnectLongMemory().storeNewPerson(input)

    except Thrift.TException as tx:
        print("%s" % (tx.message))

def test3():
    try:
        ConnectLongMemory().getAll()

    except Thrift.TException as tx:
        print("%s" % (tx.message))

def test4():
    try:
        ConnectLongMemory().getPersonConfig('AnyRandomString')

    except Thrift.TException as tx:
        print("%s" % (tx.message))

#test1()
test2()
#test3()
#test4()
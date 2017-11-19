#!/usr/bin/env bash

thrift -gen py ThriftException.thrift
thrift -gen py GenericStruct.thrift
thrift -gen py EyePi.thrift
thrift -gen py FacePi.thrift
thrift -gen py GenericServerPi.thrift

# ClientPI
cp -Rf ./gen-py/GenericStruct   ../ClientPi/gen-py/
cp -Rf ./gen-py/EyePi           ../ClientPi/gen-py/
cp -Rf ./gen-py/ThriftException ../ClientPi/gen-py/

# EyePI
cp -Rf ./gen-py/EyePi           ../EyePi/gen-py/
cp -Rf ./gen-py/FacePi          ../EyePi/gen-py/
cp -Rf ./gen-py/GenericStruct   ../EyePi/gen-py/
cp -Rf ./gen-py/GenericServerPi ../EyePi/gen-py/
cp -Rf ./gen-py/ThriftException ../EyePi/gen-py/

# FacePI
cp -Rf ./gen-py/FacePi          ../FacePi/gen-py/
cp -Rf ./gen-py/ThriftException ../FacePi/gen-py/

# GenericServerPi for WeatherPi
cp -Rf ./gen-py/GenericStruct   ../WeatherPi/gen-py/
cp -Rf ./gen-py/GenericServerPi ../WeatherPi/gen-py/
cp -Rf ./gen-py/ThriftException ../WeatherPi/gen-py/
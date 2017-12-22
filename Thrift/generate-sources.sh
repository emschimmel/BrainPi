#!/usr/bin/env bash

thrift -gen py ThriftException.thrift
thrift -gen py GenericStruct.thrift
thrift -gen py EyePi.thrift
thrift -gen py FacePi.thrift
thrift -gen py GenericServerPi.thrift
thrift -gen py ShortMemory.thrift
thrift -gen py LongMemory.thrift
thrift -gen py WeatherPi.thrift

thrift -gen java ShortMemory.thrift
thrift -gen java LongMemory.thrift
thrift -gen java GenericStruct.thrift
thrift -gen java EarPi.thrift
thrift -gen java ThriftException.thrift

rm -rf ../ClientPi/gen-py/*
rm -rf ../EyePi/gen-py/*
rm -rf ../FacePi/gen-py/*
rm -rf ../WeatherPi/gen-py/*
rm -rf ../ShortTermMemory/gen-py/*
rm -rf ../EarPi/src/main/java/nl/earpi/generated/*

# ClientPI
cp -Rf ./gen-py/GenericStruct   ../ClientPi/gen-py/
cp -Rf ./gen-py/EyePi           ../ClientPi/gen-py/
cp -Rf ./gen-py/ThriftException ../ClientPi/gen-py/
cp -Rf ./gen-py/ShortMemory     ../ClientPi/gen-py/ # mock!
cp -Rf ./gen-py/WeatherPi       ../ClientPi/gen-py/

# EyePI
cp -Rf ./gen-py/EyePi           ../EyePi/gen-py/
cp -Rf ./gen-py/FacePi          ../EyePi/gen-py/
cp -Rf ./gen-py/GenericStruct   ../EyePi/gen-py/
cp -Rf ./gen-py/GenericServerPi ../EyePi/gen-py/
cp -Rf ./gen-py/ShortMemory     ../EyePi/gen-py/
cp -Rf ./gen-py/ThriftException ../EyePi/gen-py/

# FacePI
cp -Rf ./gen-py/FacePi          ../FacePi/gen-py/
cp -Rf ./gen-py/ThriftException ../FacePi/gen-py/

# GenericServerPi for WeatherPi
cp -Rf ./gen-py/GenericStruct   ../WeatherPi/gen-py/
cp -Rf ./gen-py/GenericServerPi ../WeatherPi/gen-py/
cp -Rf ./gen-py/ThriftException ../WeatherPi/gen-py/
cp -Rf ./gen-py/WeatherPi       ../WeatherPi/gen-py/

# ShortMemory
cp -Rf ./gen-py/GenericStruct   ../ShortTermMemory/gen-py/
cp -Rf ./gen-py/ShortMemory     ../ShortTermMemory/gen-py/

# LongMemory
cp -Rf ./gen-py/GenericStruct   ../LongTermMemory/gen-py/
cp -Rf ./gen-py/LongMemory      ../LongTermMemory/gen-py/
cp -Rf ./gen-py/ThriftException ../LongTermMemory/gen-py/

#EarPI
cp -Rf ./gen-java/nl/earpi/generated/   ../EarPi/src/main/java/nl/earpi/generated/



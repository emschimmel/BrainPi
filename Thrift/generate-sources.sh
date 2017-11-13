#!/usr/bin/env bash

thrift -gen py EyePi.thrift
thrift -gen py FacePi.thrift

cp -Rf ./gen-py/EyePi ../EyePi/gen-py/
cp -Rf ./gen-py/FacePi ../EyePi/gen-py/
cp -Rf ./gen-py/FacePi ../FacePi/gen-py/
#!/usr/bin/env bash

thrift -gen py ThriftException.thrift
thrift -gen py GenericStruct.thrift
thrift -gen py AutorisationStruct.thrift
thrift -gen py EarPi.thrift
thrift -gen py EyePi.thrift
thrift -gen py FacePi.thrift
thrift -gen py GenericServerPi.thrift
thrift -gen py ShortMemory.thrift
thrift -gen py LongMemory.thrift
thrift -gen py WeatherPi.thrift
thrift -gen py LightPi.thrift
thrift -gen py AgendaPi.thrift
thrift -gen py PhonePi.thrift
thrift -gen py PhotoPi.thrift
thrift -gen py MusicPi.thrift

thrift -gen java ShortMemory.thrift
thrift -gen java LongMemory.thrift
thrift -gen java GenericStruct.thrift
thrift -gen java AutorisationStruct.thrift
thrift -gen java EarPi.thrift
thrift -gen java ThriftException.thrift

rm -rf ../AdminConsolePi/gen-py/*
rm -rf ../AgendaPi/gen-py/*
rm -rf ../1IntegrationTests/gen-py/*
rm -rf ../EarPi/Java/src/main/java/nl/earpi/generated/*
rm -rf ../EarPi/Python/gen-py/*
rm -rf ../EyePi/gen-py/*
rm -rf ../FacePi/gen-py/*
rm -rf ../LightPi/gen-py/*
rm -rf ../LongTermMemory/gen-py/*
rm -rf ../MusicPi/gen-py/*
rm -rf ../PhonePi/gen-py/*
rm -rf ../PhotoPi/gen-py/*
rm -rf ../ShortTermMemory/gen-py/*
rm -rf ../WeatherPi/gen-py/*

# AdminConsole
cp -Rf ./gen-py/GenericStruct           ../AdminConsolePi/gen-py/
cp -Rf ./gen-py/EyePi                   ../AdminConsolePi/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../AdminConsolePi/gen-py/
cp -Rf ./gen-py/ThriftException         ../AdminConsolePi/gen-py/

# GenericServerPi for AgendaPi
cp -Rf ./gen-py/GenericStruct           ../AgendaPi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../AgendaPi/gen-py/
cp -Rf ./gen-py/ThriftException         ../AgendaPi/gen-py/
cp -Rf ./gen-py/AgendaPi                ../AgendaPi/gen-py/

# 1IntegrationTests
cp -Rf ./gen-py/GenericStruct           ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/EyePi                   ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/EarPi                   ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/ThriftException         ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/ShortMemory             ../1IntegrationTests/gen-py/ # mock!
cp -Rf ./gen-py/LongMemory              ../1IntegrationTests/gen-py/ # mock!
cp -Rf ./gen-py/WeatherPi               ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/PhonePi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/PhotoPi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/LightPi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/MusicPi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/AgendaPi                ../1IntegrationTests/gen-py/

#EarPI
cp -Rf ./gen-java/nl/earpi/generated/   ../EarPi/Java/src/main/java/nl/earpi/generated/
cp -Rf ./gen-py/EarPi                   ../EarPi/Python/gen-py/
cp -Rf ./gen-py/GenericStruct           ../EarPi/Python/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../EarPi/Python/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../EarPi/Python/gen-py/
cp -Rf ./gen-py/ShortMemory             ../EarPi/Python/gen-py/
cp -Rf ./gen-py/LongMemory              ../EarPi/Python/gen-py/
cp -Rf ./gen-py/ThriftException         ../EarPi/Python/gen-py/

# EyePI
cp -Rf ./gen-py/EyePi                   ../EyePi/gen-py/
cp -Rf ./gen-py/FacePi                  ../EyePi/gen-py/
cp -Rf ./gen-py/GenericStruct           ../EyePi/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../EyePi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../EyePi/gen-py/
cp -Rf ./gen-py/ShortMemory             ../EyePi/gen-py/
cp -Rf ./gen-py/LongMemory              ../EyePi/gen-py/
cp -Rf ./gen-py/ThriftException         ../EyePi/gen-py/

# FacePI
cp -Rf ./gen-py/FacePi                  ../FacePi/gen-py/
cp -Rf ./gen-py/ThriftException         ../FacePi/gen-py/

# GenericServerPi for LightPi
cp -Rf ./gen-py/GenericStruct           ../LightPi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../LightPi/gen-py/
cp -Rf ./gen-py/ThriftException         ../LightPi/gen-py/
cp -Rf ./gen-py/LightPi                 ../LightPi/gen-py/

# LongMemory
cp -Rf ./gen-py/GenericStruct           ../LongTermMemory/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../LongTermMemory/gen-py/
cp -Rf ./gen-py/LongMemory              ../LongTermMemory/gen-py/
cp -Rf ./gen-py/ThriftException         ../LongTermMemory/gen-py/

# GenericServerPi for MusicPi
cp -Rf ./gen-py/GenericStruct           ../MusicPi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../MusicPi/gen-py/
cp -Rf ./gen-py/ThriftException         ../MusicPi/gen-py/
cp -Rf ./gen-py/MusicPi                 ../MusicPi/gen-py/

# GenericServerPi for PhonePi
cp -Rf ./gen-py/GenericStruct           ../PhonePi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../PhonePi/gen-py/
cp -Rf ./gen-py/ThriftException         ../PhonePi/gen-py/
cp -Rf ./gen-py/PhonePi                 ../PhonePi/gen-py/

# GenericServerPi for PhotoPi
cp -Rf ./gen-py/GenericStruct           ../PhotoPi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../PhotoPi/gen-py/
cp -Rf ./gen-py/ThriftException         ../PhotoPi/gen-py/
cp -Rf ./gen-py/PhotoPi                 ../PhotoPi/gen-py/

# ShortMemory
cp -Rf ./gen-py/GenericStruct           ../ShortTermMemory/gen-py/
cp -Rf ./gen-py/ShortMemory             ../ShortTermMemory/gen-py/

# GenericServerPi for WeatherPi
cp -Rf ./gen-py/GenericStruct           ../WeatherPi/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../WeatherPi/gen-py/
cp -Rf ./gen-py/ThriftException         ../WeatherPi/gen-py/
cp -Rf ./gen-py/WeatherPi               ../WeatherPi/gen-py/

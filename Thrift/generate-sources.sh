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

thrift -gen go EarPi.thrift
thrift -gen go GenericStruct.thrift
thrift -gen go AutorisationStruct.thrift
thrift -gen go ThriftException.thrift

rm -rf ../AdminConsolePi/gen-py/*
rm -rf ../AgendaPi/src/gen-py/*
rm -rf ../1IntegrationTests/gen-py/*
rm -rf $HOME/go/src/generated/
rm -rf ../EarPi/Java/src/main/java/nl/earpi/generated/*
rm -rf ../EarPi/src/gen-py/*
rm -rf ../EyePi/src/gen-py/*
rm -rf ../FacePi/src/gen-py/*
rm -rf ../LightPi/src/gen-py/*
rm -rf ../LongTermMemory/src/gen-py/*
rm -rf ../MusicPi/src/gen-py/*
rm -rf ../PhonePi/src/gen-py/*
rm -rf ../PhotoPi/src/gen-py/*
rm -rf ../ShortTermMemory/src/gen-py/*
rm -rf ../StatisticPi/src/main/scala/nl/statisticpi/generated/*
rm -rf ../WeatherPi/src/gen-py/*
rm -rf ../SetupDevEnv/Consul/gen-py/*

# AdminConsole
cp -Rf ./gen-py/GenericStruct           ../AdminConsolePi/gen-py/
cp -Rf ./gen-py/EyePi                   ../AdminConsolePi/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../AdminConsolePi/gen-py/
cp -Rf ./gen-py/ThriftException         ../AdminConsolePi/gen-py/

# GenericServerPi for AgendaPi
cp -Rf ./gen-py/GenericStruct           ../AgendaPi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../AgendaPi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../AgendaPi/src/gen-py/
cp -Rf ./gen-py/AgendaPi                ../AgendaPi/src/gen-py/

# 1IntegrationTests
cp -Rf ./gen-py/GenericStruct           ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/EyePi                   ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/EarPi                   ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/FacePi                   ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/ThriftException         ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/ShortMemory             ../1IntegrationTests/gen-py/ # mock!
cp -Rf ./gen-py/LongMemory              ../1IntegrationTests/gen-py/ # mock!
cp -Rf ./gen-py/WeatherPi               ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/PhonePi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/PhotoPi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/LightPi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/MusicPi                 ../1IntegrationTests/gen-py/
cp -Rf ./gen-py/AgendaPi                ../1IntegrationTests/gen-py/

# DeviceRegistrationUI
# GOPATH = $HOME/go
cp -Rf ./gen-go/               $HOME/go/src/

#EarPI
cp -Rf ./gen-java/nl/earpi/generated/   ../EarPi/Java/src/main/java/nl/earpi/generated/
cp -Rf ./gen-py/EarPi                   ../EarPi/src/gen-py/
cp -Rf ./gen-py/GenericStruct           ../EarPi/src/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../EarPi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../EarPi/src/gen-py/
cp -Rf ./gen-py/ShortMemory             ../EarPi/src/gen-py/
cp -Rf ./gen-py/LongMemory              ../EarPi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../EarPi/src/gen-py/

# EyePI
cp -Rf ./gen-py/EyePi                   ../EyePi/src/gen-py/
cp -Rf ./gen-py/FacePi                  ../EyePi/src/gen-py/
cp -Rf ./gen-py/GenericStruct           ../EyePi/src/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../EyePi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../EyePi/src/gen-py/
cp -Rf ./gen-py/ShortMemory             ../EyePi/src/gen-py/
cp -Rf ./gen-py/LongMemory              ../EyePi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../EyePi/src/gen-py/

# FacePI
cp -Rf ./gen-py/FacePi                  ../FacePi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../FacePi/src/gen-py/

# GenericServerPi for LightPi
cp -Rf ./gen-py/GenericStruct           ../LightPi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../LightPi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../LightPi/src/gen-py/
cp -Rf ./gen-py/LightPi                 ../LightPi/src/gen-py/

# LongMemory
cp -Rf ./gen-py/GenericStruct           ../LongTermMemory/src/gen-py/
cp -Rf ./gen-py/AutorisationStruct      ../LongTermMemory/src/gen-py/
cp -Rf ./gen-py/LongMemory              ../LongTermMemory/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../LongTermMemory/src/gen-py/

# GenericServerPi for MusicPi
cp -Rf ./gen-py/GenericStruct           ../MusicPi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../MusicPi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../MusicPi/src/gen-py/
cp -Rf ./gen-py/MusicPi                 ../MusicPi/src/gen-py/

# GenericServerPi for PhonePi
cp -Rf ./gen-py/GenericStruct           ../PhonePi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../PhonePi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../PhonePi/src/gen-py/
cp -Rf ./gen-py/PhonePi                 ../PhonePi/src/gen-py/

# GenericServerPi for PhotoPi
cp -Rf ./gen-py/GenericStruct           ../PhotoPi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../PhotoPi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../PhotoPi/src/gen-py/
cp -Rf ./gen-py/PhotoPi                 ../PhotoPi/src/gen-py/

# ShortMemory
cp -Rf ./gen-py/GenericStruct           ../ShortTermMemory/src/gen-py/
cp -Rf ./gen-py/ShortMemory             ../ShortTermMemory/src/gen-py/

# StatisticPi
cp -Rf ./gen-py/ShortMemory             ../StatisticPi/src/main/scala/nl/statisticpi/generated/

# GenericServerPi for WeatherPi
cp -Rf ./gen-py/GenericStruct           ../WeatherPi/src/gen-py/
cp -Rf ./gen-py/GenericServerPi         ../WeatherPi/src/gen-py/
cp -Rf ./gen-py/ThriftException         ../WeatherPi/src/gen-py/
cp -Rf ./gen-py/WeatherPi               ../WeatherPi/src/gen-py/

# SetupEnv
cp -Rf ./gen-py/GenericStruct           ../SetupDevEnv/Consul/gen-py/
cp -Rf ./gen-py/ShortMemory             ../SetupDevEnv/Consul/gen-py/
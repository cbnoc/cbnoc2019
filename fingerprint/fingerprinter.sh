#!/bin/sh

nohup python2 ./joy/fingerprinting/fingerprinter.py -i eth1 -o ./log/FPlog.json > joy.out &

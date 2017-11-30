#!/bin/bash

python CPULoadGenerator.py &
pid=$!
htop

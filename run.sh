#!/bin/bash

set -e
g++ -o main ${1:-"base/main.cpp"} -std=c++17 -Wall -Wextra -Wshadow -Wconversion -Wfloat-equal -Wvla -Wduplicated-cond -Wlogical-op -Wnull-dereference -Wdouble-promotion -Wformat=2

./main
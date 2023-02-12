#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('python-practice\ex-files-python-esst\exercise-files\chap-12\lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
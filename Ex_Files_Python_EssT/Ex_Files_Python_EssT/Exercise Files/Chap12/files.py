#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('C:/Users/nvilc/iCloudDrive/Documents/Synced Code/Ex_Files_Python_EssT/Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt') # Windows 10 file path
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
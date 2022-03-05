def main():
    f = open('C:/Users/nvilc/iCloudDrive/Documents/Synced Code/Python Essential Training/Chap12/lines.txt', 'r') # can replace file path backslashes with foward slashes in Python 
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()        
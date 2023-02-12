def main():
    f = open('python-practice\python-essential-training\chap-12\lines.txt', 'r') # can replace file path backslashes with forward slashes in Python 
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
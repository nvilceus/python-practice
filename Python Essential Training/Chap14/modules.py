# import sys
# import os
# import random
import datetime

def main():
    # v = sys.version_info
    # print('Python version {}.{}.{}'.format(*v))
    # v = sys.platform
    # v = os.name
    # v = os.getenv('PATH')
    # v = os.getcwd()
    # v = os.urandom(25).hex() # random number that is 25 bytes long
    # print(v)
    # x = random.randint(1, 1000)
    # x = list(range(25))
    # random.shuffle(x)
    # print(x)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()    
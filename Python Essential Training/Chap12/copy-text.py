def main():
    infile = open('C:/Users/nvilc/iCloudDrive/Documents/Synced Code/Python Essential Training/Chap12/lines.txt', 'rt') # Windows 10 file path
    outfile = open('C:/Users/nvilc/iCloudDrive/Documents/Synced Code/Python Essential Training/Chap12/lines-copy.txt', 'wt') # Windows 10 file path
    for line in infile:
        # print(line.rstrip(), file=outfile)
        outfile.writelines(line) # does the same as the line above
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
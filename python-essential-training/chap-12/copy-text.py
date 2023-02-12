def main():
    infile = open('python-practice\python-essential-training\chap-12\lines.txt', 'rt')
    outfile = open('python-practice\python-essential-training\chap-12\lines-copy.txt', 'wt')
    for line in infile:
        # print(line.rstrip(), file=outfile)
        outfile.writelines(line) # does the same as the line above
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
def main():
    infile = open('python-practice\python-essential-training\chap-12/berlin.jpg', 'rb')
    outfile = open('python-practice\python-essential-training\chap-12/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # 10 kbyte buffer
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\done.')

if __name__ == '__main__': main()
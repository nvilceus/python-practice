def main():
    a = set("We're gonna neeed a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a & b)
    # print_set(b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
def main():
    seq = range(11)
    from math import pi
    # seq2 = [x * 2 for x in seq] # Multiplies each element in the sequence by 2
    # seq2 = [x for x in seq if x % 3 != 0] # Only prints element in the sequence that are not divisible by 3
    # seq2 = [(x, x**2) for x in seq] # Creates tuples for each element in the sequence and its square
    # seq2 = [round(pi, i) for i in seq] # Prints pi for each element in the sequence with the number of decimal places equal to each corresponding element
    # seq2 = {x: x**2 for x in seq} # Prints a dictionary for each element in the sequence and its square
    seq2 = {x for x in 'superduper' if x not in 'pd'} # Prints each letter that is not p or d in superduper
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
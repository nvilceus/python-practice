def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    # print(game[1:5:2])
    i = game.index('Paper') # Gets the index of Paper
    # print(game[i])
    # game.append('Computer') # Adds Computer to the end of the list
    # game.insert(0, 'Computer') # Inserts Computer at the specified index
    # game.remove('Paper')
    # x = game.pop() # Removes an item from the end of the list and returns the removed item
    # print(x)
    # game.pop(3) # Removes the value at the third index
    # del game[3] # Removes the value at the third index
    # del game[1:3] # Removes Paper and Scissors by slice
    # print(', '.join(game)) # Prints the list joined by comma, space in between each of the elements
    print(len(game))
    print_list(game)

def print_list(o):
    for i in o: print(i, end = ' ', flush = True)
    print()

if __name__ == '__main__': main()
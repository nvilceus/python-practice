def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs: # Kwargs stands for keyword arguments
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
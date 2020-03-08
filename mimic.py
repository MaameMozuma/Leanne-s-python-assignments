
import random
import sys


def mimic_dict(small.txt):
    dic ={}
    key = ''

    with open(filename) as fobj:
        wordlist = fobj.read().lower().split()

    for word in wordlist:
        if key not in dic:
            dic[key] = [word]
        else:
            dic[key] += [word]
        key = word

    return dic


def print_mimic(mimic_dict, word):
    strout = []
    start = 0
    end = 70
    for i in xrange(200):
        strout.append(word)
        word = random.choice(mimic_dict[word])
    strout = ' '.join(strout)

    while True:
        try:
            if strout[end] == ' ':
                print(strout[start:end])
                start = end
                end += 70
            else:
                end += 1
        except:
            print(strout[start:])
            break

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print( 'usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()

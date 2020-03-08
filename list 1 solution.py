def match_ends(words):
    li=0
    for item in words:
        if len(item)>=2 and item[0]==item[-1]:
            li+=1
    return li
print(match_ends(['aa','aba','x','bbb']))         


def front_x(words):
    li1=[]
    list2=[]
    for item in words:
        if item.startswith('x'):
         li1.append(item)
        else:
            list2.append(item)
    return sorted(li1)+sorted(list2)
print(front_x([ 'bbb', 'ccc', 'axx', 'xzz', 'xaa']))   
    

def last(tup):
        return tup[-1]



def sort_last(tuples):
        return sorted(tuples,key=last)
print(sort_last([(1, 3), (3, 2), (2, 1)]))
print(sort_last([(1, 4), (3, 2), (2, 8)]))


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))














# Calls the above functions with interesting inputs.
def main():
  print ('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print ('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print( 'sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()


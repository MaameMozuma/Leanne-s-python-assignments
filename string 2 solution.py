def verbing(s):
    if len(s)>=3 and s[4:]==("ing"):
       return(s +'ly')
    else:
       return (s +'ing')
    
print(verbing('hail'))
print(verbing('swiming'))
print(verbing('do'))

def front_back(a,b):
    afront=len(a)
    aindex=len(a)//2
    bfront=len(b)
    bindex=len(b)//2
    if afront%2==1:
        aindex=aindex+1
    if bfront %2==1:
        bindex=bindex+1
    return a[:aindex]+b[:bindex]+a[aindex:]+b[bindex:]


def not_bad(s):
    word1=s.find('not')
    word2=s.find('bad')
    r=s.replace(s[word1:(word2+3)],'good')
    if word1<word2:
     return r
print(not_bad('tea is not bad'))



def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")


  print( 'front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()


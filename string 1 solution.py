def donuts(count):
    if count<10:
        return("number of donuts:5")
    else:
        return("number of donuts:many")

print(donuts(5))


def both_ends(s):
    if len(s)<2:
        return(" ")
    else:
        return(s[:2]+s[-2:])
print(both_ends("spring"))
print(both_ends("s"))


def fix_start(s):
    back=s[1:]
    new_s=s.replace(s[0],"*")
    return(s[0]+new_s)
print(fix_start("cocky"))


def mix_up(a,b):
    return(b[:2]+a[2:]+""+a[:2]+b[2:])
print(mix_up("dog","dinner"))


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print( '%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
         
def main():
  print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print( 'both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()


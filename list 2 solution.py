def remove_adjacent(nums):
    result=[]
    for num in nums:
        if len(result)==0 or num!= result[-1]:
            result.append(num)
    return result




def linear_merge(list1,list2):
    solution=[]
    while len(list1) and len(list2):
        if list1[0]<list2[0]:
            solution.append(list1.pop(0))
        else:
            solution.append(list2.pop(0))

    solution.extend(list1)
    solution.extend(list2)
    return solution



def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  
  print ('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()


def remove_adjacent(nums):
  result = []
  for num in nums:
    if len(result) == 0 or num != result[-1]:
      result.append(num)
  return result
  

def linear_merge(list1, list2):
  result = []
  while len(list1) and len(list2):
    if list1[0] < list2[0]:
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))

  
  result.extend(list1)
  result.extend(list2)
  return result
  
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()

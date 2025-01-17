
def donuts(count):
  if count < 10:
    return 'Number of donuts: ' + str(count)
  else:
    return 'Number of donuts: many'
  


def both_ends(s):

  if len(s) < 2:
    return ''
  first2 = s[0:2]
  last2 = s[-2:]
  return first2 + last2
 



def fix_start(s):
  
  front = s[0]
  back = s[1:]
  fixed_back = back.replace(front, '*')
  return front + fixed_back
  
def mix_up(a, b):
  
  a_swapped = b[:2] + a[2:]
  b_swapped = a[:2] + b[2:]
  return a_swapped + ' ' + b_swapped
 


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
  print('donuts')
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print()
  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')


  print()
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')



if __name__ == '__main__':
  main()

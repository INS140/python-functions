def max_num(*args):
  return max(args)

def mult_list(*args):
  s = 1
  for x in args:
    s *= x
  return s

def rev_string(str):
  return str[::-1]

def num_within(num, begin, end):
  return begin <= num <= end

def pascal(n):
  string = ''
  prev = ''
  for x in range(n):
    if x == 0:
      prev = '1'
      string += f'{prev}\n'
    elif x == 1:
      prev = '1 1'
      string += f'{prev}\n'
    else:
      current = ''
      split = prev.split()
      for i, n in enumerate(split):
        if i != len(split) - 1:
          num = int(n) + int(split[i+1])
          current += f'{str(num)} '
      prev = f'1 {current}1'
      string += f'{prev}\n'
  return string

print(max_num(10000, 2, 4, 8, 1, 1900))

print(mult_list(10, 10))

print(rev_string('Hello!'))

print(num_within(1, 4, 10))
print(num_within(2, 1, 3), '\n')

print(pascal(5))
from collections import deque

q = deque()

n = int(input('Enter N: '))

print('Enter token no, id')

for i in range(n):
  inp = input()
  inp = inp.split(',')
  pair = (int(inp[0]), inp[1].strip())
  q.append(pair)

q = deque(sorted(q, key=lambda x: x[0]))

k = input('Enter k: ')

k_pair = [i for i in q if k in i]

q.remove(k_pair[0])

print('The order is: ')
print(k_pair[0])

for i in range(len(q)):
  print(q.popleft())

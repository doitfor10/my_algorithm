
while True:
  a,b = map(int,input().split())
  if a == 0 and b == 0:
    break
  print(a+b)


try:
  while True:
    a,b = map(int,input().split())
    print(a+b)
except:
  exit()
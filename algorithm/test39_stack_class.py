#백준 스택구현 클래스 1082 
#push 정수 x를 넣어준다.
#pop 가장 위에 있는 정수 출력, 없을 경우 -1
#size 정수 개수 
#empty 비어있으면 1, 아니면 0
#top 가장 위에 있는 정수 출력

import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None
    self.length = 0
  
  def push(self,value):
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head
    self.length+=1

  def is_empty(self):
    return self.head is None

  def pop(self):
    if self.is_empty():
      return -1  

    delete_node = self.head.data
    self.head = self.head.next
    self.length-=1
    return delete_node

  def top(self):
    if self.is_empty():
      return -1 
    return self.head.data

  def size(self):
    if self.is_empty():
      return 0 
    return self.length

case = int(sys.stdin.readline())
stack = Stack()
for _ in range(case):
  command = sys.stdin.readline().split()
  

  if command[0] =='push':
    stack.push(int(command[1]))

  
  elif command[0] =='pop':
    print(stack.pop())
  
  elif command[0] =='size':
    print(stack.size())
  
  elif command[0] =='empty':
    if stack.is_empty():
      print(1)
    else:
      print(0)
  elif command[0] =='top':
    print(stack.top())
    
  
    


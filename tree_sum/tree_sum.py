# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def tree_sum(root):
  sum = 0
  if not root:
    return sum
  
  queue = deque()
  queue.append(root)
  
  while queue:
    curr = queue.popleft()
    sum += curr.val
    
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
  return sum
  
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
import math
def tree_min_value(root):
  min = math.inf
  
  queue = deque()
  queue.append(root)
  queue = deque()
  
  while queue:
    curr = queue.popleft()
    
    if curr.val < min:
      min = curr.val
    
    if curr.left:
      queue.append(curr.left)
    
    if curr.right:
      queue.append(curr.right)
      
  return min
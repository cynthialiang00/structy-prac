# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def tree_includes(root, target):
  if not root:
    return False
  
  queue = deque()
  queue.append(root)
  
  while queue:
    curr = queue.popleft()
    if curr.val == target:
      return True
    
    if curr.left:
      queue.append(curr.left)
      
    if curr.right:
      queue.append(curr.right)
  return False
  
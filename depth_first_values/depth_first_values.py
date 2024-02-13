# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def depth_first_values(root):
  if not root:
    return []
  stack = [root]
  
  res = []
  
  while stack:
    curr = stack.pop()
    res.append(curr.val)
    
    if curr.right:
      stack.append(curr.right)
      
    if curr.left:
      stack.append(curr.left)
  
  return res
    
​
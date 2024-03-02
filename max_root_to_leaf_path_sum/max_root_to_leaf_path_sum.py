class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
import math
​
def max_path_sum(root):
  
  def traverse_sum(root):
    
    if not root:
      return -math.inf
    print(f'node: {root.val}')
    if not root.left and not root.right:
      return root.val
    
    left_sum = traverse_sum(root.left)
    right_sum = traverse_sum(root.right)
    
    return root.val + max(left_sum, right_sum)
​
  max_sum = traverse_sum(root)
  return max_sum
    
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)
​
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
​
max_path_sum(a)
    
    
    
      
  
  
​
b.right = e
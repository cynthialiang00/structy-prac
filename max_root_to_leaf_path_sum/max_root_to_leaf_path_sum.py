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
    
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)
​
a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g
b.right = e
​
max_path_sum(a)
    
    
    
      
  
  
​
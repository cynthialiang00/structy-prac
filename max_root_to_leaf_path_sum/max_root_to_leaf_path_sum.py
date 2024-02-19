# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
import math
​
def max_path_sum(root):
  
  def traverse_sum(root):
    if not root:
      return -math.inf
    if not root.left and not root.right:
      return root.val
    print(f'node: {root.val}')
    left_sum = traverse_sum(root.left)
    right_sum = traverse_sum(root.right)
    
    return root.val + max(left_sum, right_sum)
​
  max_sum = traverse_sum(root)
  return max_sum
    
​
    
    
    
    
    
      
  
  
​
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
    
a = Node(42)
b.right = e
​
max_path_sum(a)
    
    
    
      
  
  
​
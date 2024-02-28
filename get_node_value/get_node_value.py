# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def get_node_value(head, index):
  curr = head
  list_count = 0
  
  while curr:
    if list_count == index:
      return curr.val
    curr = curr.next
    list_count += 1
  return None
  
​
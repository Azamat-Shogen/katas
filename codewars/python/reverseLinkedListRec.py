class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None

class LLinkedList:
  def __init__(self):
    self.head = None


  def append_node(self, new_node):
    node = Node(new_node)
    if self.head is None:
      self.head = node
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = node
  

  
  def to_list(self):
    arr = []
    
    current = self.head
    while current is not None:
      arr.append(current.val)
      current = current.next
    return arr

  def reverse(self):
    self.head = self.reverse_rec(self.head)
    return self.head

  def reverse_rec(self, current):
    if current == None:
      return current
    elif current.next == None:
      return current
    else:
      nextNode = current.next
      current.next = None
      rest = self.reverse_rec(nextNode)
      nextNode.next = current
      return rest
    


list1 = LLinkedList()
list1.append_node("a")
list1.append_node("b")
list1.append_node("c")

list1.reverse()

print(list1.to_list())

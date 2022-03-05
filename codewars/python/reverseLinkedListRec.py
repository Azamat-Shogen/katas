class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None

class LLinkedList:
  def __init__(self):
    self.head = None


  def reverse(self, current):
    if current == None:
      return current
    elif current.next == None:
      return current
    else:
      nextNode = current.next
      current.next = None
      rest = self.reverse(nextNode)
      nextNode.next = current
      return rest
    

# test examples
a = Node("a")
b = Node("b")
c = Node("c")

a.next = b
b.next = c

list1 = LLinkedList()

test = list1.reverse(a)

print(test.next.next.val)
    
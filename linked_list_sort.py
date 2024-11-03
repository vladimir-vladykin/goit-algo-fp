
def main():
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(3)
    
    print(f"State of linked list at start:")
    linked_list.print_list()
    print("\n")

    linked_list.reverse()

    print(f"State of linked list after reverse:")
    linked_list.print_list()
    print("\n")

    linked_list.sort()

    print(f"State of linked list after sorting:")
    linked_list.print_list()
    print("\n")

    second_linked_list = LinkedList()
    second_linked_list.insert_at_end(13)
    second_linked_list.insert_at_end(0)
    second_linked_list.insert_at_end(6)

    print(f"Second list:")
    second_linked_list.print_list()
    print("\n")

    linked_list = merge_linked_list_sorted(linked_list, second_linked_list)
    print(f"State of list after merge:")
    linked_list.print_list()
    print("\n")



# single node of linked list
class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


# implementation of linked list
class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def get_tail_node(self):
    current = self.head
    while current:
      if current.next is None:
        # this is tail
        return current
      current = current.next
    
    return None
      


  # go through list, but make every next as previous,
  # this way reverse list
  def reverse(self):
    current = self.head
    previous = None

    while current:
      next = current.next

      # reverse
      current.next = previous

      previous = current
      current = next

    # remember updated head
    self.head = previous
      
      
  def sort(self):
    # insertion sort
    # create new list, and than insert each element in right position
    # in new list

    new_head = None
    current = self.head

    while current:
      next = current.next

      # insert node into right place, it migth become new head, or 
      # be insered in the middle or end of the list
      new_head = sorted_insert(current, new_head)
      current = next

    self.head = new_head


def sorted_insert(new_node, head):
    # check if we can just inser new node at the beggining of list
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node
    else:
        # otherwise we have to find rigth place inside list to insert new node
        curr = head
        
        while curr.next is not None and curr.next.data < new_node.data:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        return head


def merge_linked_list_sorted(first: LinkedList, second: LinkedList) -> LinkedList:
    # merging with sorting as simple as:
    # 1. combine two list together (just connect tail of first one to head of second one)
    # 2. run sorting 
    
    tail_of_first_list = first.get_tail_node()
    head_of_second_one = second.head

    tail_of_first_list.next = head_of_second_one
    
    first.sort()

    # at this point first list contains data from both lists
    return first



if __name__ == "__main__":
    main()
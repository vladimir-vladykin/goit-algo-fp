import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


def main():
  # build heap
  heap_list = [1, 3, 5, 7, 9, 2, 6]
  heapq.heapify(heap_list)
  print(f"Our heap is:\n{heap_list}")

  # convert heap into tree
  root = build_tree_from_heap(heap_list)
  print(f"Root is {root.val}")

  # draw tree
  draw_tree(root)


def build_tree_from_heap(heap: list, index = 0):
  if index >= len(heap):
    return None
  
  root = Node(heap[index])
  root.left = build_tree_from_heap(heap, index * 2 + 1)
  root.right = build_tree_from_heap(heap, index * 2 + 2)
  return root
  

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color
    self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val)
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


if __name__ == "__main__":
    main()

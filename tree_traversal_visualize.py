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
  
  nodes_count = count_nodes(root)
  
  # draw dfs order of traverse
  dfs_colors = colors_for_dfs_traverse(root, nodes_count)
  draw_tree(root, dfs_colors)

  # draw bfs order of traverse
  bfs_colors = colors_for_bfs_traverse(root, nodes_count)
  draw_tree(root, bfs_colors)


def colors_for_dfs_traverse(root, total_steps):
  visited = set()
  stack = [root]
  colors = {}

  step = 0
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)

      colors[node.id] = generate_color(step, total_steps)

      neighbours = []
      if node.left is not None:
        neighbours.append(node.left)
      if node.right is not None:
        neighbours.append(node.right)

      stack.extend(neighbours)
      step += 1

  return colors


def colors_for_bfs_traverse(root, total_steps):
  visited, queue = {root}, [root]
  colors = {}

  step = 0
  while queue:
    node = queue.pop(0)
    colors[node.id] = generate_color(step, total_steps)
    step += 1

    neighbours = []
    if node.left is not None:
      neighbours.append(node.left)
    if node.right is not None:
      neighbours.append(node.right)
      
    for neighbour in neighbours:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

  return colors

# the bigger step -> the lighter color
def generate_color(step, max_step):
  base_color = [135, 206, 240]

  if step == 0:
    new_color = base_color
  else:
    # we don't want to achieve completly white color on last step
    max_possible_color = 245

    # how close we to the end of traversal,
    # extra plus to step because we skip this code for very first step, where base color is used
    progress_percent = (step + 1) / max_step

    max_factor_red = max_possible_color - base_color[0]
   
    # note that we could increase each color component, but 
    # experiments shows that we got the best result if we change only red part of color 
    new_color = [
      base_color[0] + int(progress_percent * max_factor_red),
      base_color[1],
      base_color[2]
    ]

  return f"#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}"


def build_tree_from_heap(heap: list, index = 0):
  if index >= len(heap):
    return None
  
  root = Node(heap[index])
  root.left = build_tree_from_heap(heap, index * 2 + 1)
  root.right = build_tree_from_heap(heap, index * 2 + 2)
  return root
  

def count_nodes(root):
  if root is None:
    return 0
  
  return 1 + count_nodes(root.left) + count_nodes(root.right)
  

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


def draw_tree(tree_root, colors):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors, edge_color="skyblue")
  plt.show()


if __name__ == "__main__":
    main()

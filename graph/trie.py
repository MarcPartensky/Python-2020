#This script is inspired by wikipedia
'https://en.wikipedia.org/wiki/Trie'

class Node:
   def __init__(self) -> None:
       # Note that using dictionary for children (as in this implementation)
       # would not allow lexicographic sorting mentioned in the next section
       # (Sorting), because an ordinary dictionary would not preserve the
       # order of the keys
       self.children: Dict[str, Node] = {}  # mapping from character ==> Node
       self.value: Any = None

def find(node: Node, key: str) -> Any:
    """Find value by key in node."""
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value

def insert(node: Node, key: str, value: Any) -> None:
    """Insert key/value pair into node."""
    for char in key:
        if char not in node.children:
            node.children[char] = Node()
        node = node.children[char]
    node.value = value

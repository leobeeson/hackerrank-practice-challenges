

class Node:
    def __init__(self, info) -> None:
        self.info = info
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.info)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
            
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root:Node, v1: int, v2: int) -> Node:
    if v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    
    if v1 > root.info and v2 > root.info:
        return lca(root.right, v1, v2)
    
    return root


if __name__ == "__main__":
    tree = BinarySearchTree()
    
    t = 6
    arr = [4, 2, 3, 1, 7, 6]
    v1 = 1
    v2 = 7

    for i in range(t):
        tree.create(arr[i])

    ancestor = lca(tree.root, v1, v2)
    print(ancestor)
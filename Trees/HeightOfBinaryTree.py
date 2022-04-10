from collections import deque

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 


class BinarySearchTree:
    def __init__(self): 
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


def height(root: Node) -> int:
    # https://www.youtube.com/watch?v=EsFZeqHaO6w&t=434s&ab_channel=StudyAlgorithms
    node_queue = deque()
    node_queue.append(root)

    levels_counter = -1

    while True:
        current_queue_size = len(node_queue)
        if current_queue_size  == 0:
            return levels_counter

        while current_queue_size > 0:
            node = node_queue.popleft()

            if node.left is not None:
                node_queue.append(node.left)
            if node.right is not None:
                node_queue.append(node.right)
            current_queue_size -= 1

        levels_counter += 1


def height_recursive(root: Node):
    # https://www.youtube.com/watch?v=SgEqoq8LqKM&ab_channel=HackersRealm
    if root is None:
        return -1
    else:
        return 1 + max(height_recursive(root.left), height_recursive(root.right))



if __name__ == "__main__":
    tree = BinarySearchTree()

    t = 1
    arr = [4]
    
    for i in range(t):
        tree.create(arr[i])

    max_height = height(tree.root)
    max_height_recursive = height_recursive(tree.root)
    

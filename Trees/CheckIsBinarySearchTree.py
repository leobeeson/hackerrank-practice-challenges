from collections import deque

class node:
    def __init__(self, data: int) -> None:
        self.info = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.info)


def checkBST(root: node) -> bool:
    # https://www.youtube.com/watch?v=lovcjT8J5Js&ab_channel=HackersRealm
    # https://github.com/talkdirty/knarrekcah/blob/master/cracking_the_coding_interview/trees_is_this_a_bst.ipynb
    def check_bst_recursive(root: node, lower_bound: int, upper_bound: int) -> bool:
        if root is None:
            return True
        
        if root.data > lower_bound and root.data < upper_bound:    
            return check_bst_recursive(root.left, lower_bound, root.data) and check_bst_recursive(root.right, root.data, upper_bound)
        else:
            return False
    
    return check_bst_recursive(root, 0, 10**4)

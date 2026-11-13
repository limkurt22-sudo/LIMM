"""Assessment 3.3: Binary Tree using the last name LIM.

Letters are inserted in order (L, I, M) using binary search tree rules:
smaller letters go left, larger letters go right.
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    # ---------- BFS (level-order) ----------
    def bfs(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # ---------- DFS ----------
    def preorder(self, node="start"):
        """Root, Left, Right"""
        if node == "start":
            node = self.root
        if node is None:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node="start"):
        """Left, Root, Right"""
        if node == "start":
            node = self.root
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    def postorder(self, node="start"):
        """Left, Right, Root"""
        if node == "start":
            node = self.root
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.value]


def arrow(items):
    return " -> ".join(items)


if __name__ == "__main__":
    tree = BinaryTree()
    for letter in "LIM":
        tree.insert(letter)

    print("BINARY TREE (LIM)")
    print("      L")
    print("     / \\")
    print("    I   M")
    print()
    print("BFS (level-order)        :", arrow(tree.bfs()))
    print("DFS Preorder (Root,L,R)  :", arrow(tree.preorder()))
    print("DFS Inorder (L,Root,R)   :", arrow(tree.inorder()))
    print("DFS Postorder (L,R,Root) :", arrow(tree.postorder()))
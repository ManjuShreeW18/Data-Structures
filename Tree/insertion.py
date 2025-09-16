class Node:
    def __init__(self, val):
        self.val = val
        self.left = None  #left and right children are none
        self.right = None


class BST:
    def __init__(self):
        self.root = None   # Initially tree is empty

    def insert(self, val):  # public method to insert a value
        self.root = self.insert_node(self.root, val)

    def insert_node(self, root, val):  # recursve help to insert
        if root is None:  # current node is none
            return Node(val)  # Insert new node here
        
        if val < root.val:          # If value is less than current node's value
            root.left = self.insert_node(root.left, val)

        elif val > root.val:
            root.right = self.insert_node(root.right, val)

        return root

    def search(self, val):
        return self.search_node(self.root, val)

    def search_node(self, root, val):
        if root is None:
            return False  # Reached empty spot, not found

        if val == root.val:
            return True  # found
        elif val < root.val:
            return self.search_node(root.left, val)  # LST

        else:
            return self.search_node(root.right, val)  # RST

    def delete(self, val):
        self.root = self.delete_node(self.root, val)  # Delete starting at root

    def delete_node(self, root, val):
        if not root:
            return None
        if val < root.val:
            root.left = self.delete_node(root.left, val)
        elif val > root.val:
            root.right = self.delete_node(root.right, val)
        else:
            # Node to delete found
            # Case 1: No child (leaf node)

            if not root.left and not root.right:
                return None
            # Case 2: One child (either left or right)

            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: Two children
            # Find the smallest node in the right subtree
            succ = root.right
            while succ.left:
                succ = succ.left  # Find leftmost node in right subtree
            root.val = succ.val   # Replace node's value with successor's value
            root.right = self.delete_node(root.right, succ.val)  # Delete successor node
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    def find_min(self):
        cur=self.root
        while cur and cur.left:
            cur=cur.left
        if cur:
            return cur.val
        return None
    
    def find_max(self):
        cur=self.root
        while cur and cur.right:
            cur=cur.right
        if cur:
            return cur.val
        return None


b1 = BST()
print("\n insertion")
b1.insert(8)
b1.insert(2)
b1.insert(9)
b1.insert(7)

print(b1.root.right.val)
print(b1.root.left.val)
print("\nsearch")
print(b1.search(9))
print(b1.search(90))

print("\ninorder before deletion")
b1.inorder(b1.root)
print("\ninorder after deletion")
b1.delete(2)
b1.inorder(b1.root)


print("\nInorder")
b1.inorder(b1.root)
print("\npreorder")
b1.preorder(b1.root)
print("\npostorder")
b1.postorder(b1.root)

print("\nMin:", b1.find_min())       
print("Max:", b1.find_max()) 
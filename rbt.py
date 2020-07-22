class TreeNode:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

    def __repr__(self):
        return 'TreeNode(%s)' % self.val

# 把节点当成树本身似乎更加灵活些
class RedBlackTree:
    def __init__(self, root):
        self.nil = TreeNode(None, 'b')
        self.root = root

    def inorder_walk(self):
        arr = []
        self._inorder_walk(self.root, arr)
        print(arr)

    def _inorder_walk(self, x, arr):
        if x is not None:
            self._inorder_walk(x.left, arr)
            arr.append(x)
            self._inorder_walk(x.right, arr)
    
    def search(self, k, mod=0):
        assert mod == 0 or mod == 1
        if mod == 0:
            self._serch(self.root, k)
        elif mod == 1:
            self._search_interative(self.root, k)
        else:
            raise ValueError('mode must be 0 or 1')

    def _serch(self, x, k):
        if x is None or x.val == k:
            return x
        if k < x.val:
            return self._serch(x.left, k)
        else:
            return self._serch(x.right, k)

    def _search_interative(self, x, k):
        while x and k != x.vl:
            if k < x.val:
                x = x.left
            else:
                x = x.right
        return x

    @classmethod
    def build(self, arr):
        root = TreeNode(arr[0])
        root.parent = root.left = root.roght = self.nil
        root.color = 'b'
        tree = BinarySearchTree(root)
        for item in arr[1:]:
            tree.insert(item)
        return tree


    def insert(self, v):
        self._insert(self.root, v)

    def _insert(self, root, v):
        if v < root.val:
            if root.left is self.nil:
                node = TreeNode(v)
                node.parent = root
                node.left = node.right = self.nil
                root.left = node
                self.insert_fixup(node)
            else:
                self._insert(root.left, v)
        else:
            if root.right is None:
                node = TreeNode(v)
                node.parent = root
                node.left = node.right = self.nil
                root.right = node
                self.insert_fixup(node)
            else:
                self._insert(root.right, v)
        

    def 

    def minimum(self):
        x = self.root
        while x.left:
            x = x.left
        return x
    
    def maximum(self):
        x = self.root
        while x.right:
            x = x.right
        return x

    def successor(self, x):
        if x.right:
            return BinarySearchTree(x.right).minimum()
        y = x.parent
        while y and x == y.right:
            x = y
            y = x.parent
        return y

    def predecesor(self, x):
        if x.left:
            return BinarySearchTree(x.left).maximum()
        y = x.parent
        while y and x == y.left:
            x = y
            y = x.parent
        return y


    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = BinarySearchTree(z.right).minimum()
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def right_rotat(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

if __name__ == '__main__':
    tree = RedBlackTree.build([15, 6, 18])
    tree.inorder_walk()
    tree.insert(20)
    tree.inorder_walk()
    node = tree.root
    tree.delete(node)
    tree.inorder_walk()

class Node:
    
    def __init__(self, key: int, left, right):
        self.key = key
        self.left = left
        self.right = right
        self.left_h = 0
        self.right_h = 0
        
class BinarySearchTree:
    def __init__(self, root: Node | None = None):
        self.root = root 
        
    def _min_key(self, _root: Node | str = "root"):
        if _root == "root": _root = self.root
        
        if _root is None: return
        
        if _root.left is None: return _root
        
        def left_search(r: Node):
            if r.left is None: 
                return r
            # else: print(f"{r.key}.left = {r.left.key}")
            return left_search(r.left)
            
        
        return left_search(_root)
    
    def _update_height(self, _root: None | str = "root"):
        if _root == "root": _root = self.root
        
        if _root is None:
            return (-1, -1)

        _root.left_h = max(self._update_height(_root.left)) + 1 if _root.left else 0
        _root.right_h = max(self._update_height(_root.right)) + 1 if _root.right else 0

        return (_root.left_h, _root.right_h)
    
    def height(self):
        def h(node):
            if node is None:
                return 0
            return 1 + max(h(node.left), h(node.right))

        return h(self.root)
    
    def exists(self, key: int, _root: Node | str = "root"):
        if _root == "root": _root = self.root
        
        if _root is None: return False
        
        if _root.key == key:
            # print(f"{key} exists")
            return _root
        elif key < _root.key:
            return self.exists(key, _root.left)
        elif key > _root.key:
            return self.exists(key, _root.right)

        
    
    def add(self, key: int, _root: Node | str = "root"):
        if _root == "root" and self.root is not None:
            _root = self.root
        elif _root == "root": 
            _root = Node(key, None, None)
            
        
        if _root is None: return
        
        if self.root is None:
            self.root = Node(key, None, None)
        else:
            if _root.right is None and key > _root.key:
                _root.right = Node(key, None, None)
            elif key > _root.key: 
                self.add(key, _root.right)
            elif _root.left is None and key < _root.key:
                _root.left = Node(key, None, None)
            elif key < _root.key: 
                self.add(key, _root.left)
            # self._update_height()
            
            
    def print(self, _root: Node | str = "root"):
        if self.root is None: print("Empty")
        
        if _root == "root": _root = self.root
        
        if _root is None: return
        
        print(_root.key, end = " ")
        
        if _root.left is not None: self.print(_root.left)
        if _root.right is not None: self.print(_root.right)
        
        
        
    def _del(self, key: int, _root: Node | str = "root"):
        if _root == "root": _root = self.root
                
        if _root is None: return
        
        if key < _root.key:
            _root.left = self._del(key, _root.left)
        elif key > _root.key:
            _root.right = self._del(key, _root.right)
        else:
            if _root.left is None:
                return _root.right
            elif _root.right is None:
                return _root.left

            v_to_replace = self._min_key(_root.right)
            _root.key = v_to_replace.key
            _root.right = self._del(v_to_replace.key, _root.right)

        return _root
    
    def delete(self, key: int):
        self.root = self._del(key)
        
bst = BinarySearchTree()

q = int(input())

for i in range(q):
    line = input()
    cmd, arg = line, None
    if len(line.split()) == 2: 
        cmd, arg = line.split()
    
    if cmd == "add":
        bst.add(int(arg)) 
    if cmd == "del":
        bst.delete(int(arg))
    if cmd == "exists":
        print("YES" if bst.exists(int(arg)) else "NO")
    if cmd == "print":
        bst.print()
        print()
    if cmd == "height":
        print(bst.height())
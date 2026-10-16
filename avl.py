class Node:
    def __init__(self, key: int, left, right):
        self.key = key
        self.left = left
        self.right = right
        self.left_h = 0
        self.right_h = 0
        
class BalancingBST:
    def __init__(self, root: Node | None = None):
        self.root = root 
        
    def _par(self, root: Node | str = "root"):
        if root == "root": return None
        
        cur = self.root
        parent = None
        
        while cur is not None and cur is not root:
            parent = cur
            if root.key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        
        return parent
            
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
       
    def _bal(self, root: Node | str = "root"):
        if root == "root": root = self.root
        
        if root is None: return 0
        
        return root.right_h - root.left_h
    
    def height(self, root: Node | str = "root"):
        if root == "root": root = self.root
        
        if root is None: return (0,0)
        
        return (root.left_h, root.right_h)
    
    def _update_height(self, root: Node | str = "root"):
        if root == "root": root = self.root
        
        if root is None: 
            return 
                
        root.left_h = max(self.height(root.left)) + 1 if root.left else 0
        root.right_h = max(self.height(root.right)) + 1 if root.right else 0
    
    def exists(self, key: int, root: Node | str = "root"):
        if root == "root": root = self.root
        if root is None: return False
        if root.key == key: return root
        
        if root.left and key < root.key: return self.exists(key, root.left)
        if root.right and key > root.key: return self.exists(key, root.right)
    
    def left(self, key: int = None, root: Node | str = "root"):
        if root == "root": root = self.root
        
        parent = None
        if key is not None:
            if not self.exists(key):
                return
            
            while root.key != key:
                # print(root.key)
                parent = root
                if key < root.key:
                    root = root.left
                elif key > root.key:
                    root = root.right
                else:
                    break
        else:
            parent = self._par(root)
            
        if root is None or root.right is None:
            return
        
        x = root
        y = root.right
        
        x.right = y.left
        y.left = x

        root = y
        
        if parent is None:
            self.root = y
        elif parent.left is x:
            parent.left = y
        else:
            parent.right = y
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def right(self, key: int = None, root: Node | str = "root"):
        if root == "root": root = self.root

        parent = None
        if key is not None:
            if not self.exists(key):
                return
            
            while root.key != key:
                # print(root.key)
                parent = root
                if key < root.key:
                    root = root.left
                elif key > root.key:
                    root = root.right
                else:
                    break
        else:
            parent = self._par(root)
            
        if root is None or root.left is None:
            return
    
        x = root
        y = root.left
        
        x.left = y.right
        y.right = x

        root = y
        
        if parent is None:
            self.root = y
        elif parent.left is x:
            parent.left = y
        else:
            parent.right = y
        
        self._update_height(x)
        self._update_height(y) 
        
        return y
                
    def _balance(self, root: Node | str = "root"):
        
        if root  == "root": root = self.root
        
        self._update_height(root)
        
        if self._bal(root) == 2:
            if self._bal(root.right) >= 0:
                root = self.left(root=root)
            else:
                self.right(root=root.right)
                root = self.left(root=root)
        if self._bal(root) == -2:
            if self._bal(root.left) <= 0:
                root = self.right(root=root)
            else:
                self.left(root=root.left)
                root = self.right(root=root)
        print("BALANCE", root.key, root.left_h, root.right_h, self._bal(root))
        return root          
    
    def imbalanced_insert(self, key: int, root: Node| str = "root"):
        if not self.root: 
            self.root = Node(key, None, None)
            return self.root
        
        if root == "root": 
            root = self.root 
                
        if key > root.key: 
            if root.right is None: 
                root.right = Node(key, None, None)
            else:
                root.right = self.imbalanced_insert(key, root.right)
        elif key < root.key:
            if root.left is None:
                root.left = Node(key, None, None)
            else:
                root.left = self.imbalanced_insert(key, root.left) 
        else: 
            return root
        
        return self._balance(root)
        
    def insert(self, key: int, root: Node | str = "root"):
        if root == "root":
            self.root = self.imbalanced_insert(key, self.root)
        else:
            return self.imbalanced_insert(key)
        
        return self.root
        
    def delete(self, key: int, root: Node | str = "root"):
        if root == "root":
            root = self.root

        if root is None:
            return None

        if key < root.key:
            root.left = self.delete(key, root.left)
        elif key > root.key:
            root.right = self.delete(key, root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            m = self._min_key(root.right)
            root.key = m.key
            root.right = self.delete(m.key, root.right)
            
        return self._balance(root)
            
        
    def print(self, _root: Node | str = "root"):
        if self.root is None: print("Empty")
        
        if _root == "root": _root = self.root
        
        if _root is None: return
        
        print(_root.key, end = " ")
        
        if _root.left is not None: self.print(_root.left)
        if _root.right is not None: self.print(_root.right)
            

avl = BalancingBST()


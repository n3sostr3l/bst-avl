from avl import BalancingBST, avl

m = int(input())

for r in range(m):
    l = input()
    c, k = None, None
    if len(l.split())==1: c = l
    else:
        c = l.split()[0]
        k = int(l.split()[1])
    
    if c == "print":
        avl.print()
        print()
    if c == "height":
        print(max(avl.height()) + 1 if avl.root else 0)
    if c == "root":
        print(avl.root.key if avl.root else "Empty")
    if c == "add":
        avl.insert(int(k))
    if c == "exists":
        print("YES" if avl.exists(int(k)) else "NO")
    if c == "del":
        avl.delete(int(k))
    if c == "prev":
        print(avl.prev(int(k)).key if avl.prev(int(k)) else "None")
    if c == "next":
        print(avl.next(int(k)).key if avl.next(int(k)) else "None")
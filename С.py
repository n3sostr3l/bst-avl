from avl import BalancingBST as AVL

avl = AVL()

n = int(input())

a = map(int, input().split())
for _ in a: avl.imbalanced_insert(_)

m = int(input())

for r in range(m):
    c, k = input().split()
    if c == "right": avl.right(int(k))
    if c == "left": avl.left(int(k))
    avl.print()
    print() 
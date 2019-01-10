rows=int(input())
columns=int(input())
X=[]
Z=[]
result = [[0,0,0], [0,0,0],
 [0,0,0]]
for x in range(rows):
  X11 = list(map(int,input().split()))
  X.append(X11)
for y in range(columns):
  Z11 = list(map(int,input().split()))
  Z.append(Z11)
A=X
B=Z
# print(X)
# print(Y)
result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*B)] 
                                for A_row in A] 
  
for r in result: 
    print(r) 
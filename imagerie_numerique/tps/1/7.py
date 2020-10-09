#Pour numpy
import numpy as np
from scipy.optimize import newton_krylov

#(a)
a= np.array([2,-3,4,1,0])
b= np.array([1,2,-5,2,4])
c= np.array([-1,3,0,1,2])

print((4*a)-(2*b)+c)

#(b)
print(((3*(-1))-17)/4)

#(c) false because we find (a= -13, 2a= -16, -a= -4)

#(d) 
A= np.array([[1,1],[2,3]])
b= np.array([5,0])
print(np.linalg.solve(A,b))

#(e)

a= np.array([[1,2,1],[-2,-1,5],[1,3,0]])

def B(x):
    b= np.array([[-1,3,7],[2,3,3],[4,-1,-6],[2,3,4]])
    return np.dot(x,b)

print(np.linalg.solve(a,[0,0,0]))
print(newton_krylov(B,[0,0,0,0]))

#(f)
a= np.array([1,2,3])
b= np.array([4,-5,6])
print(np.dot(a, np.transpose(b)))

#(g)
a= np.array([3,-3,1])
b= np.array([4,9,2])
print(np.dot(np.transpose(a), b))

#angle between the two vectors
print(np.arccos(np.dot(np.transpose(a), b)/(np.linalg.norm(a)*np.linalg.norm(b))))

#(h) c= 18 scalar product must be 0

#(i)
A= np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b= np.array([-2,1,0])

print(np.dot(A,b))

#(j) There are no solution because their dimention don't match

#(k) There are no solution because their dimention don't match

#(l) Yes because of commutativity

#(m) Yes because of associativity

#(n) No, (prove with example)
A= np.array([[3,2],[3,4]])
B= np.array([[2,3],[4,4]])
C= np.array([[0,4],[1,6]])
print(np.dot(np.dot(A,B),C))
print(np.dot(A,np.dot(B,C)))

#(o) No, (prove with example)
B= np.array([[2,3],[4,4]])
C= np.array([[0,4],[1,6]])
print(np.dot(B,C))
print(np.dot(C,B))

#(p)

B= np.array([[1,2,3], [4,5,6]])
C= np.array([[1,2],[3,4],[5,6]])
print(np.dot(B,C))

#(q)
M= np.array([[2,1,-1],[3,5,-7],[4,-5,-6]])
print(np.linalg.matrix_rank(M))

#(r)
A= np.array([[4,4],[2,-5]])
B= np.array([[1,1,2],[2,3,1],[3,4,-5]])
C= np.array([[1,0,0,3],[2,1,0,1],[3,0,5,4],[0,3,2,2]])

print(np.linalg.det(A))
print(np.linalg.det(B))
print(np.linalg.det(C))

#(s) if deti(M) != 0 it is inversible

M= np.array([[-1,1,1,0],[0,0,-1,0],[0,0,1,-1],[0,0,1,0]])

print(np.linalg.det(M))

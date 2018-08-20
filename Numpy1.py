import numpy as np

dt=np.dtype('float')
x=np.array([1.1,2.1,3.1],dtype=dt)
print(x)

matB=np.array([[3,1,9],[2,5,8],[4,7,6]])
print(matB.shape)

# A =np.array([-2,1],[1,5,-0.5])
# np.linalg.inv(A)
#
# np.linalg.det(A)
#
# np.linalg.matrix_rank(A)


x2d=np.arange(12).reshape(3,4)

print(x2d)

a=x2d[1][1:]
print(a)

print(a[0])
a[0]=-1
print(a[0])

nba=np.arange(12).reshape(4,3,order='f')

print(nba)

z=np.arange(9).reshape(3,3)
print(z)
z=np.zeros([5,5])
z+=np.arange(5)

print(z)

z=np.arange(10,dtype=np.int32)
z=z.astype(np.float32,copy=False)

print(z)
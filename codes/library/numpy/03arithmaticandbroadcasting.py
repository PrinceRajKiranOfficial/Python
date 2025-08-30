#arithmetic & Broadcasting
import numpy as np
a=np.array([1,2,3])
b=np.array([10,20,30])
print(a+b)#[11 22 33]
print(a*b)#[11 22 33]
print(np.sqrt(a))#[1.         1.41421356 1.73205081]
print(np.sqrt(b))#[3.16227766 4.47213595 5.47722558]




#Broadcasting
x = np.array([[1],[2],[3]])
y = ([10,20,30])
print(x+b)
#Each row of 'a' is broadcast over 'b'
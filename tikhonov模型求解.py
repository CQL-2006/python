import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
n = 20
A = np.vander(np.linspace(0,1,n) , increasing = True)
#np.slove()直接算
x_true = np.ones(n)#假定真实解全为1
b = A @ x_true + 0.1 * np.random.randn(n)
x_bad = np.linalg.lstsq(A , b , rcond = None)[0]#这是因为返回值有四个:解x,残差平方和,rankA，A的特征值

lambda_val = 1e-4
I = np.eye(n)

ATA = A.T @ A
ATb = A.T @ b
x_good = np.linalg.solve(ATA + lambda_val * I,ATb)

plt.figure(figsize=(10,5))
plt.plot(x_true,'g-o',label = 'Ture',markersize = 6)
plt.plot(x_bad,'r-o',label = 'Bad',markersize = 6)
plt.plot(x_good,'b-s',label = 'good',markersize = 6)

plt.title("Comparsion")
plt.xlabel('Index of x')
plt.ylabel('value of x')
plt.legend()
plt.grid(True,linestyle = '--',alpha = 0.5)
plt.ylim(-5,5)
plt.show()


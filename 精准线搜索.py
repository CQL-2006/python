import numpy as np
import matplotlib.pyplot as plt
import math
def f(x):
    return x[0]**2+2*x[1]**2

def grad_f(x):
    return np.array([2*x[0],4*x[1]])

def g_history(start_point,max_steps = 30,tol = 1e-7):
    x = np.array(start_point,dtype = float)
    
    x_old = [x.copy()]
    
    hx,hy,hf=[],[],[]
    
    for i in range(max_steps):
        
        hx.append(x_old[i][0])
        hy.append(x_old[i][1])
        hf.append(f(x_old[i]))
        
        A = np.array([[2,0],[0,4]])
        
        alpha = ( grad_f(x_old[i]) @ grad_f(x_old[i]) ) /(grad_f(x_old[i]) @ A @ grad_f(x_old[i]))
        
        x_1 = x_old[i] - alpha *grad_f(x_old[i])
        
        if abs(f(x_1)-f(x_old[i])) > tol:
            x_old.append(x_1)
        else:
            hx.append(x_1[0])
            hy.append(x_1[1])
            hf.append(f(x_1))
            print(f"f(x)最小值为{f(x_old[i]):.8f}")
            return x_old,hx,hy,hf
            break
x_resule,h_x,h_y,h_f = g_history([5,5])
fig,ax = plt.subplots(1,2)

#函数值与迭代次数图像
ax[0].plot(h_f,'b-o')
ax[0].set_yscale('log')
ax[0].set_title("function value")

#精准搜索路径
x_grid = np.linspace(-6,6,100)
y_grid = np.linspace(-6,6,100)
X,Y = np.meshgrid(x_grid,y_grid)
Z = X**2 + 2*Y**2
ax[1].contour(X,Y,Z,levels = 20,cmap = 'viridis',alpha = 0.5)
ax[1].plot(h_x,h_y,'r-o')
ax[1].set_title("road")

plt.show()
        

                   
        
            
        
            
        
        
        
        
    
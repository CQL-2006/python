import numpy as np
import matplotlib.pyplot as plt 
# fig,ax = plt.subplots(1,2) #第一个是行，第二个是列
# x = np.array([0,1,2,3,4,5])
# y = np.array([0,2,4,6,8,10])
# ax[0].plot(x,y,label = '469')
# # plt.plot(x,y,'red') #变红色
# # plt.plot(x,y,'o')   #显示每个点  
# ax[0].set_title("y=2x")
# ax[0].legend()
# x_1 = [0,1,2,3,4]
# y_1 = [235,74,95,2136,877]
# ax[1].plot(x_1,y_1,'o-',label = '236') #o-表示显示点同时连线
# #如果是四张就是ax[i,j]
# ax[1].legend() #使用plt.legend()只给最后一个显示
# plt.show()

def f(x):
    return x[0]**2+2*x[1]**2

def grad_f(x):
    return np.array([2*x[0],4*x[1]])

def record_decreas(start_point,step_size):
    x = np.array(start_point,dtype = float)
    
    step_number = []
    func_values = []
    for i in range(50):
        step_number.append(i)
        func_values.append(f(x))
        
        x = x - step_size*grad_f(x)
        
    return step_number,func_values

x1,alpha1 = record_decreas([5.0,5.0],step_size = 0.1)
x2,alpha2 = record_decreas([5.0,5.0],0.3)

plt.plot(x1,alpha1,'o-',label = 'samll step = 0.1')
plt.plot(x2,alpha2,'o-',label = 'big step = 0.3')  
plt.legend()
plt.show()
    
import numpy as np
import matplotlib.pyplot as plt 
fig,ax = plt.subplots(1,2) #第一个是行，第二个是列
x = np.array([0,1,2,3,4,5])
y = np.array([0,2,4,6,8,10])
ax[0].plot(x,y)
# plt.plot(x,y,'red') #变红色
# plt.plot(x,y,'o')   #显示每个点  
ax[0].set_title("y=2x")

x_1 = [0,1,2,3,4]
y_1 = [235,74,95,2136,877]
ax[1].plot(x_1,y_1,'o-') #o-表示显示点同时连线
#如果是四张就是ax[i,j]
plt.show()
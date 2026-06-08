import numpy as np
import matplotlib.pyplot as plt 
x = np.array([0,1,2,3,4,5])
y = np.array([0,2,4,6,8,10])
plt.plot(x,y)
# plt.plot(x,y,'red') #变红色
# plt.plot(x,y,'o')   #显示每个点  
plt.title("y=2x")
plt.show()

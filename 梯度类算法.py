# #使用固定步长最速下降法求解f(x,y)=x^2+2y^2极小值例子
# import numpy as np 
# import matplotlib.pyplot as plt
# def f(x):
#     return x[0]**2+2*x[1]**2

# def grad_f(x):
#     return np.array([2*x[0],4*x[1]])

# def steepest_descent(initial_x, learning_rate=0.1, tol=1e-6, max_iter=1000):
#     x = np.array(initial_x, dtype=float)
#     for i in range(max_iter):
#         g = grad_f(x)
#         if np.linalg.norm(g) < tol:
#             print(f"收敛于第 {i} 次迭代")
#             break
#         x = x - learning_rate * g
#     return x

# result_x = steepest_descent([1.0,2.0],learning_rate = 0.3)
# # print("最优解",result_x)
# # print("最小值",f(result_x))


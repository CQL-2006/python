import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    return x[0]**2 + 2 * x[1]**2

def grad_f(x):
    return np.array([2 * x[0], 4 * x[1]])

# 修改函数：增加历史记录功能
def steepest_descent_with_history(initial_x, learning_rate=0.1, tol=1e-6, max_iter=1000):
    x = np.array(initial_x, dtype=float)
    
    # 初始化列表用于存储历史数据
    history_x = [x.copy()]      # 存储每一步的坐标 [x, y],这个地方要用.copy不然history_x是指向x的指针，x变化之后也会变化
    history_f = [f(x)]          # 存储每一步的函数值
    
    for i in range(max_iter):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            print(f"收敛于第 {i} 次迭代")
            break
        x = x - learning_rate * g
        
        # 记录更新后的状态
        history_x.append(x.copy())
        history_f.append(f(x))
        
    # 转换为 numpy 数组方便绘图
    return np.array(history_x), np.array(history_f)

# 1. 执行计算
initial_point = [5.0, 5.0]  
lr = 0.3
hx, hf = steepest_descent_with_history(initial_point, learning_rate=lr)

print("最终最优解:", hx[-1]) #倒数第一个
print("最终最小值:", hf[-1])

# 2. 开始绘图
plt.figure(figsize=(14, 5))

# 图1: 函数值随迭代次数的变化 (收敛曲线)
plt.subplot(1, 3, 1)
iterations = range(len(hf))
plt.plot(iterations, hf, 'b-o', markersize=4, linewidth=1)
plt.title('Convergence Curve (f vs Iterations)')
plt.xlabel('Iteration Count (k)')
plt.ylabel('Objective Function Value f(x,y)')
plt.grid(True, linestyle='--', alpha=0.5)

# 图2: 梯度范数随迭代次数的变化
plt.subplot(1, 3, 2)
# 重新计算每一步的梯度范数
grad_norms = [np.linalg.norm(grad_f(x)) for x in hx]
plt.plot(iterations, grad_norms, 'r-s', markersize=4, linewidth=1)
plt.title('Gradient Norm vs Iterations')
plt.xlabel('Iteration Count (k)')
plt.ylabel('||Gradient||')
plt.yscale('log')  # 使用对数坐标，因为梯度下降是指数级接近0的,看起来方便一些
plt.grid(True, linestyle='--', alpha=0.5)

# 图3: 二维平面上的搜索轨迹 (等高线图+路径)
plt.subplot(1, 3, 3)
# 生成等高线背景
x_range = np.linspace(-6, 6, 400)
y_range = np.linspace(-6, 6, 400)
X, Y = np.meshgrid(x_range, y_range)
Z = X**2 + 2 * Y**2
contour = plt.contour(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)
plt.clabel(contour, inline=True, fontsize=8)

# 绘制搜索路径
plt.plot(hx[:, 0], hx[:, 1], 'white', marker='o', markersize=3, linewidth=1.5, label='Path')
plt.scatter(hx[0, 0], hx[0, 1], c='red', s=100, zorder=5, label='Start')   # 起点
plt.scatter(hx[-1, 0], hx[-1, 1], c='yellow', s=100, zorder=5, label='End') # 终点

plt.title('Optimization Path on Contour Map')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal') # 保持横纵坐标比例一致，避免图形变形

plt.tight_layout()
plt.show()
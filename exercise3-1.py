import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Tạo dữ liệu
np.random.seed(42)
x = np.random.normal(size=500)

np.random.seed(2)
y = np.random.normal(size=500) + 1

# Tính mật độ
density_x = gaussian_kde(x)
density_y = gaussian_kde(y)

# Lưới giá trị cho trục x
x_grid_x = np.linspace(min(x), max(x), 1000)
x_grid_y = np.linspace(min(y), max(y), 1000)

# Xác định giới hạn trục x và y
x_min = min(x.min(), y.min())
x_max = max(x.max(), y.max())
y_min = min(density_x(x_grid_x).min(), density_y(x_grid_y).min())
y_max = max(density_x(x_grid_x).max(), density_y(x_grid_y).max())

# Vẽ đồ thị
plt.figure(figsize=(8, 6))
plt.plot(x_grid_x, density_x(x_grid_x), color='red', linewidth=2, label='Density of x')
plt.plot(x_grid_y, density_y(x_grid_y), color='blue', linewidth=2, label='Density of y')
plt.title("Multiple curves with correct axis limits", fontsize=16)
plt.xlabel("", fontsize=12)
plt.xlim(x_min, x_max)  # Giới hạn trục x
plt.ylim(y_min, y_max)  # Giới hạn trục y
plt.legend()
plt.show()
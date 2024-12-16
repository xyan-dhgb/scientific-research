import numpy as np
import matplotlib.pyplot as plt

# Height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T #.T được sử dụng để chuyển vị ma trận X
# Weight (kh)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# Visualize data 
plt.plot(X, y, 'ro') # 'ro' là một chuỗi định dạng: 'r' là viết tắt của màu đỏ (red), 'o' là ký hiệu dùng để đánh dấu các điểm bằng hình tròn.
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

# Hàm bậc nhất: cân nặng = w_1*(chiều cao) + w_0
# Tạo X bar
one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one,X),axis=1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ',w)

# Preparing the fitting line 
w_0 = w[0][0] # Hệ số chặn (intercept)
w_1 = w[1][0] # Hệ số góc (slope),là mức độ dốc của đường thẳng, cho biết mức độ thay đổi của y khi x thay đổi
x0 = np.linspace(145, 185, 2)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro') # Vẽ các điểm dữ liệu ban đầu (
plt.plot(x0, y0) # the fitting line
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

# Predicting weights for heights 155 cm and 160 cm
height_155 = w_0 + w_1 * 155
height_160 = w_0 + w_1 * 160
print( u'Predict weight of person with height 155 cm: %.2f (kg), real number: 52 (kg)'  %(height_155) )
print( u'Predict weight of person with height 160 cm: %.2f (kg), real number: 56 (kg)'  %(height_160) )
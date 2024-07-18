import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Tạo dữ liệu mẫu (giả sử chúng ta có 2 đặc trưng và 2 lớp)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [1, 0], [2, 1], [3, 2], [4, 3]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
#0 là cho các trường hợp số trc nhỏ hơn số sau và 1 là ngược lại
# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Khởi tạo mô hình Logistic Regression
model = LogisticRegression()

# Huấn luyện mô hình trên tập huấn luyện
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình bằng độ chính xác
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
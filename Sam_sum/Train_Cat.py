import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Đường dẫn tới thư mục chứa dữ liệu hình ảnh
cat_folder = 'Data_train_Cat\Cat'
dog_folder = 'Data_train_Cat\Dog'

# Hàm để đọc và resize hình ảnh
def load_images_from_folder(folder, label):
    images = [] #tạo mảng 1 chiều để lưu trữ các ảnh dữ liệu
    labels = [] #tạo mảng 1 chiều để lưu trữ nhãn // trường hợp này là 2 ? Cat, Dog
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))# đọc ảnh đồng thời nạp vào biến img
        
        if img is not None:#nếu img không trống thì
            img = cv2.resize(img, (64, 64))  # Resize hình ảnh về kích thước 64x64
            img = img.flatten()  # Chuyển đổi hình ảnh thành vector
            images.append(img)#nạp vào images
            labels.append(label)
    return images, labels

# Tải dữ liệu hình ảnh
cat_images, cat_labels = load_images_from_folder(cat_folder, 0)  # 0 cho mèo
dog_images, dog_labels = load_images_from_folder(dog_folder, 1)  # 1 cho chó

# Kết hợp dữ liệu và nhãn
X = np.array(cat_images + dog_images)
y = np.array(cat_labels + dog_labels)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo mô hình KNN
knn = KNeighborsClassifier(n_neighbors=3)  # k=3

# Huấn luyện mô hình
knn.fit(X_train, y_train)

import matplotlib.pyplot as plt

# Hàm hiển thị hình ảnh
def show_image(image, label, prediction):
    plt.imshow(image.reshape(64, 64, 3))
    plt.title(f'True: {"Cat" if label == 0 else "Dog"}, Predicted: {"Cat" if prediction == 0 else "Dog"}')
    #plt.show()

# Dự đoán trên tập kiểm tra
y_pred = knn.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Hiển thị một số kết quả dự đoán

index = np.random.randint(0, len(X_test))
#show_image(X_test[index], y_test[index], y_pred[index])
    #X_test : hình ảnh
    #y_test : nhãn được gán

from PIL import Image
import matplotlib.pyplot as plt

# Đọc ảnh từ đường dẫn file
image_path = r'D:\My_Self_Studying\Python\Neural_Network\image\book.png'
img = Image.open(image_path)
img_gray = img.convert('L')
# Hiển thị ảnh
plt.imshow(img_gray, cmap="gray")
plt.axis('off')  # Tắt các trục
plt.show()

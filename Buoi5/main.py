import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import numpy as np

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        # Khởi tạo các biến
        self.original_image = None
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Tạo các thành phần GUI
        self.create_widgets()

    def create_widgets(self):
        # Tạo nút Load Image
        load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        load_button.pack()

        # Tạo nút Blur
        blur_button = tk.Button(self.root, text="Blur Image", command=self.blur_image)
        blur_button.pack()

        # Tạo nút Edge Detection
        edge_button = tk.Button(self.root, text="Edge Detection", command=self.edge_detection)
        edge_button.pack()

        # Tạo nút Convert Color
        convert_color_button = tk.Button(self.root, text="Convert Color", command=self.convert_color)
        convert_color_button.pack()

    def load_image(self):
        # Mở cửa sổ để chọn tệp ảnh
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Mở và hiển thị ảnh gốc
            pil_image = Image.open(file_path)
            self.original_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
            self.display_image(self.original_image)

    def display_image(self, image):
        # Chuyển đổi ảnh để hiển thị trong giao diện tkinter
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)
        tk_image = ImageTk.PhotoImage(pil_image)

        # Hiển thị ảnh trong label
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def blur_image(self):
        if self.original_image is not None:
            # Thực hiện làm mờ và hiển thị ảnh kết quả
            blurred_image = cv2.GaussianBlur(self.original_image, (15, 15), 0)
            self.display_image(blurred_image)

    def edge_detection(self):
        if self.original_image is not None:
            # Thực hiện phát hiện cạnh và hiển thị ảnh kết quả
            gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_image, 50, 150)
            self.display_image(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

    def convert_color(self):
        if self.original_image is not None:
            # Chuyển đổi màu và hiển thị ảnh kết quả
            converted_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
            self.display_image(converted_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

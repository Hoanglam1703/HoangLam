import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array

def tinh_tong_sv_dat_A():
    tong_sinh_vien_dat_A = np.sum(diemA >= 5)
    messagebox.showinfo("Tổng sinh viên đạt điểm A", f"Tổng sinh viên đạt điểm A: {tong_sinh_vien_dat_A}")

def tinh_diem_trung_binh_lop():
    diem_tb_lop = np.mean(in_data[:, 3:], axis=0)
    messagebox.showinfo("Điểm trung bình của các lớp", f"Điểm trung bình của các lớp: {diem_tb_lop}")

def ve_bieu_do_diem_cuoi_ky():
    diem_cuoi_ky_theo_lop = df.groupby('Lop')['DiemCuoiKy'].mean().reset_index(name='DiemCuoiKy')
    plt.figure(figsize=(10, 6))
    plt.bar(diem_cuoi_ky_theo_lop['Lop'], diem_cuoi_ky_theo_lop['DiemCuoiKy'], color='blue')
    plt.xlabel('Lớp')
    plt.ylabel('Điểm Cuối Kỳ Trung Bình')
    plt.title('So sánh điểm cuối kỳ của các lớp')
    plt.show()

def ve_do_thi_diem_A_va_Bc():
    plt.figure()
    plt.plot(range(len(diemA)), diemA, 'r-', label="DiemA")
    plt.plot(range(len(diemBc)), diemBc, 'g-', label="Diem B +")
    plt.xlabel('Lớp')
    plt.ylabel('Số sinh viên đạt điểm')
    plt.legend(loc='upper right')
    plt.show()

# Đọc dữ liệu từ tệp tin CSV
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])
diemA = in_data[:, 3]
diemBc = in_data[:, 4]

# Tạo giao diện GUI
root = tk.Tk()
root.title("Ứng dụng Quản lý Điểm")

# Nút tính tổng sinh viên đạt điểm A
btn_tong_sv_dat_A = tk.Button(root, text="Tổng SV Đạt A", command=tinh_tong_sv_dat_A)
btn_tong_sv_dat_A.pack()

# Nút tính điểm trung bình của các lớp
btn_diem_tb_lop = tk.Button(root, text="Điểm TB Các Lớp", command=tinh_diem_trung_binh_lop)
btn_diem_tb_lop.pack()

# Nút vẽ biểu đồ so sánh điểm cuối kỳ
btn_bieu_do_diem_cuoi_ky = tk.Button(root, text="Biểu đồ Điểm Cuối Kỳ", command=ve_bieu_do_diem_cuoi_ky)
btn_bieu_do_diem_cuoi_ky.pack()

# Nút vẽ đồ thị cho điểm A và Điểm Bc
btn_ve_do_thi = tk.Button(root, text="Vẽ Đồ Thị", command=ve_do_thi_diem_A_va_Bc)
btn_ve_do_thi.pack()

# Chạy giao diện GUI
root.mainloop()

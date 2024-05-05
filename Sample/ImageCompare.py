import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageChops

def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def compare_images():
    path1 = file_path1_entry.get()
    path2 = file_path2_entry.get()

    if path1 and path2:
        try:
            image1 = Image.open(path1)
            image2 = Image.open(path2)
            
            if image1.size != image2.size:
                result_label.config(text="Images have different sizes")
            else:
                diff = ImageChops.difference(image1, image2).getbbox()
                if diff is None:
                    result_label.config(text="Images are identical")
                else:
                    result_label.config(text="Images are different")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="Please select two image files")

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Image Comparator")

# ファイル1の参照ボタンとエントリ
file_path1_label = tk.Label(root, text="File 1 Path:")
file_path1_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
file_path1_entry = tk.Entry(root, width=40)
file_path1_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
browse_button1 = tk.Button(root, text="Browse", command=lambda: select_file(file_path1_entry))
browse_button1.grid(row=0, column=2, padx=5, pady=5)

# ファイル2の参照ボタンとエントリ
file_path2_label = tk.Label(root, text="File 2 Path:")
file_path2_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
file_path2_entry = tk.Entry(root, width=40)
file_path2_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
browse_button2 = tk.Button(root, text="Browse", command=lambda: select_file(file_path2_entry))
browse_button2.grid(row=1, column=2, padx=5, pady=5)

# 比較ボタン
compare_button = tk.Button(root, text="Compare", command=compare_images)
compare_button.grid(row=2, column=1, padx=5, pady=5)

# 比較結果表示用ラベル
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# アプリの実行
root.mainloop()

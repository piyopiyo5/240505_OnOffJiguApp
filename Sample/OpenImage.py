import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((500, 500))  # 画像をウィンドウサイズ内に縮小する
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo, width=500, height=500)  # ウィンドウサイズに合わせて画像サイズを調整
        image_label.image = photo

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Image Viewer")
root.geometry("500x500")  # ウィンドウサイズを指定

# 画像表示用ラベル
image_label = tk.Label(root)
image_label.pack(fill="both", expand=True)

# ファイル選択ボタン
open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack()

# アプリの実行
root.mainloop()

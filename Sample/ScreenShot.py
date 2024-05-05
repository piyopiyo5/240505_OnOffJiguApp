import tkinter as tk
from tkinter import filedialog
import pyautogui

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_path)

def take_screenshot():
    save_path = path_entry.get()
    if save_path:
        try:
            x1 = int(x1_entry.get())
            y1 = int(y1_entry.get())
            x2 = int(x2_entry.get())
            y2 = int(y2_entry.get())

            screenshot = pyautogui.screenshot()
            cropped_screenshot = screenshot.crop((x1, y1, x2, y2))
            cropped_screenshot.save(f"{save_path}/screenshot.png")
            status_label.config(text="Screenshot saved successfully!", fg="green")
        except ValueError:
            status_label.config(text="Please enter valid integer values for coordinates.", fg="red")
    else:
        status_label.config(text="Please select a folder to save the screenshot.", fg="red")

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Screenshot Cropper")

# 入力欄
path_label = tk.Label(root, text="Save Path:")
path_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
path_entry = tk.Entry(root, width=40)
path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

x1_label = tk.Label(root, text="X1:")
x1_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
x1_entry = tk.Entry(root)
x1_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

y1_label = tk.Label(root, text="Y1:")
y1_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
y1_entry = tk.Entry(root)
y1_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

x2_label = tk.Label(root, text="X2:")
x2_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
x2_entry = tk.Entry(root)
x2_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")

y2_label = tk.Label(root, text="Y2:")
y2_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
y2_entry = tk.Entry(root)
y2_entry.grid(row=4, column=1, padx=5, pady=5, sticky="we")

# 参照ボタン
browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# スクリーンショットボタン
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.grid(row=5, column=1, padx=5, pady=5)

# ステータス表示用ラベル
status_label = tk.Label(root, text="")
status_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# アプリの実行
root.mainloop()

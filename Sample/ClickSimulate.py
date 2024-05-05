import tkinter as tk
import pyautogui

def simulate_click():
    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
        pyautogui.click(x, y)
        status_label.config(text="Click simulated successfully!", fg="green")
    except ValueError:
        status_label.config(text="Please enter valid integer values for X and Y.", fg="red")

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Click Simulator")

# ウィンドウサイズの設定
root.geometry("300x150")

# X座標の入力欄
x_label = tk.Label(root, text="X Coordinate:")
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()

# Y座標の入力欄
y_label = tk.Label(root, text="Y Coordinate:")
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()

# クリックシミュレートボタン
click_button = tk.Button(root, text="Simulate Click", command=simulate_click)
click_button.pack(pady=10)

# ステータス表示用ラベル
status_label = tk.Label(root, text="")
status_label.pack()

# アプリの実行
root.mainloop()

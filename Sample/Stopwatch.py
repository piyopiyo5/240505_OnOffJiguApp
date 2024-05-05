import tkinter as tk
import time

def start_timer():
    global running, start_time, elapsed_time
    if not running:
        running = True
        start_time = time.time()

def stop_timer():
    global running, elapsed_time
    if running:
        running = False

def reset_timer():
    global running, start_time, elapsed_time
    running = False
    start_time = 0
    elapsed_time = 0
    show_time()

def show_time():
    global elapsed_time, time_label
    if running:
        elapsed_time = time.time() - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    time_label.config(text=time_string)
    time_label.after(100, show_time)

# グローバル変数
running = False
start_time = 0
elapsed_time = 0

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Stopwatch")

# 時間表示ラベル
time_label = tk.Label(root, text="00:00:00", font=("Arial", 24))
time_label.pack(pady=20)

# スタートボタン
start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack(side=tk.LEFT, padx=10)

# ストップボタン
stop_button = tk.Button(root, text="Stop", command=stop_timer)
stop_button.pack(side=tk.LEFT, padx=10)

# リセットボタン
reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack(side=tk.LEFT, padx=10)

# アプリの実行
show_time()
root.mainloop()

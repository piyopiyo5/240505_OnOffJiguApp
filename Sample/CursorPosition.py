import tkinter as tk

def update_position(event):
    x, y = event.x_root, event.y_root  # ウィンドウ外のカーソル座標を取得
    position_label.config(text=f'X: {x}, Y: {y}')

def space_pressed(event):
    if event.keysym == "space":
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # ウィンドウ内のカーソル座標を取得
        position_label.config(text=f'X: {x}, Y: {y}')

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Cursor Position Tracker")

# ウィンドウサイズの設定
root.geometry("300x100")

# カーソル座標を表示するラベル
position_label = tk.Label(root, text="")
position_label.pack(pady=10)

# キーボードイベントをバインド
root.bind('<Key>', space_pressed)  # キーが押されたとき

# アプリの実行
root.mainloop()

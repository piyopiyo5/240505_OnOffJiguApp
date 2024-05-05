import tkinter as tk
from tkinter import filedialog
import pyautogui
from PIL import Image, ImageTk

# 変数初期化
RowNumber = 0
save_path = ""

def space_pressed(event):
    if event.keysym == "space":
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # ウィンドウ内のカーソル座標を取得
        # position_label.config(text=f'X: {x}, Y: {y}')
        click_x_entry.delete(0, tk.END)
        click_x_entry.insert(0, x)
        click_y_entry.delete(0, tk.END)
        click_y_entry.insert(0, y)
    if event.keysym == "1":
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # ウィンドウ内のカーソル座標を取得
        x1_entry.delete(0, tk.END)
        x1_entry.insert(0, x)
        y1_entry.delete(0, tk.END)
        y1_entry.insert(0, y)
    if event.keysym == "2":
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # ウィンドウ内のカーソル座標を取得
        x2_entry.delete(0, tk.END)
        x2_entry.insert(0, x)
        y2_entry.delete(0, tk.END)
        y2_entry.insert(0, y)

def simulate_click():
    try:
        x = int(click_x_entry.get())
        y = int(click_y_entry.get())
        pyautogui.click(x, y)
        status_label.config(text="Click simulated successfully!", fg="green")
    except ValueError:
        status_label.config(text="Please enter valid integer values for X and Y.", fg="red")
        
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_path)
        
def open_file():
    file_path = f"{path_entry.get()}/screenshot.png"
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # 画像をウィンドウサイズ内に縮小する
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo, width=300, height=300)  # ウィンドウサイズに合わせて画像サイズを調整
        image_label.image = photo
        
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
            open_file()
            status_label.config(text="Screenshot saved successfully!", fg="green")
        except ValueError:
            status_label.config(text="Please enter valid integer values for coordinates.", fg="red")
    else:
        status_label.config(text="Please select a folder to save the screenshot.", fg="red")


# Tkinterウィンドウの作成
root = tk.Tk()
root.title("AutoClicker Ver1.0.0")

# ウィンドウサイズの設定
root.geometry("1920x1000")

# クリック座標ラベル
RowNumber+=1
ClickTarget_label = tk.Label(root, text = "ClickTarget")
ClickTarget_label.grid(row=RowNumber, column=0, padx=5, pady=5, sticky="w")

# X座標の入力欄
RowNumber+=1
click_x_label = tk.Label(root, text="X :")
click_x_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
click_x_entry = tk.Entry(root)
click_x_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

# Y座標の入力欄
RowNumber+=1
click_y_label = tk.Label(root, text="Y :")
click_y_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
click_y_entry = tk.Entry(root)
click_y_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

# クリックシミュレートボタン
RowNumber+=1
click_button = tk.Button(root, text="Simulate Click", command=simulate_click)
# click_button.grid(row=3, column=0, padx=5, pady=5)
click_button.grid(row=RowNumber, column=1, padx=5, pady=5, columnspan=3)

# スクショ座標ラベル
RowNumber+=1
ClickTarget_label = tk.Label(root, text = "ScreenShot")
ClickTarget_label.grid(row=RowNumber, column=0, padx=5, pady=5, sticky="w")

# 保存先
RowNumber+=1
path_label = tk.Label(root, text="Save Path:")
path_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
path_entry = tk.Entry(root, width=40)
path_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")
browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.grid(row=RowNumber, column=3, padx=5, pady=5)

# 座標１
RowNumber+=1
x1_label = tk.Label(root, text="X1:")
x1_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
x1_entry = tk.Entry(root)
x1_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

RowNumber+=1
y1_label = tk.Label(root, text="Y1:")
y1_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
y1_entry = tk.Entry(root)
y1_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

# 座標２
RowNumber+=1
x2_label = tk.Label(root, text="X2:")
x2_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
x2_entry = tk.Entry(root)
x2_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

RowNumber+=1
y2_label = tk.Label(root, text="Y2:")
y2_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
y2_entry = tk.Entry(root)
y2_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

# スクリーンショットボタン
RowNumber+=1
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.grid(row=RowNumber, column=1, padx=5, pady=5,columnspan=5)

# 画像表示用ラベル
RowNumber+=1
image_label = tk.Label(root)
image_label.grid(row=RowNumber, column=1, padx=5, pady=5, columnspan=5)

# ステータス表示用ラベル
RowNumber+=1
status_label = tk.Label(root, text="")
status_label.grid(row=RowNumber, column=1, padx=5, pady=5, columnspan=5)


# キーボードイベントをバインド
root.bind('<Key>', space_pressed)  # キーが押されたとき

# アプリの実行
root.mainloop()

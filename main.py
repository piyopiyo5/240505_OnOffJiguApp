import tkinter as tk
from tkinter import filedialog
import pyautogui
from PIL import Image, ImageTk, ImageChops

# 変数初期化
RowNumber = 0
save_dir_path = ""
save_file_path = ""
save_file_no = "1"
running_state = False
setting_state = False

def space_pressed(event):
    if event.keysym == "space":
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # ウィンドウ内のカーソル座標を取得
        # position_label.config(text=f'X: {x}, Y: {y}')
        click_x_entry.delete(0, tk.END)
        click_x_entry.insert(0, x)
        click_y_entry.delete(0, tk.END)
        click_y_entry.insert(0, y)
    if event.keysym == "1" and setting_state:
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # ウィンドウ内のカーソル座標を取得
        x1_entry.delete(0, tk.END)
        x1_entry.insert(0, x)
        y1_entry.delete(0, tk.END)
        y1_entry.insert(0, y)
    if event.keysym == "2" and setting_state:
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
    global save_file_path
    if save_file_path:
        image = Image.open(save_file_path)
        image.thumbnail((300, 300))  # 画像をウィンドウサイズ内に縮小する
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo, width=300, height=300)  # ウィンドウサイズに合わせて画像サイズを調整
        image_label.image = photo
        
def take_screenshot():
    global save_dir_path, save_file_path, save_file_no
    save_dir_path = path_entry.get()
    if save_dir_path:
        save_file_path = f"{save_dir_path}/screenshot{save_file_no}.png"
        try:
            x1 = int(x1_entry.get())
            y1 = int(y1_entry.get())
            x2 = int(x2_entry.get())
            y2 = int(y2_entry.get())

            screenshot = pyautogui.screenshot()
            cropped_screenshot = screenshot.crop((x1, y1, x2, y2))
            cropped_screenshot.save(save_file_path)
            open_file()
            status_label.config(text="Screenshot saved successfully!", fg="green")
            if save_file_no == "1":
                save_file_no = "2"
            else:
                save_file_no = "1"
        except ValueError:
            status_label.config(text="Please enter valid integer values for coordinates.", fg="red")
    else:
        status_label.config(text="Please select a folder to save the screenshot.", fg="red")
        
def compare_images():
    global save_dir_path
    path1 = f"{save_dir_path}/screenshot1.png"
    path2 = f"{save_dir_path}/screenshot2.png"

    if path1 and path2:
        try:
            image1 = Image.open(path1)
            image2 = Image.open(path2)
            
            if image1.size != image2.size:
                status_label.config(text="Images have different sizes")
            else:
                diff = ImageChops.difference(image1, image2).getbbox()
                if diff is None:
                    status_label.config(text="Images are identical")
                else:
                    status_label.config(text="Images are different")
        except Exception as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Please select two image files")
        
def start_stop_running():
    global running_state
    if running_state:
        running_state = False
        running_status_label.config(text="")
        start_stop_button.config(text="Start")
    else:
        running_state = True
        running_status_label.config(text="RUNNING")
        loop_exe()
        
def loop_exe():
    global running_state, running_status_label
    try:
        interval_time = int(interval_entry.get()) * 1000
        if running_state:
            take_screenshot()
            compare_images()
            running_status_label.after(interval_time, loop_exe)
    except ValueError:
        status_label.config(text="Invalid interval. Please enter a number.")
        running_state = False
        running_status_label.config(text="STOP")
        
def set_points():
    global setting_state
    if setting_state:
        setting_state = False
        set_points_label.config(text="")
    else:
        setting_state = True
        set_points_label.config(text="Setting Now")


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

# 座標設定
RowNumber+=1
set_points_button = tk.Button(root, text="SetPoints", command=set_points)
set_points_button.grid(row=RowNumber, column=1, padx=5, pady=5)
set_points_label = tk.Label(root, text="")
set_points_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")

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

# 比較ボタン
RowNumber+=1
compare_button = tk.Button(root, text="Compare", command=compare_images)
compare_button.grid(row=RowNumber, column=1, padx=5, pady=5,columnspan=5)

# インターバル設定
RowNumber+=1
interval_label = tk.Label(root, text="Interval:")
interval_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
interval_entry = tk.Entry(root)
interval_entry.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="we")

# スタートストップボタン
RowNumber+=1
start_stop_button = tk.Button(root, text="Start", command=start_stop_running)
start_stop_button.grid(row=RowNumber, column=1, padx=5, pady=5, columnspan=5)

# RUNNINGステータス表示ラベル
RowNumber+=1
running_status_label = tk.Label(root, text="STOP")
running_status_label.grid(row=RowNumber, column=1, padx=5, pady=5, columnspan=5)

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

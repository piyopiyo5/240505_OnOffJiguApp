import tkinter as tk
from tkinter import filedialog
import pyautogui
from PIL import Image, ImageTk, ImageChops
import time

# Constants -------------------------------------------------------------------
ON = 1
OFF = 0

# Variavles -------------------------------------------------------------------
RowNumber = 0
SetActiveFlg1stTg = False
SetActiveFlg2ndTg = False
SetActiveFlgEdge1 = False
SetActiveFlgEdge2 = False
RunningState = False
SaveDirPath = ""
SaveFilePath = ""
SaveFileIdx = "1"

# Functions --------------------------------------------------------------------------
def ReactToKey(event):
    global SetActiveFlg1stTg, SetActiveFlg2ndTg, SetActiveFlgEdge1, SetActiveFlgEdge2
    if event.keysym == "space":
        x, y = root.winfo_pointerx(), root.winfo_pointery()  # カーソル座標を取得
        if SetActiveFlg1stTg == True:
            ClickTarget_1st_X_entry.delete(0, tk.END)
            ClickTarget_1st_X_entry.insert(0, x)
            ClickTarget_1st_Y_entry.delete(0, tk.END)
            ClickTarget_1st_Y_entry.insert(0, y)
            SetActiveFlg1stTg = False
            ClickTarget_1st_Set_button.config(text="Set")
        if SetActiveFlg2ndTg == True:
            ClickTarget_2nd_X_entry.delete(0, tk.END)
            ClickTarget_2nd_X_entry.insert(0, x)
            ClickTarget_2nd_Y_entry.delete(0, tk.END)
            ClickTarget_2nd_Y_entry.insert(0, y)
            SetActiveFlg2ndTg = False
            ClickTarget_2nd_Set_button.config(text="Set")
        if SetActiveFlgEdge1 == True:
            ScreenShotEdge1_X_entry.delete(0, tk.END)
            ScreenShotEdge1_X_entry.insert(0, x)
            ScreenShotEdge1_Y_entry.delete(0, tk.END)
            ScreenShotEdge1_Y_entry.insert(0, y)
            SetActiveFlgEdge1 = False
            ScreenShotEdge1_Set_button.config(text="Set")
        if SetActiveFlgEdge2 == True:
            ScreenShotEdge2_X_entry.delete(0, tk.END)
            ScreenShotEdge2_X_entry.insert(0, x)
            ScreenShotEdge2_Y_entry.delete(0, tk.END)
            ScreenShotEdge2_Y_entry.insert(0, y) 
            SetActiveFlgEdge2 = False
            ScreenShotEdge2_Set_button.config(text="Set")
        
def Set1stClickTarget():
    global SetActiveFlg1stTg
    if SetActiveFlg1stTg:
        SetActiveFlg1stTg = False
        ClickTarget_1st_Set_button.config(text="Set")
    else:
        SetActiveFlg1stTg = True
        ClickTarget_1st_Set_button.config(text="OK")

def Set2ndClickTarget():
    global SetActiveFlg2ndTg
    if SetActiveFlg2ndTg:
        SetActiveFlg2ndTg = False
        ClickTarget_2nd_Set_button.config(text="Set")
    else:
        SetActiveFlg2ndTg = True
        ClickTarget_2nd_Set_button.config(text="OK")

def SelectSavePath():
    folder_path = filedialog.askdirectory()
    if folder_path:
        SavePath_entry.delete(0, tk.END)
        SavePath_entry.insert(0, folder_path)

def SetScreenShotEdge1():
    global SetActiveFlgEdge1
    if SetActiveFlgEdge1:
        SetActiveFlgEdge1 = False
        ScreenShotEdge1_Set_button.config(text="Set")
    else:
        SetActiveFlgEdge1 = True
        ScreenShotEdge1_Set_button.config(text="OK")

def SetScreenShotEdge2():
    global SetActiveFlgEdge2
    if SetActiveFlgEdge2:
        SetActiveFlgEdge2 = False
        ScreenShotEdge2_Set_button.config(text="Set")
    else:
        SetActiveFlgEdge2 = True
        ScreenShotEdge2_Set_button.config(text="OK")

def StartStopRunning():
    global RunningState
    if RunningState:
        RunningState = False
        RunningState_label.config(text="State:STOP")
        StartStop_button.config(text="START")
    else:
        RunningState = True
        RunningState_label.config(text="State:RUNNING")
        StartStop_button.config(text="STOP")
        TakeScreenShot() # １枚目のスクショを先に撮っておく
        LoopMain()

def ResetClickCycles():
    ClickCyclesValue_label.config(text="0")

def SimulateClick():
    # Wait Time
    time.sleep(int(PreWaitTime_entry.get()))
    
    # 1st Click
    try:
        x = int(ClickTarget_1st_X_entry.get())
        y = int(ClickTarget_1st_Y_entry.get())
        pyautogui.click(x, y)
        
        # Wait Time
        time.sleep(int(WaitTime_entry.get()))
        
        # 2nd Click
        try:
            x = int(ClickTarget_2nd_X_entry.get())
            y = int(ClickTarget_2nd_Y_entry.get())
            pyautogui.click(x, y)
            CycleTimeTmp = int(ClickCyclesValue_label.cget("text")) + 1
            ClickCyclesValue_label.config(text=str(CycleTimeTmp))
        except ValueError:
            status_label.config(text="Please enter valid integer values for X and Y.", fg="red")
            
    except ValueError:
        status_label.config(text="Please enter valid integer values for X and Y.", fg="red")
        
def TakeScreenShot():
    global SaveDirPath, SaveFilePath, SaveFileIdx
    SaveDirPath = SavePath_entry.get()
    if SaveDirPath:
        SaveFilePath = f"{SaveDirPath}/screenshot{SaveFileIdx}.png"
        try:
            x1 = int(ScreenShotEdge1_X_entry.get())
            y1 = int(ScreenShotEdge1_Y_entry.get())
            x2 = int(ScreenShotEdge2_X_entry.get())
            y2 = int(ScreenShotEdge2_Y_entry.get())

            screenshot = pyautogui.screenshot()
            cropped_screenshot = screenshot.crop((x1, y1, x2, y2))
            cropped_screenshot.save(SaveFilePath)
            open_file(SaveFilePath)
            # open_file()
            # status_label.config(text="Screenshot saved successfully!", fg="green")
            if SaveFileIdx == "1":
                SaveFileIdx = "2"
            else:
                SaveFileIdx = "1"
        except ValueError:
            status_label.config(text="Please enter valid integer values for coordinates.", fg="red")
    else:
        status_label.config(text="Please select a folder to save the screenshot.", fg="red")

def CompareImages():
    global SaveDirPath
    path1 = f"{SaveDirPath}/screenshot1.png"
    path2 = f"{SaveDirPath}/screenshot2.png"

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
                    status_label.config(text="====Images are different====")
                    if click_onoff_var.get() == ON:
                        SimulateClick()
        except Exception as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Please select two image files")
        
def open_file(savefilepath):
    file_path = savefilepath
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # 画像をウィンドウサイズ内に縮小する
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo, width=300, height=300)  # ウィンドウサイズに合わせて画像サイズを調整
        image_label.image = photo

def LoopMain():
    global RunningState
    try:
        interval_time = int(IntervalTime_entry.get()) * 1000
        if RunningState:
            TakeScreenShot()
            CompareImages()
            RunningState_label.after(interval_time, LoopMain)
    except ValueError:
        status_label.config(text="Invalid interval. Please enter a number.")
        RunningState = False
        RunningState_label.config(text="State:STOP")
        StartStop_button.config(text="START")
        
# main --------------------------------------------------------------------------------------------
# Tkinterウィンドウの作成
root = tk.Tk()
root.title("AutoClicker Ver1.0.1")

# ウィンドウサイズの設定
DisplaySize_width, DisplaySize_height = pyautogui.size()
root.geometry("{}x{}".format(DisplaySize_width,DisplaySize_height))

# ClickTarget
RowNumber+=1
ClickTarget_label = tk.Label(root, text = "ClickTarget")
ClickTarget_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")

RowNumber+=1
click_onoff_var = tk.IntVar()
ClickTarget_radiobutton_on = tk.Radiobutton(root, value=ON, variable=click_onoff_var, text="ON")
ClickTarget_radiobutton_on.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
ClickTarget_radiobutton_off = tk.Radiobutton(root, value=OFF, variable=click_onoff_var, text="OFF")
ClickTarget_radiobutton_off.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")

RowNumber+=1
PreWaitTime_label = tk.Label(root, text = "PreWaitTime [s]")
PreWaitTime_label.grid(row=RowNumber, column=6, padx=5, pady=5, sticky="w")
PreWaitTime_entry = tk.Entry(root, width=4)
PreWaitTime_entry.grid(row=RowNumber, column=7, padx=5, pady=5, sticky="w")

RowNumber+=1
ClickTarget_X_label = tk.Label(root, text = "X")
ClickTarget_X_label.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ClickTarget_Y_label = tk.Label(root, text = "Y")
ClickTarget_Y_label.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")

RowNumber+=1
ClickTarget_1st_label = tk.Label(root, text = "1st Click")
ClickTarget_1st_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
ClickTarget_1st_X_entry = tk.Entry(root, width=6)
ClickTarget_1st_X_entry.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ClickTarget_1st_Y_entry = tk.Entry(root, width=6)
ClickTarget_1st_Y_entry.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")
ClickTarget_1st_Set_button = tk.Button(root, text="Set", command=Set1stClickTarget)
ClickTarget_1st_Set_button.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w")

RowNumber+=1
WaitTime_label = tk.Label(root, text = "WaitTime [s]")
WaitTime_label.grid(row=RowNumber, column=6, padx=5, pady=5, sticky="w")
WaitTime_entry = tk.Entry(root, width=4)
WaitTime_entry.grid(row=RowNumber, column=7, padx=5, pady=5, sticky="w")

RowNumber+=1
ClickTarget_2nd_label = tk.Label(root, text = "2nd Click")
ClickTarget_2nd_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
ClickTarget_2nd_X_entry = tk.Entry(root, width=6)
ClickTarget_2nd_X_entry.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ClickTarget_2nd_Y_entry = tk.Entry(root, width=6)
ClickTarget_2nd_Y_entry.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")
ClickTarget_2nd_Set_button = tk.Button(root, text="Set", command=Set2ndClickTarget)
ClickTarget_2nd_Set_button.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w")

# ScreenShot
RowNumber+=1
ScreenShot_label = tk.Label(root, text = "ScreenShot")
ScreenShot_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")

RowNumber+=1
ClickTarget_X_label = tk.Label(root, text = "X")
ClickTarget_X_label.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ClickTarget_Y_label = tk.Label(root, text = "Y")
ClickTarget_Y_label.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")

RowNumber+=1
ScreenShotEdge1_label = tk.Label(root, text = "Edge1")
ScreenShotEdge1_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
ScreenShotEdge1_X_entry = tk.Entry(root, width=6)
ScreenShotEdge1_X_entry.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ScreenShotEdge1_Y_entry = tk.Entry(root, width=6)
ScreenShotEdge1_Y_entry.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")
ScreenShotEdge1_Set_button = tk.Button(root, text="Set", command=SetScreenShotEdge1)
ScreenShotEdge1_Set_button.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w")

RowNumber+=1
ScreenShotEdge2_label = tk.Label(root, text = "Edge2")
ScreenShotEdge2_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
ScreenShotEdge2_X_entry = tk.Entry(root, width=6)
ScreenShotEdge2_X_entry.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ScreenShotEdge2_Y_entry = tk.Entry(root, width=6)
ScreenShotEdge2_Y_entry.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")
ScreenShotEdge2_Set_button = tk.Button(root, text="Set", command=SetScreenShotEdge2)
ScreenShotEdge2_Set_button.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w")

RowNumber+=1
SavePath_label = tk.Label(root, text = "SavePath")
SavePath_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
SavePath_entry = tk.Entry(root, width=13)
SavePath_entry.grid(row=RowNumber, column=3, columnspan=2, padx=5, pady=5, sticky="w")
SavePathBrowse_button = tk.Button(root, text="Select", command=SelectSavePath)
SavePathBrowse_button.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w")

# Control
RowNumber+=1
Control_label = tk.Label(root, text = "Control")
Control_label.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")

RowNumber+=1
IntervalTime_label = tk.Label(root, text = "Interval [s]")
IntervalTime_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
IntervalTime_entry = tk.Entry(root, width=6)
IntervalTime_entry.grid(row=RowNumber, column=3, columnspan=2, padx=5, pady=5, sticky="w")
# IntervalTimeLast_label = tk.Label(root, text = "")
# IntervalTimeLast_label.grid(row=RowNumber, column=4, padx=5, pady=5, sticky="w")

RowNumber+=1
StartStop_button = tk.Button(root, text="START", command=StartStopRunning, width=12)
StartStop_button.grid(row=RowNumber, column=3, columnspan=2, padx=5, pady=5)
RunningState_label = tk.Label(root, text = "State:STOP", width=20)
RunningState_label.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w", columnspan=3)

RowNumber+=1
ClickCycles_label = tk.Label(root, text = "ClickCycles")
ClickCycles_label.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
ClickCyclesValue_label = tk.Label(root, text = "0")
ClickCyclesValue_label.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
ClickCyclesReset_button = tk.Button(root, text="Reset", command=ResetClickCycles)
ClickCyclesReset_button.grid(row=RowNumber, column=5, padx=5, pady=5)

# ステータス表示用ラベル
RowNumber+=1
status_label = tk.Label(root, text="")
status_label.grid(row=RowNumber, column=2, padx=5, pady=5, columnspan=5)

# 画像表示用ラベル
RowNumber+=1
image_label = tk.Label(root)
image_label.grid(row=RowNumber, column=2, padx=5, pady=5, columnspan=5)

# キーボードイベントをバインド
root.bind('<Key>', ReactToKey)  # キーが押されたとき

# アプリの実行
root.mainloop()

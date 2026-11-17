import tkinter as tk

# ================= 配置区 =================
WINDOW_WIDTH = 700   # 遮罩的宽度（你可以自己改）
WINDOW_HEIGHT = 30   # 遮罩的高度（你可以自己改）
BG_COLOR = "gray"   # 遮罩的颜色（纯黑）
ALPHA = 0.85         # 透明度（1.0 完全不透明，0.0 完全透明，0.85 是磨砂效果）
# ==========================================

def close_app(event):
    """右键点击窗口时，直接关闭程序"""
    root.destroy()

def start_move(event):
    """记录鼠标按下时的位置"""
    root.x = event.x
    root.y = event.y

def stop_move(event):
    """计算并移动窗口"""
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

root = tk.Tk()

# 🌟 核心设置：无边框、永远置顶
root.overrideredirect(True) 
root.attributes('-topmost', True) 

# 设置窗口大小和颜色
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+500+300") # +500+300是初始出现的位置
root.configure(bg=BG_COLOR)

# 绑定鼠标事件：左键拖动，右键关闭
root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", stop_move)
root.bind("<Button-3>", close_app)

# 运行
root.mainloop()
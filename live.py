# 导入模块
import time
from playsound import playsound

# 输入专注时间和休息时间（单位为分钟）
focus_time = int(input("请输入专注时间（分钟）："))
break_time = int(input("请输入休息时间（分钟）："))

# 定义一个函数，用于显示倒计时
def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        # 将秒数转换为分和秒
        m, s = divmod(seconds, 60)
        # 格式化输出
        print(f"{m:02d}:{s:02d}", end="\r")
        # 每秒减一
        seconds -= 1
        # 暂停一秒
        time.sleep(1)

# 定义一个函数，用于播放声音
def play_sound(file):
    # 播放指定的音频文件
    playsound(file)
    # 打印提示信息
    print(f"播放 {file}")

# 开始专注时钟
print("开始专注时钟")
while True:
    # 开始专注
    print("开始专注")
    # 倒计时专注时间
    countdown(focus_time)
    # 播放专注结束的声音
    play_sound("focus_end.mp3")
    # 开始休息
    print("开始休息")
    # 倒计时休息时间
    countdown(break_time)
    # 播放休息结束的声音
    play_sound("break_end.mp3")

import time

seconds = max(0, int(input("输入倒计时秒数: ")))
while seconds > 0:
    print(f"剩余: {seconds} 秒", end="\r")
    time.sleep(1)
    seconds -= 1
print("时间到！     ")

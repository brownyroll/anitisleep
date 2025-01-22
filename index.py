import pyautogui
import time
import ctypes

print("🐁 Mouse Move And Anti Sleep ---------------------- - [] X")
print("This program will move the mouse and anti sleep mode")
print("")
print("Version 1.0 Thank for use my product")
print("https://brownyrollz.in.th && https://github.com/brownyroll/anitisleep")
print("Power By : BBamz Kittisak Udomsri (Brownyrollz)")
print("")
print("Press Ctrl-C to stop the program")

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

def restore_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

if __name__ == "__main__":
    try:
        while True:
            prevent_sleep()
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 10, y + 10, duration=0.2)
            pyautogui.moveTo(x, y, duration=0.2)
            time.sleep(30)
    except KeyboardInterrupt:
        restore_sleep()
else:
    print("Stopped by user")

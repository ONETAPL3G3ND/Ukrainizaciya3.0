import winreg as reg

class ProxySetup:
    def __init__(self):
        ...
    @classmethod
    def set_proxy(cls, proxy) -> None:
        internet_settings = reg.OpenKey(reg.HKEY_CURRENT_USER,
                                        r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                        0, reg.KEY_ALL_ACCESS)

        reg.SetValueEx(internet_settings, 'ProxyServer', 0, reg.REG_SZ, proxy)
        reg.SetValueEx(internet_settings, 'ProxyEnable', 0, reg.REG_DWORD, 1)

        reg.CloseKey(internet_settings)

    @classmethod
    def deactivate_proxy(cls) -> None:
        internet_settings = reg.OpenKey(reg.HKEY_CURRENT_USER,
                                        r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                        0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(internet_settings, 'ProxyEnable', 0, reg.REG_DWORD, 0)

        reg.CloseKey(internet_settings)
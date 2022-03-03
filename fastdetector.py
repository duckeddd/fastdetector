import os 
import sys
import ctypes
from psutil import virtual_memory
import subprocess
import platform
import pyfiglet

system = sys.platform # переменные для работы скрипта
mem = virtual_memory()
cwd = os.getcwd()
    
text = pyfiglet.figlet_format("fastdetector")
select = pyfiglet.figlet_format("select")

def get_free_space_mb(folder):
    """ Return folder/drive free space (in bytes)
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value/1024/1024/1024 
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize/1024/1024

print(select)
answ = input('Select language / Выберите язык: (1 - eng, 2 - rus)')
if answ == '1':
    print(text)
    print('made by ducked / gh: @duckeddd')
    print('=================================================')
    if system == 'linux':
        print('System: Linux (or etc distr)')
    elif system == 'linux2':
        print('System: Linux (or etc distr)')
    elif system == 'win32':
        print('System: Windows')
    elif system == 'cygwin':
        print('System: Windows (or cygwin)')
    elif system == 'msys':
        print('System: Windows (or MSYS2)')
    elif system == 'darwin':
        print('System: Mac OS X')
    elif system == 'os2':
        print('System: OS/2')
    elif system == 'os2emx':
        print('System: OS/2 EMX')
    elif system == 'riscos':
        print('System: RiscOS')
    elif system == 'atheos':
        print('System: AtheOS')
    elif system == 'freebsd7':
        print('System: FreeBSD 7')
    elif system == 'freebsd8':
        print('System: FreeBSD 8')
    elif system == 'freebsdN':
        print('System: FreeBSD N')
    elif system == 'openbsd6':
        print('System: OpenBSD 6')
    print('Free space on (C:/ or root):', get_free_space_mb('C:\\'),'GB')
    print('Free space on (D:/ or other):', get_free_space_mb('D:\\'),'GB')
    print('Virtual memory:', mem.total // 1000000000, 'GB')
    print('Directory:', cwd)
    print('=================================================')
    print('Fast commands')
    print('1. Off the PC')
    print('2. Execute file (only .exe or other Linux program)')
    answ1 = input()
    if answ1 == '1':
        answ2 = input('Off PC? (y or n)')
        if answ2 == 'y':
            os.system('shutdown -s')
        elif answ == 'n':
            print('Canceled')
    elif answ1 == '2':
        answ1def = input('Directory:')
        subprocess.call(answ1def)
elif answ == '2':
    print(text)
    print('made by ducked / gh: @duckeddd')
    print('=================================================')
    if system == 'linux':
        print('Система: Linux (или другой дистр.)')
    elif system == 'linux2':
        print('Система: Linux (или другой дистр.)')
    elif system == 'win32':
        print('Система: Windows')
    elif system == 'cygwin':
        print('Система: Windows (или cygwin)')
    elif system == 'msys':
        print('Система: Windows (или MSYS2)')
    elif system == 'darwin':
        print('Система: Mac OS X')
    elif system == 'os2':
        print('Система: OS/2')
    elif system == 'os2emx':
        print('Система: OS/2 EMX')
    elif system == 'riscos':
        print('Система: RiscOS')
    elif system == 'atheos':
        print('Система: AtheOS')
    elif system == 'freebsd7':
        print('Система: FreeBSD 7')
    elif system == 'freebsd8':
        print('Система: FreeBSD 8')
    elif system == 'freebsdN':
        print('Система: FreeBSD N')
    elif system == 'openbsd6':
        print('Система: OpenBSD 6')
    print('Свободное место на (C:/ or другой корневой диск):', get_free_space_mb('C:\\'),'GB')
    print('Свободное место на (D:/ или другой диск):', get_free_space_mb('D:\\'),'GB')
    print('ОЗУ:', mem.total // 1000000000, 'GB')
    print('Директория:', cwd)
    print('=================================================')
    print('Быстрые команды')
    print('1. Выключить ПК')
    print('2. Открыть файл (только .exe или другая программа Linux)')
    answ1 = input()
    if answ1 == '1':
        answ2 = input('Выключить ПК? (y или n)')
        if answ2 == 'y':
            os.system('shutdown -s')
        elif answ == 'n':
            print('Отменено')
    elif answ1 == '2':
        answ1def = input('Директория:')
        subprocess.call(answ1def)
        
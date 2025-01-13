import random
import subprocess
import time
import threading
import os
import psutil
from datetime import datetime

nox_path = "C:\\Program Files (x86)\\Nox\\bin\\Nox.exe"

# Список эмуляторов и времени их запуска (в секундах)
emulators = [
    {"name": "ari", "path": "-clone:Nox_9", "interval": 24},  # 24 часа
    {"name": "david", "path": "-clone:Nox_1", "interval": 12},  # 5 часов
    {"name": "hard", "path": "-clone:Nox_2", "interval": 12},  # 5 часов
    {"name": "join", "path": "-clone:Nox_11", "interval": 24},  # 5 часов
    {"name": "lisan", "path": "-clone:Nox_3", "interval": 24},  # 5 часов
    {"name": "lux", "path": "-clone:Nox_4", "interval": 12},  # 5 часов
    {"name": "mistie", "path": "-clone:Nox_10", "interval": 24},  # 5 часов
    {"name": "revor_", "path": "-clone:Nox_5", "interval": 6},  # 5 часов
    {"name": "mo0n", "path": "-clone:Nox_6", "interval": 24},  # 5 часов
    {"name": "ministr", "path": "-clone:Nox_7", "interval": 6},  # 5 часов
    {"name": "alpaka", "path": "-clone:Nox_8", "interval": 6},  # 5 часов
    {"name": "compart", "path": "", "interval": 12}  # 5 часов
]

# Функция для проверки, запущен ли процесс Nox.exe
def is_nox_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "Nox.exe":
            return True
    return False

# Функция для запуска эмулятора
def run_emulator(emulator):
    while True:
        print(f"[{datetime.now()}] Проверка, запущен ли процесс Nox...")

        # Проверяем, запущен ли процесс Nox
        while is_nox_running():
            print(f"[{datetime.now()}] Процесс Nox.exe запущен, ожидаем 1 минуту...")
            time.sleep(15)  # Сон на 1 минуту



        print(f"[{datetime.now()}] Запуск {emulator['name']} ({emulator['path']})")
        # Запуск процесса Nox
        process = subprocess.Popen([nox_path, emulator["path"]])

        # Ожидание 180 секунд
        time.sleep(150)

        # Завершение процесса Nox
        print(f"[{datetime.now()}] Завершение {emulator['name']}")
        try:
            subprocess.call(["taskkill", "/IM", "Nox.exe", "/F"])
        except Exception as e:
            print(f"[{datetime.now()}] Процесс не найден")

        # Ожидание указанного интервала
        t = random.randint(int(3600*emulator['interval']-3600*emulator['interval']*0.2), int(3600*emulator['interval']+3600*emulator['interval']*0.2))
        if emulator['interval'] == 24:
            t = random.randint(int(3600*18-3600*18*0.2), int(3600*18+3600*18*0.2))
        print(f"[{datetime.now()}] Ожидание {t/3600} ч до следующего запуска {emulator['name']}")
        time.sleep(t)



# Создание потоков для каждого эмулятора
threads = []
for emulator in emulators:
    thread = threading.Thread(target=run_emulator, args=(emulator,))
    threads.append(thread)
    thread.start()
    time.sleep(180)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()
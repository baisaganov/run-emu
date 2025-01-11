import random
import subprocess
import time
import threading
import os


nox_path = "C:\\Program Files (x86)\\Nox\\bin\\Nox.exe"

# Список эмуляторов и времени их запуска (в секундах)
emulators = [
    {"name": "ari", "path": "-clone:Nox_9", "interval": 24},  # 24 часа
    {"name": "david", "path": "-clone:Nox_1", "interval": 6},  # 5 часов
    {"name": "hard", "path": "-clone:Nox_2", "interval": 6},  # 5 часов
    {"name": "join", "path": "-clone:Nox_11", "interval": 24},  # 5 часов
    {"name": "lisan", "path": "-clone:Nox_3", "interval": 6},  # 5 часов
    {"name": "lux", "path": "-clone:Nox_4", "interval": 12},  # 5 часов
    {"name": "mistie", "path": "-clone:Nox_10", "interval": 12},  # 5 часов
    {"name": "revor_", "path": "-clone:Nox_5", "interval": 4},  # 5 часов
    {"name": "mo0n", "path": "-clone:Nox_6", "interval": 24},  # 5 часов
    {"name": "ministr", "path": "-clone:Nox_7", "interval": 4},  # 5 часов
    {"name": "alpaka", "path": "-clone:Nox_8", "interval": 4},  # 5 часов
    {"name": "compart", "path": "", "interval": 6}  # 5 часов
]


# Функция для запуска эмулятора
def run_emulator(emulator):
    while True:
        print(f"Запуск {emulator['name']} ({emulator['path']})")
        # Запуск процесса Nox
        process = subprocess.Popen([nox_path, emulator["path"]])

        # Ожидание 180 секунд
        time.sleep(180)

        # Завершение процесса Nox
        print(f"Завершение {emulator['name']}")
        subprocess.call(["taskkill", "/IM", "Nox.exe", "/F"])

        # Ожидание указанного интервала
        print(f"Ожидание {emulator['interval']} секунд до следующего запуска {emulator['name']}")
        if emulator['interval'] == 4:
            time.sleep(random.randint(13500, 15500))
        elif emulator['interval'] == 6:
            time.sleep(random.randint(20000, 23000))
        elif emulator['interval'] == 12:
            time.sleep(random.randint(42000, 45600))
        elif emulator['interval'] == 24:
            time.sleep(random.randint(84000, 91200))


# Создание потоков для каждого эмулятора
threads = []
for emulator in emulators:
    thread = threading.Thread(target=run_emulator, args=(emulator,))
    threads.append(thread)
    thread.start()
    time.sleep(185)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()
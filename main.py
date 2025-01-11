import random
import subprocess
import time


emulator_path = r"C:\Program Files (x86)\Nox\bin\Nox.exe"

# Список эмуляторов и времени их запуска (в секундах)
emulators = [
    {"name": "Emulator1", "path": "-clone:Nox_9", "interval": 4},  # 4 часа
    {"name": "Emulator1", "path": "-clone:Nox_1", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_2", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_11", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_3", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_4", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_10", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_5", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_6", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_7", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "-clone:Nox_8", "interval": 4},  # 5 часов
    {"name": "Emulator1", "path": "", "interval": 4}  # 5 часов
]

# Функция для запуска эмулятора
def run_emulator(emulator):
    print(f"Запускается: {emulator['name']}")
    args = [emulator['path']]
    try:
        subprocess.Popen([emulator_path, *args], shell=True)
        print("Эмулятор запущен с параметрами:", " ".join(args))
    except Exception as e:
        print(f"Ошибка при запуске эмулятора: {e}")
    time.sleep(120)  # Задержка для корректной инициализации

# Основной цикл
while True:
    for emulator in emulators:
        run_emulator(emulator)
        print(f"Ждем {emulator['interval']} часов перед следующим запуском.")
        if emulator['interval'] == 4:
            random.randint(13500, 15500)
        elif emulator['interval'] == 6:
            random.randint(20000, 23000)

        time.sleep(emulator['interval'])  # Задержка перед запуском следующего

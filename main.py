import random
import subprocess
import time

# Список эмуляторов и времени их запуска (в секундах)
emulators = [
    {"name": "Emulator1", "path": "C:\\Users\\o7\\Desktop\\emu\\arimka.lnk", "interval": 4},  # 4 часа
    {"name": "Emulator2", "path": "path/to/emulator2.exe", "interval": 6},  # 5 часов
    # Добавьте остальные эмуляторы
]



# Функция для запуска эмулятора
def run_emulator(emulator):
    print(f"Запускается: {emulator['name']}")
    subprocess.Popen(emulator["path"])  # Открытие эмулятора
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

        time.sleep(emulator["interval"])  # Задержка перед запуском следующего

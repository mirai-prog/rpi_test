import RPi.GPIO as GPIO
import time
import random

# Настройка GPIO
GPIO.setmode(GPIO.BCM)

# Пины для светодиодов и кнопок
LED_PINS = [17, 27, 22]  # Пины для 3 светодиодов
BUTTON_PINS = [4, 9, 11]  # Пины для 3 кнопок

# Настройка пинов
for led_pin in LED_PINS:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)

for btn_pin in BUTTON_PINS:
    GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Функция для отображения стартовой последовательности
def start_sequence():
    for _ in range(3):  # Повторить 3 раза
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(random.uniform(0.2, 1.0))  # Случайная задержка 0.2-1 сек
            GPIO.output(pin, GPIO.LOW)
        time.sleep(random.uniform(0.2, 1.0))  # Задержка между циклами

# Функция измерения времени реакции для конкретного светодиода и кнопки
def measure_reaction_time(led_pin, btn_pin):
    time.sleep(random.uniform(2, 5))  # Ожидание случайного времени
    GPIO.output(led_pin, GPIO.HIGH)  # Включить светодиод
    start_time = time.time()  # Запомнить время включения

    while GPIO.input(btn_pin):  # Ожидание нажатия кнопки
        pass

    reaction_time = time.time() - start_time  # Вычислить время реакции
    GPIO.output(led_pin, GPIO.LOW)  # Выключить светодиод
    return reaction_time

# Главная функция программы
def main():
    try:
        name = input("Введите ваше имя: ")
        print("Начинаем измерение времени реакции!")
        results = []

        # Стартовая последовательность
        start_sequence()

        # 3 измерения, одно для каждого светодиода и кнопки
        for i in range(3):
            print(f"Тест {i+1}: Приготовьтесь...")
            result = measure_reaction_time(LED_PINS[i], BUTTON_PINS[i])
            results.append(result)
            print(f"Ваше время реакции: {result:.3f} секунды")
            time.sleep(1)

        # Подсчет среднего времени реакции
        average_time = sum(results) / len(results)
        print(f"Среднее время реакции: {average_time:.3f} секунды")

        # Сохранение результатов в файл
        with open("reaction_times.txt", "a") as file:
            file.write(f"{name}\n")
            file.write(f"Результаты: {', '.join(f'{r:.3f}' for r in results)}\n")
            file.write(f"Среднее время: {average_time:.3f} секунды\n")
            file.write("-" * 30 + "\n")

        print("Результаты сохранены в файл 'reaction_times.txt'.")

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")

    finally:
        GPIO.cleanup()  # Очистка настроек GPIO

if __name__ == "__main__":
    main()


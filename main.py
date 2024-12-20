import RPi.GPIO as GPIO
import time
import random

# Konfiguracja GPIO
GPIO.setmode(GPIO.BCM)

# Piny dla diod LED i przycisków
LED_PINS = [17, 27, 22]  # Piny dla 3 diod LED
BUTTON_PINS = [4, 9, 11]  # Piny dla 3 przycisków

# Ustawienie pinów
for led_pin in LED_PINS:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)

for btn_pin in BUTTON_PINS:
    GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Funkcja wyświetlająca sekwencję startową
def start_sequence():
    for _ in range(3):  # Powtarzaj 3 razy
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(random.uniform(0.2, 1.0))  # Losowy czas 0.2-1 sekundy
            GPIO.output(pin, GPIO.LOW)
        time.sleep(random.uniform(0.2, 1.0))  # Losowy czas między cyklami

# Funkcja pomiaru czasu reakcji dla konkretnej diody LED i przycisku
def measure_reaction_time(led_pin, btn_pin):
    time.sleep(random.uniform(2, 5))  # Czekaj losowy czas 2-5 sekund
    GPIO.output(led_pin, GPIO.HIGH)  # Włącz diodę
    start_time = time.time()  # Zarejestruj czas startu

    while GPIO.input(btn_pin):  # Czekaj na naciśnięcie przycisku
        pass

    reaction_time = time.time() - start_time  # Oblicz czas reakcji
    GPIO.output(led_pin, GPIO.LOW)  # Wyłącz diodę
    return reaction_time

# Główna funkcja programu
def main():
    try:
        name = input("Podaj swoje imię: ")  # Pobierz imię użytkownika
        print("Rozpoczynamy pomiary czasu reakcji!")
        results = []

        # Sekwencja startowa
        start_sequence()

        # 3 pomiary, po jednym dla każdej diody LED i przycisku
        for i in range(3):
            print(f"Test {i+1}: Przygotuj się...")
            result = measure_reaction_time(LED_PINS[i], BUTTON_PINS[i])
            results.append(result)
            print(f"Twój czas reakcji: {result:.3f} sekundy")
            time.sleep(1)

        # Oblicz średni czas reakcji
        average_time = sum(results) / len(results)
        print(f"Średni czas reakcji: {average_time:.3f} sekundy")

        # Zapisz wyniki do pliku
        with open("reaction_times.txt", "a") as file:
            file.write(f"{name}\n")
            file.write(f"Wyniki: {', '.join(f'{r:.3f}' for r in results)}\n")
            file.write(f"Średni czas: {average_time:.3f} sekundy\n")
            file.write("-" * 30 + "\n")

        print("Wyniki zapisane do pliku 'reaction_times.txt'.")

    except KeyboardInterrupt:
        print("\nProgram przerwany przez użytkownika.")

    finally:
        GPIO.cleanup()  # Czyszczenie ustawień GPIO

if __name__ == "__main__":
    main()


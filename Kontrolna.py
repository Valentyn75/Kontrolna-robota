import os
import json
from translation_module import translate_message, calculate_differences

# Шлях до файлу з даними
FILE_PATH = 'MyData.json'

# Функція для читання даних з файлу
def load_data():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as file:
                data = json.load(file)
                # Перевірка наявності всіх необхідних полів
                if "x" in data and "y" in data and "language" in data:
                    return data
        except (json.JSONDecodeError, KeyError):
            # Якщо виникла помилка під час читання або неправильна структура
            return None
    return None

# Функція для запису даних у файл
def save_data(x, y, language):
    data = {"x": x, "y": y, "language": language}
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

# Основна логіка програми
def main():
    data = load_data()

    if data is None:
        # Якщо файл відсутній або містить некоректні дані
        try:
            x, y = map(int, input("Введіть два числа x та y (через пробіл): ").split())
            language = input("Введіть мову інтерфейсу (uk/en): ").strip().lower()
        except ValueError:
            print("Помилка: введіть коректні числа.")
            return

        # Збереження даних у файл і завершення роботи програми
        save_data(x, y, language)
        print("Дані збережено у файл. Запустіть програму знову для обчислень.")
    else:
        # Якщо дані успішно прочитані з файлу
        x, y, language = data['x'], data['y'], data['language']

        # Перевірка мови, використання української за замовчуванням
        if language not in ['uk', 'en']:
            language = 'uk'

        # Виконання обчислень
        results = calculate_differences(x, y)

        # Виведення результатів з перекладом
        print(f"{translate_message('Модуль різниці квадратів', language)}: {results['modulus']}")
        print(f"{translate_message('Квадрат різниці', language)}: {results['square_diff']}")

        # Порівняння та виведення повідомлення
        if results['modulus'] > results['square_diff']:
            print(translate_message('Модуль різниці більше!', language))
        else:
            print(translate_message('Квадрат різниці більше!', language))

if __name__ == "__main__":
    main()

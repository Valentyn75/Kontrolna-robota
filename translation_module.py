# Функція перекладу повідомлень на вказану мову
def translate_message(message, language):
    translations = {
        'Модуль різниці квадратів': {'uk': 'Модуль різниці квадратів', 'en': 'Modulus of square difference'},
        'Квадрат різниці': {'uk': 'Квадрат різниці', 'en': 'Square of the difference'},
        'Модуль різниці більше!': {'uk': 'Модуль різниці більше!', 'en': 'Modulus is greater!'},
        'Квадрат різниці більше!': {'uk': 'Квадрат різниці більше!', 'en': 'Square of difference is greater!'}
    }
    return translations.get(message, {}).get(language, message)

# Функція для обчислення модуля різниці квадратів та квадрата різниці
def calculate_differences(x, y):
    modulus = abs(x**2 - y**2)
    square_diff = (x - y)**2
    return {"modulus": modulus, "square_diff": square_diff}

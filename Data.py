import datetime
import os  # Добавляем для os.system("pause")

def get_weekday(day, month, year):
    """Определяет день недели по дате."""
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[datetime.date(year, month, day).weekday()]

def is_leap_year(year):
    """Проверяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_day, birth_month, birth_year):
    """Вычисляет текущий возраст пользователя."""
    today = datetime.date.today()
    age = today.year - birth_year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age

def print_digital_style(date_str):
    """Выводит дату в стиле электронного табло (звёздочками)."""
    digit_patterns = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***'],
        ' ': ['   ', '   ', '   ', '   ', '   ']
    }
    
    date_chars = []
    for char in date_str:
        date_chars.append(char)
        date_chars.append(' ')
    date_chars.pop()
    
    for line in range(5):
        for char in date_chars:
            print(digit_patterns.get(char, ['   '])[line], end=' ')
        print()

def main():
    """Основная функция программы."""
    print("Введите дату вашего рождения:")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))
    
    try:
        datetime.date(year, month, day)
    except ValueError:
        print("Ошибка: Некорректная дата!")
        os.system("pause" if os.name == 'nt' else "read -p 'Нажмите Enter...'")  # Заглушка
        return
    
    weekday = get_weekday(day, month, year)
    print(f"День недели: {weekday}")
    
    leap_status = "високосный" if is_leap_year(year) else "не високосный"
    print(f"Год {year} — {leap_status}")
    
    age = calculate_age(day, month, year)
    print(f"Вам сейчас {age} лет")
    
    date_str = f"{day:02d} {month:02d} {year}"
    print("\nДата рождения в стиле электронного табло:")
    print_digital_style(date_str)
    
    # Заглушка, чтобы консоль не закрывалась
    if os.name == 'nt':  # Windows
        os.system("pause")
    else:  # Linux/Mac
        os.system("read -p 'Нажмите Enter для выхода...'")

if __name__ == "__main__":
    main()
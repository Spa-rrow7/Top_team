👩‍💻 Работа с датами и временем: 90% кода можно заменить этими шаблонами

Собрал самые частые задачи с datetime, которые встречаются в реальных проектах. Бери и используй.
from datetime import datetime, timedelta
import pytz  # pip install pytz

# 1️⃣ Парсим строку в дату (самая частая задача)
```
date_str = "2024-03-15 14:30"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
print(dt)  # 2024-03-15 14:30:00
```

# Форматы, которые нужно знать:
# %Y - год (2024), %y - год (24)
# %m - месяц (03), %B - месяц (March)
# %d - день (15)
# %H - час (14), %I - час (02 PM)
# %M - минуты (30)
# %S - секунды (45)

# 2️⃣ Разница между датами
```
date1 = datetime(2024, 3, 10)
date2 = datetime(2024, 3, 15)
diff = date2 - date1
print(diff.days)          # 5 (дней)
print(diff.total_seconds()) # 432000.0 (секунд)
```
# 3️⃣ Добавляем/вычитаем время
```
now = datetime.now()
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_hour = now + timedelta(hours=1)
```

# Можно всё вместе
```
future = now + timedelta(days=7, hours=3, minutes=30)
```

# 4️⃣ Сравнение дат
```
if date1 < date2:
    print("date1 раньше date2")
```

# 5️⃣ Форматируем дату в строку
```
now = datetime.now()
print(now.strftime("%d.%m.%Y"))      # 15.03.2024
print(now.strftime("%H:%M"))         # 14:30
print(now.strftime("%A %d %B %Y"))   # Friday 15 March 2024
```

# 6️⃣ Таймзоны (боль всех)
```
moscow_tz = pytz.timezone('Europe/Moscow')
utc_time = datetime.utcnow()
moscow_time = utc_time.replace(tzinfo=pytz.utc).astimezone(moscow_tz)
print(moscow_time)
```

# 7️⃣ UNIX timestamp
```
timestamp = datetime.now().timestamp()  # 1710505800.123
dt_from_timestamp = datetime.fromtimestamp(timestamp)
```

# 8️⃣ Работа с временем без даты
```
from datetime import time
meeting_time = time(14, 30)  # 14:30
print(meeting_time.hour)     # 14
```


# 9️⃣ Проверка на корректность даты
```
def is_valid_date(year, month, day):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False
```


# 🔟 Сколько дней до Нового года?
```
today = datetime.now()
new_year = datetime(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"До Нового года: {days_left} дней")
```

💡 Готовые функции для копирования:
```
def days_between(date1_str, date2_str, fmt="%Y-%m-%d"):
    """Возвращает количество дней между двумя датами.

    :param date1_str: первая дата (строка)
    :param date2_str: вторая дата (строка)
    :param fmt: формат даты (по умолчанию YYYY-MM-DD)
    """
    try:
        d1 = datetime.strptime(date1_str, fmt)
        d2 = datetime.strptime(date2_str, fmt)
    except ValueError as e:
        raise ValueError(f"Ошибка формата даты: {e}") from None

    return abs((d2 - d1).days)
```

```
def add_days_to_date(date_str, days, fmt="%Y-%m-%d"):
    """Добавить дни к дате."""
    dt = datetime.strptime(date_str, fmt)
    new_dt = dt + timedelta(days=days)
    return new_dt.strftime(fmt)
```

```
def is_weekend(date_str, fmt="%Y-%m-%d"):
    """Выходной ли день?"""
    dt = datetime.strptime(date_str, fmt)
    return dt.weekday() >= 5  # 5 = суббота, 6 = воскресенье
```

```
def get_age(birth_date_str, fmt="%Y-%m-%d"):
    """Вычислить возраст по дате рождения."""
    birth = datetime.strptime(birth_date_str, fmt)
    today = datetime.now()
    age = today.year - birth.year
    # Проверяем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    return age
```

```
def date_range(start_date, end_date, fmt="%Y-%m-%d"):
    """Генератор всех дат между start_date и end_date."""
    current = datetime.strptime(start_date, fmt)
    end = datetime.strptime(end_date, fmt)
    while current <= end:
        yield current.strftime(fmt)
        current += timedelta(days=1)
```
# Примеры использования
# Генератор дат
```
print(list(date_range("2024-03-01", "2024-03-05")))
```
# ['2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05']

🚀 Примеры использования:
# Калькулятор дедлайнов
```
deadline = "2024-12-31"
days_left = days_between(datetime.now().strftime("%Y-%m-%d"), deadline)
print(f"Дней до дедлайна: {days_left}")
```

# Планировщик
```
task_date = "2024-03-20"
reminder_date = add_days_to_date(task_date, -3)  # Напоминание за 3 дня
print(f"Напоминание: {reminder_date}")
<<<<<<< HEAD

task_date = "2024-03-25"
reminder_date = add_days_to_date(task_date, -3)  # Напоминание за 3 дня
print(f"Напоминание: {reminder_date}")

=======
```
>>>>>>> d1c52868c26d41d70d6f5fe6cb9b03997f15db1a
# Проверка рабочего дня
```
if not is_weekend("2024-03-16"):
    print("Рабочий день")
else:
    print("Выходной!")
```

⚠️ Частые ошибки:
🔢. Путаница форматов — %Y vs %y, %m vs %M
🔢. Игнорирование таймзон — всё время в UTC или локальное
🔢. 29 февраля — не проверяют високосные годы
🔢. Переполнение времени — time(25, 0) даст ошибку

📌 Запомни:
🟢 Используй timedelta для операций со временем
🟢 Всегда указывай формат при парсинге строк
🟢 Храни даты в UTC, отображай в локальном времени
🟢 Для сложной логики используй библиотеку dateutil

🗣 Итог: С datetime ты будешь сталкиваться в каждом втором проекте. 

👩‍💻  Only Python (https://t.me/+FMH3zPxDuRtiNTFi)||👨‍💻 #Код

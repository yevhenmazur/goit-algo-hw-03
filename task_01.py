"""The module allows processing datetime objects"""

from datetime import datetime
event_date = input("Введіть дату в форматі РРРР-ММ-ДД >>> ")

def get_days_from_today(date: str) -> int:
    """The function calculates the number of days from the date of the event to today"""
    current_date = datetime.today()
    while True:
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            date = input("Схоже що ви ввели дату не правильно. Введіть дату у фоматі РРРР-ММ-ДД >>> ")
    diff_in_days = current_date.toordinal() - date.toordinal()
    return diff_in_days
    
result = get_days_from_today(event_date)
print(result)

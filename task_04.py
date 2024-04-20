"""The module allows processing datetime and timedelta objects"""

from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    """
    The function calculates birthdays based on the employee's date of birth
    and assigns a date for congratulations within 7 days to one of the working days of the week.
    """
    current_date = datetime.today().date()
    current_year = current_date.year
    upcoming_birthdays = list()
    for user in users:
        birthday= datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year = current_year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year = current_year + 1)
        days_to_bithday = birthday_this_year - current_date
        if days_to_bithday <= timedelta(days=7):
            if birthday_this_year.weekday() == 5:
                celebration_day = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                celebration_day = birthday_this_year + timedelta(days=1)
            else:
                celebration_day = birthday_this_year
            celebration_day = celebration_day.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "celebration_day": celebration_day})
    return upcoming_birthdays

### Uncomment section below to check the function
'''
USERS = [
    {"name": "John Doe", "birthday": "1985.01.23"},     # Has Birthday in the past
    {"name": "Jane Smith", "birthday": "1993.04.25"},   # Has Birthday next week
    {"name": "Alice Brown", "birthday": "1989.04.21"},  # Has Birthday next weekend
    {"name": "Bob Johnson", "birthday": "1990.07.07"}   # Has Birthday in two monce
]

upcoming_birthdays = get_upcoming_birthdays(USERS)
print("Список привітань на цьому тижні:", upcoming_birthdays)
'''

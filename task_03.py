"""Module providing a functions for regular expressions."""

import re

def normalize_phone(phone_number: str) -> str:
    """The function accepts a phone number in any format and returns it in a normalized format"""
    phone_number = re.sub(r"[^0-9+]", "", phone_number)
    phone_number = list(phone_number)
    phone_number = phone_number[-9:] # Remove prefix
    values_to_insert = [(-9, "0"), (-10, "8"),(-11, "3"), (-12, "+")]
    for index, value in values_to_insert:
        phone_number.insert(index, value) # Rewrite prefix
    phone_number = "".join(phone_number)
    return phone_number

### Uncomment section below to check the function
'''
raw_numbers = [
    "+067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
'''

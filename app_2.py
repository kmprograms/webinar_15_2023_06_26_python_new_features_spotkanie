from enum import Enum
from datetime import datetime
from typing import Any

# Structural Pattern Matching

print("------------------------------ (1) ------------------------------")

worker1 = {
    'name': 'John',
    'address': {
        'street': 'Gr',
        'city': 'Wa',
        'number': 1
    }
}


def get_worker_city(worker: dict[str, Any]) -> str:
    match worker:
        case {'address': {'city': worker_city}}:
            return worker_city
    raise KeyError('City key not found')


print(get_worker_city(worker1))

print("------------------------------ (2) ------------------------------")

user1 = {
    'name': 'John',
    'age': '12'
}

user2 = {
    'name': 'John',
    'age': {
        'birthdate': '2000-01-01'
    }
}


def get_user_age(user: dict[str, Any]) -> int:
    match user:
        # Najpierw to (zamien i zobacz co sie stanie)
        case {'age': {'birthdate': birthdate}}:
            year_now = datetime.now().year
            birthdate_year = datetime.strptime(birthdate, '%Y-%m-%d').year
            return year_now - birthdate_year
        case {'age': age}:
            return int(age)


print(get_user_age(user1))
print(get_user_age(user2))

print("------------------------------ (3) ------------------------------")


def sum_numbers(numbers: list[int | str]) -> int:
    match numbers:
        case []:
            return 0
        case [first, *rest]:
            if type(first) == str:
                return int(first) + sum_numbers(rest)
            return first + sum_numbers(rest)
        case _:
            # Wykona sie w pozostalych przypadkach
            raise ValueError('Bad list')


print(sum_numbers([1, 2, 3, 4]))
print(sum_numbers(['1', '2', '3', '4']))


def sum_numbers_2(numbers: list[int | float | str]) -> int:
    match numbers:
        case []:
            return 0
        case [int(first) | float(first) | str(first), *rest]:
            # W tym case jestes jezeli first jest int, float lub str
            if type(first) == str:
                return int(first) + sum_numbers_2(rest)
            return first + sum_numbers_2(rest)
        case [int(first) | float(first) | str(first) as value, *rest]:
            if type(value) == str:
                return int(value) + sum_numbers_2(rest)
            return value + sum_numbers_2(rest)
        case _:
            # Wykona sie w pozostalych przypadkach
            raise ValueError('Bad list')


print(sum_numbers_2([1, 2, 3, 4]))
print(sum_numbers_2(['1', '2', '3', '4']))
print(sum_numbers_2([1.5, 2.3, 3.3, 4.4]))


# MATCHING LITERAL PATTERNS

def get_pl_color(color: str) -> str:
    match color.lower():
        case 'r':
            return 'czerwony'
        case 'g':
            return 'zielony'
        case _:
            return 'inny'


print("------------------------------ (4) ------------------------------")
print(get_pl_color('r'))

print("------------------------------ (5) ------------------------------")


class Color(Enum):
    RED = 'R',
    GREEN = 'G',
    BLUE = 'B'


def get_color(color: Color) -> str:
    match color:
        case Color.RED:
            return Color.RED.value
        case _:
            return 'KOLOR'


print(get_color(Color.BLUE))

print("------------------------------ (6) ------------------------------")


# TODO Ta funkcja jest do poprawy
def fizzbuzz(number: int) -> int | str:
    if number % 3 == 0:
        return 'fizz'
    elif number % 2 == 0:
        return 'buzz'
    elif number % 15 == 0:
        return 'fizzbuz'
    else:
        return number


def fizzbuzz_2(number: int) -> str:
    mod_3 = number % 3
    mod_5 = number % 5

    match (mod_3, mod_5):
        case (0, 0):
            return 'fizzbuzz'
        case (0, _):  # nie interesuje mnie druga wartosc, ale wiem o tej porzez ze ona nie jest 0!
            return 'fizz'
        case (_, 0):
            return 'buzz'
        case _:
            return number


# Guards
def fn(seq: list[int]) -> list[int]:
    match seq:
        case []:
            return seq
        case [x]:
            return 10 * [x]
        # Ten case zajdzie, jezeli spelniony jest warunek
        case [x, y, *rest] if x > y:
            return 10 * [x] + [y]
        case [x, y, *rest]:
            return 10 * [y]
        case _:
            return [1]

from typing import Union, Optional, Self
from dataclasses import dataclass

# UNION TYPE

# def f1(n: Union[int, float]) -> Union[int, float]:
def f1(n: int | float) -> int | float:
    return n + 10

# Odpowiednikiem Optional jest int | None
def f2(n: int | float) -> int | None:
    return n + 10


# Funkcja zip

x1 = [11, 22, 33]
x2 = [111, 222, 333] # , 444]
z1 = zip(x1, x2, strict=True)
for f, s in z1:
    print(f, s)

# Mozliwosc uzywania polaczenia z kilkoma zasobami w ramach context managera
# + mozliwosc stosowania ()
with (
    open('data1.txt', 'w') as d1,
    open('data2.txt', 'w') as d2
):
    d1.writelines(['a'])
    d2.writelines(['a'])

# ------------------------------------------------------------------------------------------------
# Python ciagle stara sie poprawiac komunikaty o bledach, zebysmy byli jeszcze
# bardziej informowani o tym co dokladnie popsulo sie w naszym programie.

# print('KM'

# def f():
#     if True:
#     x = 10

# WALRUS OPERATOR

# x = int(input('Podaj liczbę:\n'))
# while x != 10:
#     x = int(input('Podaj liczbę:\n'))
# print(x)
# while (x := int(input('Podaj liczbę:\n'))) != 10:
#     pass
# print(x)

# ------------------------------------------------------------------------------------------------
# Tworcy jezyka Python chwala sie, ze ich jezyk jest po prostu szybszy
# Takie funkcje jak str(), bytes() czy bytearray() sa nawet 40% szybsze
# przy pracy z malymi obiektami

# Opis dotyczacy szybkosci jezyka w wersji 3.11
# CPython jest referencyjną implementacją języka programowania Python. Napisany
# w C i Pythonie, CPython jest domyślną i najczęściej używaną implementacją języka Python.
# W wersji 3.11, interpreter CPythona jest znacznie bardziej zoptymalizowany i szybszy
# niż w wersji 3.10. CPython 3.11 jest średnio 1,22x szybszy od CPythona 3.10, gdy
# mierzy się to przy użyciu zestawu benchmarków pyperformance i kompiluje przy użyciu
# GCC na Ubuntu Linux. W zależności od obciążenia, przyspieszenie może wynosić nawet
# od 10 do 60%. [1]
#
# W Pythonie 3.11, deweloperzy skupili się głównie na szybszym uruchamianiu i
# szybszym działaniu, co zostało wyraźnie określone w dokumentacji.

# Szybsze Uruchamianie [6]
# W tej wersji, Python będzie buforować bajtkod w katalogu pycache w celu przyspieszenia
# procesu ładowania modułów. Oczekuje się, że uruchomienie interpretera będzie 10-15%
# szybsze w Pythonie 3.11. Ma to duży wpływ na krótkotrwałe programy korzystające z Pythona.
#
# Szybsze Działanie [6]
# W Pythonie, ramki są tworzone za każdym razem, gdy Python wywołuje funkcję zdefiniowaną
# przez użytkownika. Ta ramka przechowuje informacje o wykonaniu funkcji. Poniżej znajdują
# się nowe optymalizacje ramki w wersji 3.11, które mają na celu przyspieszenie jej działania:

# Usprawniono proces tworzenia ramek, aby był szybszy.
# Uniknięto alokacji pamięci poprzez hojne ponowne wykorzystanie przestrzeni ramek na
# stosie C.
# Zredukowano ilość informacji przechowywanych przez ramkę, upraszczając jej wewnętrzną
# strukturę. Wcześniej, ramki przechowywały dodatkowe informacje służące do debugowania
# i zarządzania pamięcią. Obiekty ramki w starym stylu są teraz tworzone tylko wtedy,
# gdy są wymagane przez debugery.
# Dla większości kodu użytkownika, w ogóle nie są tworzone obiekty ramki. W rezultacie,
# prawie wszystkie wywołania funkcji Pythona przyspieszyły znacząco. Prowadzi to do prawie
# 3-7% przyspieszenia w pyperformance.


@dataclass
class Person:
    name: str

    @classmethod
    def from_str(cls, name: str) -> Self:
        return cls(name)

print(Person.from_str('Krzys'))

"""Напечатать таблицу умножения от 2 до 5:"""


first_factor = 2 # первый множитель
second_factor = 1 # второй множитель

while first_factor <= 5:
    if second_factor <= 10:
        product = first_factor * second_factor # выражение умножения
        print(f"{first_factor}", " x ", f"{second_factor}", "=", f"{product}")
        second_factor += 1
    else:
        first_factor += 1
        second_factor = 1
        print()

# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

def task1(input_data: str) -> dict[int: int | tuple[int]]:
    first, second, third, *other = (int(i) for i in input_data.split("/"))
    return {
        second: first,
        third: tuple(other)
    }


print("task1")

input_data = "1/2/3/4/5/6"

print(task1(input_data))


# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


def task2(text: str) -> dict[str: int]:
    return {i: ord(i) for i in text}


print("\ntask2")

text = "afdskll"
print(task2(text))


# Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

def task3(n: int):
    my_iter = iter(task2(text).items())
    for i in range(n):
        print(next(my_iter))


print("\ntask3")

task3(5)


# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


def task4(max_num: int, except_sum: int):
    """0 - нечетное, поэтому, не как на семинаре, range с 2 )"""
    return (i for i in range(2, max_num + 1, 2) if sum(int(digit) for digit in str(i)) != except_sum)


print("\ntask4")
for i in task4(100, 8):
    print(i, end="\t")
print()


# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


def task5(max_num: int, except_fizz: int, except_buzz: int) -> list[int | str]:
    result_list = []
    for i in range(1, max_num + 1):
        if i % (except_fizz * except_buzz) == 0:
            result_list.append("FizzBuzz")
        elif i % except_fizz == 0:
            result_list.append("Fizz")
        elif i % except_buzz == 0:
            result_list.append("Buzz")
        else:
            result_list.append(i)
    return result_list


def task5_gen(max_num: int, except_fizz: int, except_buzz: int):
    for i in range(1, max_num + 1):
        if i % (except_fizz * except_buzz) == 0:
            yield "FizzBuzz"
        elif i % except_fizz == 0:
            yield "Fizz"
        elif i % except_buzz == 0:
            yield "Buzz"
        else:
            yield i


print("\ntask5")

print(f"{type(task5(50, 3, 5))}, {task5(50, 3, 5).__sizeof__()}")
for i in task5(50, 3, 5):
    print(i, end="\t")

print(f"\n{type(task5_gen(50, 3, 5))}, {task5_gen(50, 3, 5).__sizeof__()}")
for i in task5_gen(50, 3, 5):
    print(i, end="\t")

print()


# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


def task6():
    LOWER_LIMIT = 2
    UPPER_LIMIT = 10
    COLUMNS = 4

    """ почему-то первое выражение уходит на 1 символ левее без этой строчки
        я так понимаю, из-за распаковки что-то нарушается
    """
    print(" ", end="")
    print(*(
        f"{k:>2} X {j:>2} = {k * j:>2}\n\n" if j == UPPER_LIMIT and k == i + COLUMNS - 1
        else f"{k:>2} X {j:>2} = {k * j:>2}\n" if k == i + COLUMNS - 1
        else f"{k:>2} X {j:>2} = {k * j:>2}\t\t"
        for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMNS)
        for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
        for k in range(i, i + COLUMNS)))


print("\ntask6")

task6()


# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def task7(count_numbers: int, first_number=2):
    current_num = first_number
    counter = 0
    while counter < count_numbers:
        if is_prime(current_num):
            counter += 1
            yield current_num
        current_num += 1


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


print("\ntask7")

count_num = 10
for i in task7(count_num):
    print(i, end="\t")
print()

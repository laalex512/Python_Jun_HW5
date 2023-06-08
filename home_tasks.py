# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def home_task1(path: str) -> tuple[str]:
    res_list = []
    res_list.append(path[0:path.rfind("\\"):])
    res_list.append(path[path.rfind("\\") + 1::].split(".")[0])
    res_list.append(path[path.rfind("\\") + 1::].split(".")[1])
    return tuple(res_list)


print("\nhome_task1:")
print(home_task1("D:\GeekBrains\Python jun\Sem5\home_tasks.py"))


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def home_task2(names: list[str], bids: list[int], premium: list[str]):
    return {names[i]: float(premium[i].replace("%", "")) / 100 * bids[i] for i in range(len(names))}


print("\nhome_task2:")

names = ["Ivanov", "Petrov", "Sidorov"]
bids = [50000, 70000, 90000]
premium = ["10.5%", "15.3%", "20%"]
for key, value in home_task2(names, bids, premium).items():
    print(f"{key}: {value}")


# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def home_task3(count_nums: int):
    a, b = 0, 1
    counter = 1
    while counter <= count_nums:
        yield a
        a, b = b, a + b
        counter += 1


print("\nhome_task3:")

count_nums = 10
for i in home_task3(count_nums):
    print(i, end="\t")

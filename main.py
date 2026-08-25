def string_length(string: str) -> int:
    """Повертає довжину рядка"""
    return len(string)


print(string_length('hello world!'))


def string_concatenation(string1: str, string2: str) -> str:
    """Повертає конкатенацію 2 рядків"""
    return string1 + string2


print(string_concatenation('Anna', ' Smith'))


def squared(number: int) -> int:
    """Повертає число піднесене до квадрату"""
    return number ** 2


print(squared(4))


def sum_numbers(a: int, b: int) -> int:
    """Повертає сумму 2-ох чисел"""
    return a + b


print(sum_numbers(10, 15))


def division(c: int, d: int) -> tuple[int, int]:
    """Повертає ціле число після ділення і залишок"""
    integer_part = c // d
    remainder = c % d
    return integer_part, remainder


print(division(13, 2))


def arithmetic_mean(numbers: list[int]) -> float:
    """Повертає середнє арефметичне чисел у списку"""
    total = sum(numbers)
    length_numbers = len(numbers)
    return total / length_numbers


print(arithmetic_mean([1, 2, 3, 4, 5]))


def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    """Повертає список, який містить спільні елементи обох списків"""
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


print(common_elements([1, 2, 3, 4, 5], [3, 5, 8, 9, 2]))


def all_keys(dictionary: dict[str, int]) -> list[str]:
    """Повертає всі ключі у словнику"""
    return list(dictionary.keys())


alphabet = {'a': 1, 'b': 2, 'c': 3}
print(all_keys(alphabet))


def merging_of_dictionaries(dict1: dict, dict2: dict) -> dict:
    """Повертає перший словник, доповнений другим"""
    dict1.update(dict2)
    return dict1


alphabet2 = {'d': 4, 'e': 5, 'f': 6}
print(merging_of_dictionaries(alphabet, alphabet2))


def union_of_sets(set1: set[int], set2: set[int]) -> set[int]:
    """Повертає об'єднання двух множин"""
    return set1 | set2


print(union_of_sets({1, 2, 3, 4}, {5, 6, 7, 8}))


def is_subset(set1: set[int], set2: set[int]) -> bool:
    """Повертає відповідь, чи є одна множина підмножиною іншої"""
    return set1.issubset(set2)


print(is_subset({1, 2, 3, 4}, {1, 2, 3, 4, 5, 6}))


def parity_check(number: int) -> str:
    """Повертає відповідь, чи вказане число парне/непарне"""
    if number % 2 == 0:
        return 'Парне!'
    else:
        return 'Непарне!'


print(parity_check(5))
print(parity_check(6))


def even_numbers_only(list_numbers: list[int]) -> list[int]:
    """Повертає новий список, який містить лише парні числа"""
    new_list = []
    for number in list_numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


def even_numbers_only2(list_numbers: list[int]) -> list[int]:
    """Повертає новий список, який містить лише парні числа"""
    return [number for number in list_numbers if number % 2 == 0]


print(even_numbers_only2([7, 8, 9, 10, 11]))


print(even_numbers_only([1, 2, 3, 4, 5, 6]))


many_numbers = [11, 20, 30, 43, 50]

even_numbers = list(filter(lambda x: x % 2 == 0, many_numbers))

print(even_numbers)

even_numbers2 = [number for number in many_numbers if number % 2 == 0]

print(even_numbers2)
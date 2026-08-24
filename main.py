def string_length(string):
    return len(string)
print(string_length('hello world!'))

def string_concatenation(string1, string2):
    return string1 + string2
print(string_concatenation('Anna', ' Smith'))

def squared(number):
    return number ** 2
print(squared(4))

def summa(a, b):
    return a + b
print(summa(10, 15))

def division(c, d):
    integer_part = c // d
    remainder = c % d
    return integer_part, remainder
print(division(13, 2))

def arithmetic_mean(numbers):
    summa_numbers = sum(numbers)
    length_numbers = len(numbers)
    return summa_numbers / length_numbers
print(arithmetic_mean([1, 2, 3, 4, 5]))

def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
print(common_elements([1, 2, 3, 4, 5], [3, 5, 8, 9, 2]))

def all_keys(dictionary):
    return dictionary.keys()
alphabet = {'a': 1, 'b': 2, 'c': 3}
print(all_keys(alphabet))

def merging_of_dictionaries(dict1, dict2):
    dict1.update(dict2)
    return dict1
alphabet2 = {'d': 4, 'e': 5, 'f': 6}
print(merging_of_dictionaries(alphabet, alphabet2))

def union_of_sets(set1, set2):
    return set1 | set2
print(union_of_sets({1, 2, 3, 4}, {5, 6, 7, 8}))

def set_verification(set1, set2):
    return set1.issubset(set2)
print(set_verification({1, 2, 3, 4}, {1, 2, 3, 4, 5, 6}))

def parity_check(number):
    if number % 2 == 0:
        return'Парне!'
    else:
        return 'Непарне!'
print(parity_check(5))
print(parity_check(6))

def even_numbers_only(list_numbers):
    new_list = []
    for number in list_numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list
print(even_numbers_only([1, 2, 3, 4, 5, 6]))

many_numbers = [10, 20, 30, 40, 50]
even_and_odd = list(filter(lambda x: x % 2 == 0, many_numbers))
print(even_and_odd)
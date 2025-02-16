# Программа a: Удаление элементов, которые встречаются только один раз
from collections import Counter


def remove_unique_elements(lst):
    counts = Counter(lst)
    return [x for x in lst if counts[x] > 1]


lst = [4, 3, 5, 3, 4, 4, 7, 8]
print(remove_unique_elements(lst))


# Программа b: Наибольшая последовательность подряд идущих одинаковых чисел
def longest_consecutive_sequence(lst):
    if not lst:
        return []

    max_seq = []
    current_seq = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_seq.append(lst[i])
        else:
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
            current_seq = [lst[i]]

    return max_seq if len(max_seq) >= len(current_seq) else current_seq


lst = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
print(longest_consecutive_sequence(lst))


# Программа c: Сортировка списка по количеству вхождений элементов
def sort_by_frequency(lst):
    counts = Counter(lst)
    return sorted(lst, key=lambda x: (-counts[x], lst.index(x)))


lst = [4, 3, 3, 2, 2, 2, 1]
print(sort_by_frequency(lst))

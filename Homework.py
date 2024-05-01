# def tpl_sort(tpl):
#     for element in tpl:
#         if not isinstance(element, int):
#             return tpl
#     return tuple(sorted(tpl))
# print(tpl_sort((2,5,5,6,1)))

# def sieve(lst):
#     a = set(lst)
#     return tuple(a)[::-1]
#     # a = []
#     # [a.append(item) for item in reversed(lst) if item not in a]
#     # return tuple(a)
# print(sieve([1, 2, 3, 3, 2]))

# def del_from_tuple(tpl, elem):
#     lst = list(tpl)
#     if elem in tpl:
#         lst.remove(elem)
#     return tuple(lst)
# print(del_from_tuple((1,4,6,5,4,1),1))

# data = ['Elli', 'Miles', 'Kratos', 'Joel', 'Peter', 'Nathan']
# print(sorted(data))

# duplicates = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
# unique = {}
# for i in duplicates:
#     unique[i] = unique.get(i,0) + 1
# print(unique)
# for key,value in unique.items():
#     if value >= 3:
#         duplicates = [x for x in duplicates if x != key]
# print(duplicates)

# b = []
# for number in duplicates:
#     if unique[number] < 3:
#         b.append(number)

from random import shuffle
 
test_list = [1, 4, 5, 6, 3]
shuffle(test_list)
print("Перемешаный лист: " + str(test_list))
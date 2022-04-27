from django.test import TestCase

# Create your tests here.
names = ['Dawid', 'Marian', 'M', 'd', 'dawid ciii', 'dawid ciii', 'Dawid']
ages = [30, 50, 50, 5, 50, 50, 12]
lists = list(zip(names, ages))
print(lists)
dict_list = []

dictionary = {}
for new in range(0, len(names)):
    dictionary['name'] = lists[new][0]
    dictionary['age'] = lists[new][0]
    dict_list.append(dictionary)
print(dict_list)

'''rom random import randint
from timeit import timeit


list_dicts = []
for _ in range(10):     # number of dicts in the list
    dict_tmp = {}
    for i in range(10):   # number of keys for each dict
        dict_tmp[f"key{i}"] = randint(0,50)
    list_dicts.append( dict_tmp )

print(list_dicts)
'''

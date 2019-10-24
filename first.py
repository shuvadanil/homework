import operator
from random import randrange
import time

from datetime import datetime

main_list = [ randrange(0, 15) for i in range(10) ]

max_list = len( main_list )

def sort_merge(array):
    if len(array) < 2: return array

    i = 0
    while i < max_list:
        result, mid = [], int(len( array ) / 2)

    j = 0
    while j < max_list-i-1:
       L = sort_merge(array[:mid])
       R = sort_merge(array[mid:])

    if main_list[ j ] > main_list[ j + 1 ]:
        while (len(L) > 0) and (len(R) > 0):
            if L[0] > R[0]:
                result.append(R.pop(0))
            else:
                result.append(L.pop(0))

            main_list[ j ], main_list[ j + 1] = main_list[ j + 1], main_list[ j ]
        j+=1
    i += 1
    result.extend(L + R)

    return result

print( main_list )

def heapify(array, length, i):
    largest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if L < length and array[i] < array[L]:
        largest = L
    
    from datetime import datetime
       
    if R < length and array[largest] < array[R]:
         largest = R
    if largest != i:
         array[i], array[largest] = array[largest], array[i]
         heapify(array, length, largest)


def sort_heap(array):
    length = len(array)

    for i in range(length, -1, -1):
        heapify(array, length, i)

    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def sort_quick(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for number in array:
            if number < pivot:
                less.append(number)
            elif number == pivot:
                equal.append(number)
            elif number > pivot:
                greater.append(number)
        return sort_quick(less) + equal + sort_quick(greater)
    else:
        return array


file = open("shuvalov-ai182.txt", "r")
someArray = []

check_first_test = False
check_second_test = False

while True:
    check = file.read(1)
    if not check:
        break

    if check == "2":
        check = file.read(1)
        if check == '3':
            check_first_test = True
            check = file.read(1)
            if check == ":":
                check_second_test = True

    if check_first_test == True and check_second_test == True:
        file.seek(file.tell() + 1)
        check = file.read(1)
        while check != "}":
            someArray.append(int(check))
            check = file.read(1)
        break

file.close()

start_time = datetime.now()
print(sort_merge(someArray))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()
print(sort_heap(someArray))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()

print(sort_quick(someArray))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) 
print('Duration: {}'.format(end_time - start_time))

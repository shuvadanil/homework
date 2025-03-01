x = 1
y = 2
z = 5

if z <= 1 :
    print("Hey")
else:
    print("Ho")
 #Shuvalov Danil Ai-182

#Сортировка 1
def BubbleSort(someArray):
    for i in range(0, len(someArray) - 1):
        swapCheck = False
        for j in range(len(someArray) - i - 1):
            if (someArray[j] > someArray[j + 1]):
                someArray[j], someArray[j + 1] = someArray[j + 1], someArray[j]
                SswapCheck = True
    if (not swapCheck): 
        swapCheck = False
    return someArray

myArray = [234, 655, 618, 687, 524, 698, 947, 332, 890, 124, 508, 809, 325, 456, 344]
print(BubbleSort(myArray))

#Сортировка 2
def SelectionSort(someArray):
    for i in range(len(someArray) - 1):
        minElement = i
        for j in range(i + 1, len(someArray)):
            if (someArray[j] < someArray[minElement]):
                minElement = j
        if minElement != i:
            someArray[i], someArray[minElement] = someArray[minElement], someArray[i]
    return someArray

anotherMyArray = [342, 231, 231, 602, 23, 312, 540, 233, 534, 472, 544, 233, 968, 423, 114]
taskFromPractice = [21, 34, 19, 65, 35, 7, 45, 43, 76]
print(SelectionSort(anotherMyArray))
print(SelectionSort(taskFromPractice))

#Сортировка 3
def InsertionSort(someArray):
    for i in range(1, len(someArray)):
        checkingNumber = someArray[i]
        j = i - 1
        while j >= 0 and checkingNumber < someArray[j]:
            someArray[j + 1] = someArray[j]
            j -= 1
        someArray[j + 1] = checkingNumber
    return someArray

andAnotherAnotherMyArray = [456, 234, 123, 243, 652, 339, 323, 432, 383, 967, 123, 225, 174, 234, 411]
anotherTaskFromPractice = [34, 21, 45, 67, 34, 78, 53, 54, 87]
print(InsertionSort(andAnotherAnotherMyArray))
print(InsertionSort(anotherTaskFromPractice))

def bubbleSsssort(array):
    for i in range(len(array)):
        print(array)
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

def selectionSort(array):
    for i in range(len(array)):
        minind=i
        for j in range(i+1,len(array)):
            if array[j]<array[minind]:
                minind=j
        array[i],array[minind]=array[minind],array[i]


data=[23,12,33,1,234,5,2,13,46,2,42,5]
# bubbleSsssort(data)
selectionSort(data)
print(data)
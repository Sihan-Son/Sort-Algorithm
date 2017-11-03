list=[8,9,5,7,6,1,3,2,4]

length = len(list)

for i in range(length-1):
    indexMin = i
    for j in range(i + 1, length):
        if list[indexMin] > list[j]:
            indexMin = j
    temp = list[indexMin]
    list[indexMin] = list[i]
    list[i] = temp
    print(list)
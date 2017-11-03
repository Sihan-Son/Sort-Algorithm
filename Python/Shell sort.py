def shellSort(list):
    for gap in range(5,0,-2):
        for i in range(gap, len(list)):
            key = list[i]
            j = i
            while j >= gap and list[j - gap] > key:
                list[j] = list[j - gap]
                j -= gap
            list[j] = key
        print(list)

list =[6, 5, 12, 4, 10, 9, 0, 2, 7, 4, 1, 3]
a = [8,7,6,1,2,3,9,4,5,0]
#shellSort(list)
shellSort(a)
print(a)
list = [2,3,5,9,7,1,6,12,48,56]

for i in range(len(list) - 1):
    for j in range(1, len(list) - i):
        if list[j - 1] > list[j]:
            temp = list[j - 1]
            list[j - 1] = list[j]
            list[j] = temp

print(list)
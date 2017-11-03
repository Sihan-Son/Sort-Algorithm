x = [40,30,70,60,50,10,20]
print("초기값")
print(x)
print("정렬")
for i in range(1, len(x)):
    j = i - 1
    key = x[i]
    while x[j] > key and j >= 0:
        x[j+1]  = x[j]
        j = j - 1
    x[j+1] = key

    print(x)

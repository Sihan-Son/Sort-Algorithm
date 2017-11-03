def swap(array,x,y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def printArray(array):
    sizeOfArray = 8
    for i in range(1,sizeOfArray):
        print("%3d" %array[i],end= " ")
    print()

array = [0,5,26,37,1,61,11,59]

print("입력 데이터 >> " ,end = " ")
printArray(array)
print()

rt_cnt = 0
for loop in range(7, 0, -1):
    rt_cnt +=1
    for i in range(((int)(loop / 2)), 0, -1) :
        rtemp = array[i]
        j = 2 * i
        while(j<=loop):
            if (j < loop) & (array[j] < array[j+1]):
                j+=1
            if rtemp < array[j]:
                array[(int)(j / 2)] = array[j]
                j *=2
            else :
                break
            array[(int)(j / 2)] =rtemp
        print("%3d 회전 >> " %rt_cnt, end = " ")
        printArray(array)
    print("%3d 회전 >> " % rt_cnt, end =" ")
    printArray(array)

    swap(array, 1, loop)

    print("%3d 교환 >> " %rt_cnt, end = " ")
    printArray(array)
    print()
print()
print("최종 결과 >> ",end =" ")
printArray(array)
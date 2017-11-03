def swap(array, i, j) :

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def Partiton(array, left, right) :
    end = array[right]
    start = left-1

    for j in range(left, right) :
        if array[j] <= end :
            start+=1
            swap(array,start,j)

    swap(array,start+1,right)
    return (start+1)

def quicksort(array, count) :
    startIndex = 0
    endIndex = count -1
    top = -1

    stack =[]
    stack.append(startIndex)
    top +=1
    stack.append(endIndex)
    top +=1

    while top >= 0 :
        endIndex = stack.pop()
        top -= 1
        startIndex = stack.pop()
        top -= 1

        p = Partiton(array, startIndex, endIndex)

        if p -1 > startIndex :
            stack.append(startIndex)
            top += 1
            stack.append(p-1)
            top += 1

        if p + 1 < endIndex :
            stack.append(p+1)
            top += 1
            stack.append(endIndex)
            top += 1

list = [6,3,11,9,12,2,8,15,18,7,14]
print(list)

quicksort(list, len(list))

print(list)
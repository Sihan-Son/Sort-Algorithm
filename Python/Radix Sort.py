def radix(digit, data):
    radix_queue[digit][queueIndex[digit]] = data
    queueIndex[digit] +=1

def putData():
    k=0
    for i in range(0,10):
        for j in range(0,2):
            data[k] = radix_queue[i][j]
            k+=1

def initQueuePos():
    for i in range(0,len(queueIndex)):
        queueIndex[i] -=2

def printQueue():

    for i in range(0,10):
        print("큐%2d >> " %(i + 1), end=" ")
        for j in range(0,2):
            print("%3d"%radix_queue[i][j],end = " ")
        print()


radix_queue = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
data = [15,23,31,49,58,64,72,80,96,7,5,93,81,79,68,54,42,30,26,17]
var_data =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

queueIndex =[0,0,0,0,0,0,0,0,0,0]

t =10
n = 1
k = 1

while(t<=100): #100은 자릿수에 따라 수정
    for i in range(0,len(data)):
        digit = int((data[i]%t)/n)
        radix(digit,data[i]) # switch문을 지원 안해서 사용
        if(i ==len(data)-1):
            print("K%d 정렬 큐 상태"%k)
            printQueue()
            print()
            initQueuePos()
            putData()
            t*=10
            n*=10
            k+=1

var_data = data
print("K2 정렬 자료")
print(var_data)

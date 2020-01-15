import os
from time import *
import psutil

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr=[]
arra = input("Enter the series to sort: ")
t1=time()
arra=arra.split(' ')
for i in range(len(arra)):
    arr.append(int(arra[i]))

insertionSort(arr)

for i in range(len(arr)):
    print("% d" % arr[i],end=' ')
t2=time()
t=t2-t1
py=psutil.Process(os.getpid())
memory_used=py.memory_info().rss
print()
print("Time consumed by Insertion sort: %.30f"%t)
print("Memory consumed by Insersion sort: ",memory_used,'B')

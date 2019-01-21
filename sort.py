# Insertion Sort
def ins_sort(arr):
    for i in range(len(arr)):
        if i == 0:
            continue
        sm = arr[i]
        j = i - 1
        while j>=0 and arr[j] > arr[j+1] :
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = sm

#Bubble Sort
def bub_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1,len(arr)):
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

#Selection Sort
def sel_sort(arr):
    for i in range(len(arr)-1):
        sm = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[sm]):
                sm = j
        if(sm != i):
            temp = arr[sm]
            arr[sm] = arr[i]
            arr[i] = temp

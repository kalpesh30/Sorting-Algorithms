import random
import time
import sort

arr = []
arr2 = []
arr3 = []

# populating an array with 1000 elements
for i in range(1000):
    arr.append(random.randint(1000,500000))

# populating an array with 10000 elements
for i in range(10000):
    arr2.append(random.randint(1000,500000))

# populating an array with 100000 elements
for i in range(100000):
    arr3.append(random.randint(1000,50000000))
    
# For array size 1000
st1 = time.time()
sort.ins_sort(arr)
en1 = time.time()


# For array size 10000
st2 = time.time()
sort.ins_sort(arr2)
en2 = time.time()


# For array size 100000
st3 = time.time()
sort.ins_sort(arr3)
en3 = time.time()


# Writing into the file
filename = "AlgorithimTime.txt"
file = open(filename,"a")
file.write("Insertion Sort\n")
file.write("--------------\n")
file.write("1000 array size         " + str(10**6 * (en1 - st1)) + " microseconds\n")
file.write("10000 array size            " + str(10**6 * (en2 - st2)) + " microseconds\n")
file.write("100000 array size           " + str(10**6 * (en3 - st3)) + " microseconds\n")
file.close()


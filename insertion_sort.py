#include <stdio.h>

def insertion_sort(arr):
    for j in range(1, len(arr)):
        i = j - 1
        key = arr[j]
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key


if __name__ == '__main__':
    arr = [3, 5, 2, 1, 4, -1]
    insertion_sort(arr)
    print(arr)

def shell_sort(arr):
    n = len(arr)
    # 初始步長
    gap = n // 2
    while gap > 0:
        for i in range(gap, n): 
            # 每个步長進行插入排序
            temp = arr[i]
            j = i
            # 插入排序
            while j >= 0 and j-gap >= 0 and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(i)
        # 得到新的步長
        gap = gap // 2
        print(arr, gap)


if __name__ == '__main__':
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    shell_sort(nums)
    # print(nums)

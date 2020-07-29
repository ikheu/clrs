def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    # 后部分是合并两个排序的数组，result 这里还可以优化，避免数组的动态扩展
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if right:
        result.extend(right[j:])
    return result


if __name__ == "__main__":
    nums = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", nums)
    print("Sorted:", mergeSort(nums))

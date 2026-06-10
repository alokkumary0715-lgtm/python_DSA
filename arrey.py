#search in rotated sorted array
# def count_occurrence(arr, target):
#     n = len(arr)
#     for i in range (0,n):
#         if arr[i] == target:
#             return i
#     return -1
        
# #driver code
# arr = [1,2,6,3,4,4,4,5]
# target = 10
# print(count_occurrence(arr, target))


#optimal solution
def count_occurance_optimized(arr, target):
    n = len(arr)
    low = 0
    high = n - 1 
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid]<=arr[high]:  # right half is sorted
            if arr[mid] <= target <= arr[high]:  # target is in right half
                low = mid + 1
            else:
                high = mid - 1
        else:  # left half is sorted
            if arr[low] <= target <= arr[mid]:  # target is in left half
                high = mid - 1
            else:
                low = mid + 1
    return -1

#driver code
arr = [1,2,6,3,4,4,4,5]
target = 10
print(count_occurance_optimized(arr, target))
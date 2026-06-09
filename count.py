#count occurance in soted arrey
def count_occurrence(arr, target):
    left = -1
    right = -1
    n = len(arr)
    for i in range (0,n):
        if arr[i] == target:
            if left == -1:
                left = i
            right = i
    if left == -1:
        return 0
    return right - left + 1


#driver code
arr = [1,2,2,3,4,4,4,5]
target = 4
print(count_occurrence(arr, target))


#optimized code we try binar
"""here we wwill use lower bound and upper bound to find the first and last occurence of the target in the array and then we will return the count of the target in the array"""
def lower_bound(arr, target):
    lb = -1
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            mid = lb
            left = mid + 1
        else:
            right = mid - 1
    return lb        


def upper_bound(arr, target):
    ub = n     # why we keep n here because if the target is greater than all the elements in the array then we will return n as the upper bound
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            mid = ub
            left = mid + 1
        else:
            right = mid - 1
    return ub

def count_occurrence_optimized(arr, target):
    lb = lower_bound(arr, target)
    if lb == -1:
        print(0)
    else:
        ub = upper_bound(arr, target)
        print(ub - lb)

arr = [1,2,2,3,4,4,4,5]
target = 4 
count_occurrence_optimized(arr, target)



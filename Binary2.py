#lower and upper bound of a binary search
"""lower bound =smallest value such nums[i] >= target
upper bound = smallest value such that nums[i] > target"""


def lower_bound(arr, target):
    n = len(arr)
    lb = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb



def upper_bound(arr, target):
    n = len(arr)
    ub = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub   


arr = list(map(int, input("Enter a sorted list of integers (space separated): ").split()))
target = int(input("Enter the target value to search for: "))
lb = lower_bound(arr, target)
print(f"Lower bound index: {lb}")
ub = upper_bound(arr, target)
print(f"Upper bound index: {ub}")

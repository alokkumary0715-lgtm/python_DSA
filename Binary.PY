"""A real life example where binary works
#coding problem
# iterative solution
# Recursive solution
# Time and space complexity"""

# in a binary search tree, we can find the minimum value by going to the leftmost node
# List should be sorted for binary search to work

""" we use 2 pointers to find the middle element of the list and compare it with the target value
# to find the middle element, we can use the formula: mid = left + (right - left) // 2
# if the middle element is equal to the target value, we return the index of the middle element
# if the middle element is less than the target value, we move the left pointer to the right of the middle element
# if the middle element is greater than the target value, we move the right pointer to the left of the middle element"""

def binary_search_iterative(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:   # we want this to continue until low is less than or equal to high, because if low is greater than high, it means we have exhausted the search space
        mid = (low + high) // 2    # WE WANT VALUE OF MID TO BE AN INTEGER, SO WE USE FLOOR DIVISION
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1   # if we exhaust the search space and do not find the target value, we return -1 to indicate that the target value is not present in the list
    
arr = list(map(int, input("Enter a sorted list of integers (space separated): ").split()))
target = int(input("Enter the target value to search for: "))

result = binary_search_iterative(arr, target)
if result != -1:    print(f"Element found at index: {result}")
else:   print("Element not found in the list")

# recursive solution
def binary_search_recursive(arr, target, low, high):
    if low > high: #base case: if low is greater than high, it means we have exhausted the search space and do not find the target value, we return -1 to indicate that the target value is not present in the list
        return -1
    mid = (low+high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, high)
    else:
        return binary_search_recursive(arr, target, low, mid-1)
    

arr = list(map(int, input("Enter a sorted list of integers (space separated): ").split()))
target = int(input("Enter the target value to search for: "))
low = 0
high = len(arr) - 1
result = binary_search_recursive(arr, target, low, high)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")
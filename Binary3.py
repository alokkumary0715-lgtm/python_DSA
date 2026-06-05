#search insertion point
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums = list(map(int, input("Enter a sorted list of integers (space separated): ").split()))
target = int(input("Enter the target value to search for: "))
result = searchInsert(nums, target)
print(f"Target value can be inserted at index: {result}")
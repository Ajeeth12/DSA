def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0  # Index to place the next unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    print(slow + 1)  # The number of unique elements
nums = [1, 1, 2, 2, 3, 4, 7, 8, 8]
remove_duplicates(nums)


## Time Complexity = O(n) - Single pass through the array
## Space Complexity =  O(1) - In-place modification, no extra memory
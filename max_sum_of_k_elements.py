def max_sum_k_elements(nums, k):
    max_sum = curr_sum =sum(nums[:k])
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum)

    print(max_sum)

nums = [2, 1, 5, 1, 3, 2]
k = 3
max_sum_k_elements(nums, k)
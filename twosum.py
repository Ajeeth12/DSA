def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in seen:
            # Complement found — return its index and current index
            return [seen[complement], i]
        # Store the current number and its index
        seen[num] = i

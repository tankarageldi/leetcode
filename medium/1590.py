class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        # Step 1: Calculate total sum and target remainder
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0  # The array is already divisible by p

        # Step 2: Use a dict to track prefix sum mod p
        mod_map = {
            0: -1
        }  # To handle the case where the whole prefix is the answer
        current_sum = 0
        min_len = n

        # Step 3: Iterate over the array
        for i in range(n):
            print("===========Iteration==========")
            current_sum = (current_sum + nums[i]) % p
            print("Current Sum on iteration ",i, " ",current_sum)
            # Calculate what we need to remove
            needed = (current_sum - remainder + p) % p
            print("Needed value to remove, on iteration ",i, " ",needed)
            # If we have seen the needed remainder, we can consider this subarray
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
                print("Min_len, on iteration ",i, " ",min_len)

            # Store the current remainder and index
            mod_map[current_sum] = i
            print("Current remainder and index, on iteration",i, " ",mod_map[current_sum])

        # Step 4: Return result
        return -1 if min_len == n else min_len

sol = Solution()
nums = [6,3,5,2]
p = 9

print(sol.minSubarray(nums,p))
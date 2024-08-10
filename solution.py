class Solution:
    def findLHS(self, nums):
        frequency_map = {}
        
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        max_length = 0

        for num in frequency_map:
            if num + 1 in frequency_map:
                max_length = max(max_length, frequency_map[num] + frequency_map[num + 1])

        return max_length


solution = Solution()

nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
output1 = solution.findLHS(nums1)
print("Input: {}\nOutput: {}".format(nums1, output1))

nums2 = [1, 2, 3, 4]
output2 = solution.findLHS(nums2)
print("Input: {}\nOutput: {}".format(nums2, output2))

nums3 = [1, 1, 1, 1]
output3 = solution.findLHS(nums3)
print("Input: {}\nOutput: {}".format(nums3, output3))

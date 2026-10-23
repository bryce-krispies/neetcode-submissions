class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counts = {}
        frequencies = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            frequencies[count].append(num)

        for i in range(len(frequencies) - 1, -1, -1):
            for frequency in frequencies[i]:
                ans.append(frequency)
                if len(ans) == k:
                    return ans

        return None

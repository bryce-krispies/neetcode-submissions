class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            freq[count].append(num)

        for idx in range(len(freq) - 1, -1, -1):
            for num in freq[idx]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return None
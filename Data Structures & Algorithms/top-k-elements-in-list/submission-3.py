class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        buckets = [[] for _ in range(len(nums)+1)]
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            buckets[count].append(num)

        for i in range(len(buckets)-1, -1, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        return None
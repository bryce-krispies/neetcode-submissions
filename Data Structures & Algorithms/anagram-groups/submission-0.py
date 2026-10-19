class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            temp = str(sorted(word))
            if temp in seen:
                seen[temp].append(word)
            else:
                seen[temp] = [word]

        return list(seen.values())
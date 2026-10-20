class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_to_join = []
        for string in strs:
            strs_to_join.append(str(len(string)))
            strs_to_join.append("#")
            strs_to_join.append(string)
        return "".join(strs_to_join)

    def decode(self, s: str) -> List[str]:
        strs_to_return = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strs_to_return.append(s[i:j])
            i = j
        return strs_to_return
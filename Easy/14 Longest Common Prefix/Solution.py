class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for characters in zip(*strs):
            if len(set(characters)) == 1:
                common_prefix += characters[0]
            else:
                break

        return common_prefix
      
